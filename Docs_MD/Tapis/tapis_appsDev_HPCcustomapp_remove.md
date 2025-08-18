# Creating a Custom App on DesignSafe
THIS NEEDS TO BE TESTED!!!!


Writing your own app definition for DesignSafe lets you create reusable, shareable, web-based tools that run on TACC's supercomputers, but launch from DesignSafe's interface. 
Perfect for custom workflows, lab-specific tools, or research reproducibility.

This guide walks you through creating your own HPC-enabled application on **DesignSafe**, powered by **TACC** resources like Stampede3. 
You'll define a custom app with a graphical interface that runs your code via SLURM.

## Prerequisites

- A DesignSafe account: [https://www.designsafe-ci.org](https://www.designsafe-ci.org)
- Basic knowledge of shell scripting
- Your code (e.g., Python, MATLAB, or other scripts) ready to run
- Optional: Access to TACC CLI or DesignSafe CLI

## What's an App Definition in DesignSafe?
An app definition in DesignSafe is a JSON file that describes:
- What your app does (its name, inputs, and outputs)
- What compute resources it needs (nodes, time, cores)
- How it runs your code on TACC (via SLURM)
- What users see (forms, input fields, dropdowns, etc.)
- Once defined, you or others can launch the app from DesignSafe's GUI — and behind the scenes, it runs a SLURM job on TACC!

### How it Works (Big Picture)
Components:

Part | Description
App Definition JSON | Describes the interface and runtime configuration
Wrapper Script | Bash or Python script that executes your code
Executable/code | Your software or model to run (can be your own or a module like OpenSees)
Input/Output Mapping | Defines how users' input becomes command-line arguments or file references
Execution System | TACC resource like Stampede3 or Frontera
Deployment | App is uploaded and registered via Tapis API (formerly Agave)

## Step-by-Step: Creating a Custom App on DesignSafe

1. Create Your App Directory
Create a folder named my-app/ with the following files:
- wrapper.sh -- the SLURM wrapper script that runs your code
- my_code.py -- your actual code
- app-definition.json -- metadata that defines the app

2. Create the Wrapper Script (wrapper.sh)
Example contents of wrapper.sh:
```
#!/bin/bash
cd $WORK/$JOB_NAME

# Run your Python script with inputs from the GUI
python my_code.py "$input_param1" "$input_param2"
```
Make it executable:
```
chmod +x wrapper.sh
```

3. Write the App Definition (app-definition.json)
Example contents of app-definition.json:
```
{
  "id": "my-awesome-app-1.0",
  "name": "My Awesome App",
  "version": "1.0",
  "executionSystem": "designsafe.community.execution",
  "deploymentPath": "apps/my-awesome-app/1.0",
  "templatePath": "wrapper.sh",
  "parallelism": "SERIAL",
  "inputs": [
    {
      "id": "input_param1",
      "value": {
        "default": "default_value"
      }
    }
  ],
  "parameters": [
    {
      "id": "input_param2",
      "value": {
        "default": "5"
      }
    }
  ],
  "outputs": [
    {
      "id": "output_file",
      "value": {
        "default": "results.txt"
      }
    }
  ],
  "tags": ["custom", "python", "designsafe"]
}
```

4. Upload Files to TACC
Use SCP to upload your app folder to TACC:
```
scp -r my-app/ yourusername@login.designsafe-ci.org:/work/apps/my-awesome-app/1.0
```
Or upload via DesignSafe DataDepot and move files to:
```
/work/apps/my-awesome-app/1.0
```

5. Set Up and Authenticate the Tapis CLI
Install the Tapis CLI:
```
pip install tapis-cli-ng
```
Authenticate
```
tapis auth login
```
6. Register the App with Tapis
Register your app:
```
tapis apps create -F app-definition.json
```
Confirm it's registered:
```
tapis apps list | grep my-awesome-app
```

7. Launch the App from DesignSafe GUI
1. Go to Workspace → Tools & Applications → Private Apps
1. Select My Awesome App
1. Fill out the input fields from the form
1. Submit the job
1. Results will appear in your project data storage

## Tips and Tricks
- Use "parallelism": "PARALLEL" for MPI jobs
- Load TACC software modules inside wrapper.sh (e.g., module load matlab)
- Use $SCRATCH for temporary fast storage, $WORK for persistent storage
- Add "helpURI" to your JSON if you want to link to documentation or GitHub