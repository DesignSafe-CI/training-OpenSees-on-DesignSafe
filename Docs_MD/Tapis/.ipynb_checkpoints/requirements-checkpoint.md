# Dependencies (`requirements.txt`)

*Author: Silvia Mazzoni, DesignSafe ([silviamazzoni@yahoo.com](mailto:silviamazzoni@yahoo.com))*

A `requirements.txt` file lists the Python packages (and versions) your code needs so others can recreate the same environment.

## Quick start (install)

```bash
# In your active environment or venv
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### (DesignSafe/TACC one-time setup)

```bash
module load python/3.11
python -m venv $WORK/.venvs/opensees
source $WORK/.venvs/opensees/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
# In each job/session later:
# source $WORK/.venvs/opensees/bin/activate
```

## What goes in it?

Each line is one dependency. You can pin exact versions, allow compatible updates, or set ranges.

```txt
# Exact pin (most reproducible)
numpy==1.26.4

# Compatible release (allow bugfixes)
pandas~=2.2

# Version range
scipy>=1.12,<1.14

# Extras
matplotlib[qt]

# Only on certain Pythons/OSes
importlib-resources; python_version < "3.9"

# Include another file (base list or constraints)
-r base-requirements.txt
-c constraints.txt
```

### Pinning strategies (pick one)

* **Exact pins** `pkg==1.2.3` → maximum stability (recommended for HPC runs).
* **Compatible pins** `pkg~=1.2` → allow bugfixes, keep API.
* **Ranges** `pkg>=1.2,<2.0` → flexible but less deterministic.

## Constraints (optional but useful)

Keep top-level deps in `requirements.txt`, lock transitive deps in `constraints.txt`.

**requirements.txt**

```txt
numpy
pandas
scipy
-c constraints.txt
```

**constraints.txt**

```txt
numpy==1.26.4
pandas==2.2.2
scipy==1.12.0
```

Generate from a working env:

```bash
pip freeze > constraints.txt
```

## Updating the file

* Add/remove packages as needed.
* Re-pin occasionally from a clean env:

  ```bash
  pip install -r requirements.txt
  pip freeze > constraints.txt   # update locks
  ```

## Offline/cluster installs (optional)

Pre-download wheels once, then install without internet:

```bash
pip download -r requirements.txt -d $WORK/wheels
pip install --no-index --find-links $WORK/wheels -r requirements.txt
```

## Troubleshooting

* **Conflicts**: add/adjust `constraints.txt` to pin the clashing transitive pkg.
* **Wrong Python**: add markers (e.g., `pkg==X; python_version<'3.11'`).
* **Editable local package**: use `-e .` only for dev; avoid in production runs.

If you want, I can tailor a minimal `requirements.txt` + `constraints.txt` starter for your OpenSees docs.
