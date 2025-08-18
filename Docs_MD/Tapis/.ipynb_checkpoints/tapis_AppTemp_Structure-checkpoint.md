# Structure of App Template
***Structure of a Tapis App Template***

All Tapis app templates follow a consistent folder structure that defines how the app behaves, how inputs and parameters are handled, and how jobs are launched. This structure makes it easy for platforms like DesignSafe to automate the submission and execution of scientific applications on remote systems.

A typical app template includes the following key components:

1. ## **app-definition.json**

    This is the core configuration file (or set of files). <br>
    It defines:
    
    * The name and version of the app
    * What execution and storage systems it uses
    * Which input files and parameters it expects
    * What resources it needs (e.g., processors, memory, queue)
    * How the results should be archived
    
    Tapis uses this file to register the app and validate any job submitted to it.

1. ## **Wrapper Script** (e.g., **app-wrapper.sh**)

    This is a shell script that runs the actual program. It:
    
    * Sets up the environment (e.g., loads modules)
    * Reads variables passed in as inputs and parameters
    * Constructs and runs the command line (e.g., `ibrun OpenSeesMP model.tcl`)
    * Organizes and prepares outputs for archiving
    
    Template variables like `${input1}` or `${param1}` are injected into this script at runtime based on the job request.

1. ## **README.md** or Documentation (Optional but Recommended)

    Includes notes for developers or admins about how to install, register, or troubleshoot the app. While not required, it helps ensure the app template is maintainable or adaptable by others.



This consistent structure allows app templates to be easily managed, reused, and shared. Whether you're submitting OpenSees jobs or running your own tools, all apps in the Tapis system follow this same general layout.

