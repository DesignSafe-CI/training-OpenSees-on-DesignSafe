from __future__ import annotations




def get_user_path_tapis_uri(
    t,
    file_system: str = "none",                  # "none" | "mydata" | "community" | "work"
    work_system: str = "none",                  # "stampede3" | "ls6" | "frontera" | "none"
    paths_file_path: str = "~/MyData/.tapis_user_paths.json",
    force_refresh: bool = False,
) -> Union[str, Dict]:
    """
    Discover and cache user-specific Tapis base URIs for DesignSafe storage systems,
    then return either the entire dictionary or a single base URI.

    Author
    -------
    Silvia Mazzoni, DesignSafe (silviamazzoni@yahoo.com)

    Parameters
    ----------
    t : Tapipy client
        An authenticated Tapipy v3 client.
    file_system : {"none","mydata","community","work"}, optional
        Which base to return. Use "none" to return the full dictionary.
    work_system : {"stampede3","ls6","frontera","none"}, optional
        When file_system="work", which HPC system's Work base to return.
    paths_file_path : str, optional
        Location (on MyData or local home) where the JSON cache is stored.
        Default: "~/MyData/.tapis_user_paths.json".
    force_refresh : bool, optional
        If True, (re)discover all bases and overwrite the cache file.

    Returns
    -------
    Union[str, dict]
        - If file_system == "none": the full dict of bases (including subdict for "work").
        - Else: a single base URI string for the requested system.

    Notes
    -----
    - Stored values are full Tapis URIs (start with "tapis://" and end with "/").
    - Keys are lowercase: "mydata", "community", "work". For "work", values are a dict
      keyed by HPC system ("stampede3", "ls6", "frontera").
    """
    import json
    import os
    from pathlib import Path
    from typing import Dict, Optional, Union, Iterable, Sequence
    from OpsUtils import OpsUtils
    # ----------------------------
    # Inner helper: build Work Tapis URI from credential app
    # ----------------------------
    def get_user_work_tapis_uri(
        t,
        *,
        system_id: str,
        username: str,
        app_suffix: str = "-credential",
        job_name: str = "getWork",
        valid_systems: Iterable[str] = ("stampede3", "ls6", "frontera"),
        tapis_work_system_id: str = "cloud.data",
        work_roots: Sequence[str] = ("work", "work2", "work3", "work4"),
        ensure_trailing_slash: bool = True,
    ) -> str:
        """
        Submit the system's credential app, parse its archive path, and return:
            tapis://{tapis_work_system_id}/work/{allocation}/{username}/{system_id}/
        """
        sys_key = system_id.strip().lower()
        if sys_key not in {s.lower() for s in valid_systems}:
            raise ValueError(f"Unknown system '{system_id}'. Choose one of: {sorted(valid_systems)}")

        app_id = f"{sys_key}{app_suffix}"

        # Resolve latest app version
        try:
            latest = t.apps.getAppLatestVersion(appId=app_id)
            app_version = getattr(latest, "version", None) or "latest"
        except Exception:
            try:
                app = t.apps.getApp(appId=app_id, appVersion="latest")
                app_version = getattr(app, "version", None) or "latest"
            except Exception as exc2:
                raise RuntimeError(
                    f"Could not resolve latest version for appId='{app_id}': {exc2}"
                )

        # Submit temporary credential job
        try:
            submitted_job = t.jobs.submitJob(name=job_name, appId=app_id, appVersion=app_version)
        except Exception as exc:
            raise RuntimeError(
                f"Credential job submission failed for appId='{app_id}', version='{app_version}': {exc}"
            )

        # Extract HPC archive path
        archive_dir = getattr(submitted_job, "archiveSystemDir", None)
        if not archive_dir or not isinstance(archive_dir, str):
            raise RuntimeError("Response missing string field 'archiveSystemDir'.")

        # Example archive_dir:
        #   /work2/01121/stampede3/home/jdoe/job-abc
        parts = [p for p in archive_dir.split("/") if p]  # remove empties
        # find system segment
        try:
            sys_idx = next(i for i, seg in enumerate(parts) if seg.lower() == sys_key)
        except StopIteration:
            raise ValueError(
                f"Expected segment '/{sys_key}' in archiveSystemDir='{archive_dir}', but did not find it."
            )

        # find nearest work root before system segment and infer allocation
        work_idx = None
        work_roots_lc = {r.lower() for r in work_roots}
        for i in range(sys_idx - 1, -1, -1):
            if parts[i].lower() in work_roots_lc:
                work_idx = i
                break
        if work_idx is None:
            raise ValueError(
                f"Could not identify a Work root {tuple(work_roots)} in '{archive_dir}'."
            )

        alloc_idx = work_idx + 1
        if alloc_idx >= sys_idx:
            raise ValueError(
                f"Could not locate allocation segment between '{parts[work_idx]}' "
                f"and '{parts[sys_idx]}' in '{archive_dir}'."
            )

        allocation = parts[alloc_idx]
        uri = f"tapis://{tapis_work_system_id}/work/{allocation}/{username}/{sys_key}/"
        return uri if ensure_trailing_slash else uri.rstrip("/")

    # ----------------------------
    # normalize & validate inputs
    # ----------------------------
    fs = (file_system or "none").strip().lower()
    ws = (work_system or "none").strip().lower()

    # Handle loose input like "CommunityData"
    if "community" in fs:
        fs = "community"

    valid_file_systems = {"mydata", "community", "work", "none"}
    valid_work_systems = {"stampede3", "ls6", "frontera", "none"}

    if fs not in valid_file_systems:
        raise ValueError(f"file_system='{file_system}' not in {sorted(valid_file_systems)}")

    if fs == "work" and ws not in valid_work_systems - {"none"}:
        raise ValueError(f"work_system='{work_system}' not in {sorted(valid_work_systems - {'none'})}")

    cache_path = Path(os.path.expanduser(paths_file_path))

    # ----------------------------
    # helper: normalize URIs
    # ----------------------------
    def _with_scheme(u: str) -> str:
        u = u.strip()
        if not u:
            return u
        if not u.startswith("tapis://"):
            u = "tapis://" + u.lstrip("/")
        if not u.endswith("/"):
            u += "/"
        return u

    # ----------------------------
    # try reading existing cache
    # ----------------------------
    paths: Dict = {}
    if cache_path.exists() and not force_refresh:
        try:
            with cache_path.open("r", encoding="utf-8") as f:
                paths = json.load(f)
                print(f'found paths file: {cache_path}')
        except Exception:
            paths = {}

    # quick return if cache satisfies the request
    def _maybe_return_from_cache() -> Optional[Union[str, Dict]]:
        if not paths:
            return None
        if fs == "none":
            return paths
        if fs in {"mydata", "community"}:
            val = paths.get(fs)
            if isinstance(val, str) and val:
                return _with_scheme(val)
        if fs == "work":
            work = paths.get("work", {})
            if isinstance(work, dict) and ws in work and work[ws]:
                return _with_scheme(work[ws])
        return None

    cached = _maybe_return_from_cache()
    if cached is not None:
        return cached

    # ----------------------------
    # (re)discover all bases
    # ----------------------------
    print('discover all bases-')
    try:
        username = OpsUtils.get_tapis_username(t)
    except Exception as e:
        raise RuntimeError(f"Could not determine Tapis username: {e}")

    discovered: Dict = {
        "mydata": _with_scheme(f"designsafe.storage.default/{username}"),
        "community": _with_scheme("designsafe.storage.community"),
        "work": {}
    }

    # Discover Work bases using the new inner helper
    for system in ("stampede3", "ls6", "frontera"):
        try:
            base_uri = get_user_work_tapis_uri(t, system_id=system, username=username)
            discovered["work"][system] = _with_scheme(base_uri)  # idempotent
        except Exception:
            # Skip systems we can't resolve; they can be refreshed later
            continue

    # Persist to cache
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    with cache_path.open("w", encoding="utf-8") as f:
        json.dump(discovered, f, indent=2)
        print(f'saved data to {cacth_path}')

    # Return per request
    if fs == "none":
        return discovered
    if fs in {"mydata", "community"}:
        return discovered[fs]
    if fs == "work":
        if ws not in discovered["work"]:
            raise RuntimeError(
                f"Work base for '{ws}' not found during discovery. "
                f"Available: {sorted(discovered['work'].keys())}"
            )
        return discovered["work"][ws]

    return discovered
