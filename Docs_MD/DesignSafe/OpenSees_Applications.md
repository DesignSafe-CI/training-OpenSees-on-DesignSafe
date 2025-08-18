## OpenSees Applications
**Which OpenSees to run on DesignSafe?**

There are three main applications, each with its own use case.
* #### Sequential Application:
  1. **OpenSees** is the simplest application:
     - Regular OpenSees  
       Single core and is easy to use.  
       It's your starting place and can easily meet most project needs.

* #### Parallel Applications:
  1. **OpenSeesSP** is the *Single Parallel Interpreter* application:
     - The single processor distributes a large model to the remaining processors for faster solution strategies.
     - This application allows you to run very large models with ease because it automates the model decomposition with no need for input from the user.
     - This application may not be available on OpenSeesPy

  2. **OpenSeesMP** is the *Multiple Parallel Interpreters* application:
     - It is the most versatile parallel application.
     - It runs all the processors in parallel, each executing the same script containing individual instructions for each processor.
     - This is the most powerful OpenSees application by giving the user full control of the job.
     - Two types of parallelization:
       1. Manual Model Decomposition (automated in OpenSeesSP).
       2. Distributed parametric analyses.
     - Improve efficiency with Load Balancing (inter-processor communication)

These applications are available in the TCL interpreter, as well as in the Python interpreter (OpenSeesPy). However, there are several ways to run OpenSeesPy in the parallel environment. <br>
Running OpenSeesSP in OpenSeesPy requires some verification since it is environment-dependent. This is beyond the scope of this traning content.

### Decision Matrix for OpenSees Applications


| Model Size     | Analysis Parameters | Sequential OpenSees          | Parallel OpenSeesSP                           | Parallel OpenSeesMP                             |
|----------------|---------------------|-------------------------------|------------------------------------------------|--------------------------------------------------|
| small–medium   | none–few            | ✅ Recommended                | 🚩 Element Robustness                      | ⏳ Extra time to set up the script             |
| small–medium   | many                | ⏳ Wait Time                   | 🚩 Element Robustness                      | ✅ Recommended                                    |
| medium–large   | none–few            | ⛔ Too Slow                   | ✅ Recommended                                  | ✅ Recommended + ⚠️ Manual Scripting              |
| medium–large   | many                | ⛔ Too Slow                   | 🚩 Element Robustness + ⛔ Too Slow             | ✅ Recommended + ⚠️ Manual Scripting              |
| very large     | none–few            | ⛔ Too Slow                   | ✅ Recommended                                  | ✅ Recommended + ⚠️ Manual Scripting              |
| very large     | many                | ⛔ Too Slow                   | ✅ Recommended 1 analysis/job                           | ✅ Recommended + ⚠️ Manual Scripting              |

Legend:
- ✅ Recommended solution  
- ⏳ Additional wait time due to HPC queue makes it a weak solution  
- 🚩 Requires ensuring element robustness in OpenSeesSP (weak solution)  
- ⚠️ Manual domain decomposition requires extra scripting effort  
- ⛔ Additional run time due to single-threaded execution makes it a bad solution  