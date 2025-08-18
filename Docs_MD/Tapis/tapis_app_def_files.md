# App-Definition Files
***App Definition Files: app.json vs profile.json***

The OpenSees Tapis applications are configured using a small set of structured files instead of a single app.json. Two of the key configuration files are app.json and profile.json. <br>
While app.json contains most of the application's metadata and logic, profile.json is used specifically to define the environment modules required at runtime.

* ##  **app.json**

    This is the **primary Tapis application definition file**. It contains all the top-level metadata and job configuration used by the Tapis Jobs API, including:
    
    * The app ID, version ("latest"), and description
    * Runtime type and container image (`ZIP`, containerImage)
    * Execution system and directory paths (e.g., `${JobWorkingDir}`)
    * Job submission type and resource requirements (e.g., node count, cores per node, memory, wall time) 
    * Inputs and arguments required to run the application (input parameters and file requirements)
    * Archive and output settings
    * Tagging and user interface notes and options
    
    This file is used by Tapis to register the app and to describe how it should be executed on the target HPC system.
    Essentially, `app.json` tells Tapis **what this app is, how to run it, and what inputs/outputs to expect**.



* ##  **profile.json**

    This is a **modular execution profile**, used to specify what environment modules to load on the HPC system (Stampede3 in this case) before the application runs. <br>
    In the case of OpenSees, it ensures that both the opensees module and its dependency hdf5/1.14.4 are loaded on Stampede3. <br>
    The structure is:
    
    
    ```json
    {
        "name": "OpenSees_default",
        "description": "Modules to load for the default version of OpenSees",
        "moduleLoads": [
            {
                "modulesToLoad": [
                    "hdf5/1.14.4",
                    "opensees"
                ],
                "moduleLoadCommand": "module load"
            }
        ],
        "hiddenOptions": [
            "MEM"
        ]
    }
    ```
    
    This profile is referenced from `app.json` through the `--tapis-profile OpenSees_default` scheduler option, allowing Tapis to:
    
    * Load `opensees` and its dependencies (like `hdf5`) on the execution nodes
    * Cleanly abstract **environment setup from app logic**



## Why Separate Them?

Separating the environment definition into `profile.json` offers several advantages:

* **Reusability**: A single `profile.json` can be shared across many apps that need the same module environment.
* **Maintainability**: Module updates can be made without changing the core app definition. You can update environment modules (e.g., new version of OpenSees or HDF5) in one place without modifying the main app definition.
* **Cleaner Abstraction**: It keeps environment setup logic separate from application logic. It separates *what* the app does (`app.json`) from *how* the system prepares the environment (`profile.json`).

This separation is particularly helpful when managing multiple applications on the same HPC system, or when updating module versions independently of application functionality.




