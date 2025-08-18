# OpenSees Tapis Apps

The [OpenSeesMP app template](https://github.com/TACC/WMA-Tapis-Templates/tree/main/applications/opensees-mp/opensees-mp-s3) provides a working example of how to wrap the parallel version of OpenSees into a Tapis App.

## Structure Overview

This template includes:

* **app-definition.json**: Describes the app’s metadata and links it to a system (like Frontera or Stampede3). It defines:

  * `deploymentSystem` and `executionSystem`
  * CLI-style `parameters` and `inputs`
  * Output handling rules

* **app-wrapper.sh**: The actual launch script. It:

  * Loads the OpenSees module (or uses a container)
  * Builds the MPI run command (e.g., `ibrun OpenSeesMP`)
  * Moves inputs and manages outputs

* `README.md`: Provides guidance on how to install the app using the Tapis CLI or API.

## Example Use Case

Let’s say you want to run a parametric analysis using OpenSeesMP on Stampede3. You can:

1. Register the app in your Tapis tenant using the provided `app-definition.json`.
2. Submit a job specifying:

   * The OpenSees `.tcl` input script
   * The number of processors (as a parameter)
3. Tapis will stage the files, launch the job using the `app-wrapper.sh`, and archive outputs to your designated storage system.

This allows researchers to submit repeatable OpenSeesMP runs through various interfaces—whether through the web, notebooks, or programmatic pipelines—without needing to manually SSH into a cluster or write job scripts from scratch.

