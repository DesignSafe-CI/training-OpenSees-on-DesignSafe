def connect_tapis(token_filePath: str = "~/.tapis_tokens.json",
                  base_url: str = "https://designsafe.tapis.io",
                  username: str = "",
                  password: str = "",
                  force_connect: bool = False):
    """
    Connect to a Tapis platform (e.g., DesignSafe) with automatic token handling.

    Behavior
    --------
    - Looks for a saved access token at `token_filePath` (default: ~/.tapis_tokens.json).
    - If present and not expired, uses it to create an authenticated Tapis client.
    - If missing/expired, or when `force_connect=True`, prompts for credentials,
      requests new tokens, and saves them back to `token_filePath`.
    - Prints expiration details for transparency.

    Parameters
    ----------
    token_filePath : str, default "~/.tapis_tokens.json"
        Path to the JSON file that stores the Tapis `access_token` and `expires_at`.
    base_url : str, default "https://designsafe.tapis.io"
        Tapis API endpoint base URL.
    username : str, default ""
        Optional preset username. If empty, you will be prompted.
    password : str, default ""
        Optional preset password. If empty, you will be prompted (securely).
    force_connect : bool, default False
        If True, ignores any valid saved token and performs a fresh login.

    Returns
    -------
    object
        An authenticated `Tapis` client object ready to use.

    Notes
    -----
    - The token file stores: `{"access_token": "...", "expires_at": "...ISO8601..."}`.
    - Expiry timestamps are treated as UTC if no timezone is present.
    - If the saved token cannot be parsed/validated, a fresh login is performed.

    Example
    -------
    t = connect_tapis()                        # use saved token or prompt as needed
    jobs = t.jobs.getJobList()                 # now you're authenticated

    Author
    ------
    Silvia Mazzoni, DesignSafe (silviamazzoni@yahoo.com)

    Date
    ----
    2025-08-14

    Version
    -------
    1.0
    """
    from tapipy.tapis import Tapis
    from getpass import getpass
    from datetime import datetime, timezone
    import json
    import os

    def _parse_expires_at(s: str) -> datetime | None:
        """Parse ISO8601 expiry, accepting 'Z' and naive strings; return aware UTC dt or None."""
        if not s:
            return None
        try:
            # normalize trailing 'Z' to +00:00
            s_norm = s.replace("Z", "+00:00")
            dt = datetime.fromisoformat(s_norm)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt.astimezone(timezone.utc)
        except Exception:
            return None

    def getTokensLoop():
        username = getpass("Username: ")
        password = getpass("Password: ")
        t = Tapis(base_url=base_url, username=username, password=password)
        try:
            t.get_tokens()
            return t
        except Exception as e:
            print(f" ** Warning ** could get token : {e},\n TRY AGAIN!")
            t= getTokensLoop()
            return t

        
    print(" -- Checking Tapis token --")
    token_path = os.path.expanduser(token_filePath)
    now = datetime.now(timezone.utc)

    t = None
    saved_expires_at = None
    valid_token = False

    # Try to load a saved token
    if os.path.exists(token_path):
        try:
            with open(token_path, "r") as f:
                tokens = json.load(f)
            saved_expires_at = _parse_expires_at(tokens.get("expires_at"))
            if tokens.get("access_token") and saved_expires_at and saved_expires_at > now:
                print(" Token loaded from file. Token is still valid!")
                t = Tapis(base_url=base_url, access_token=tokens["access_token"])
                valid_token = True
            else:
                print(" Token file found but token is missing/expired.")
                if saved_expires_at:
                    print(" Token expired at:", saved_expires_at.isoformat())
        except Exception as e:
            print(f" Could not read/parse token file ({token_path}): {e}")
    else:
        print(" No saved tokens found.")

    if force_connect:
        print(" Forcing a connection to Tapis (fresh login).")

    if not valid_token or force_connect:
        print("-- Connect to Tapis --")
        if not username:
            # username isn't sensitive; echoing can help avoid typos, but keeping your original choice:
            username = getpass("Username: ")
        if not password:
            password = getpass("Password: ")
        t = Tapis(base_url=base_url, username=username, password=password)
        try:
            t.get_tokens()
        except Exception as e:
            print(f" ** Warning ** could get token : {e},\n TRY AGAIN!")
            t= getTokensLoop()
        # Save the new token back to the chosen path
        try:
            tokens = {
                "access_token": t.access_token.access_token,
                "expires_at": t.access_token.expires_at.isoformat(),
            }
            os.makedirs(os.path.dirname(token_path), exist_ok=True)
            with open(token_path, "w") as f:
                json.dump(tokens, f)
            print(f" Token saved to {token_path}")
            saved_expires_at = _parse_expires_at(tokens["expires_at"])
        except Exception as e:
            print(f" Warning: could not save token to {token_path}: {e}")

    # Print expiry info (use stored/parsed date if needed)
    exp_to_show = saved_expires_at
    try:
        # if available, prefer the client object's value
        if getattr(t, "access_token", None) and getattr(t.access_token, "expires_at", None):
            exp_to_show = _parse_expires_at(str(t.access_token.expires_at)) or exp_to_show
    except Exception:
        pass

    if exp_to_show:
        print(" Token expires at:", exp_to_show.isoformat())
        print(" Token expires in:", str(exp_to_show - now))
    else:
        print(" Token expiry time unavailable.")

    print("-- LOG IN SUCCESSFUL! --")
    return t
