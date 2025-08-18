# Command-Line Arguments 
***Optional***

A more powerful version of non-interactive execution includes **additional arguments** at the end of the command -- **Advanced Non-Interactive Mode**. These can be read inside your script to customize behavior dynamically — perfect for parameter studies and automation. You pass arguments (like numbers, file names, or parameters) into your script from the command line.

## Use Cases

* Parameter studies
* High-throughput computing and job arrays
* Model calibration and uncertainty quantification

**NOTE:** In this mode, your script must include logic to read and parse the arguments.

* ## Examples – Sequential Execution

    | Language   | Command                                  |
    | ---------- | ---------------------------------------- |
    | Tcl        | `OpenSees inputfile.tcl 3 5 tabasFn.at2` |
    | OpenSeesPy | `python inputfile.py 3 5 tabasFn.at2`    |

* ## Examples – Parallel Execution

    | Language         | Command                                                    |
    | ---------------- | ---------------------------------------------------------- |
    | Tcl (MP)         | `mpiexec -np N OpenSeesMP inputfileMP.tcl 3 5 tabasFn.at2` |
    | Tcl (SP)         | `mpiexec -np N OpenSeesSP inputfileSP.tcl 3 5 tabasFn.at2` |
    | OpenSeesPy (MPI) | `mpiexec -np N python inputfile.py 3 5 tabasFn.at2`        |
  
    
    Inside your script, you can access these variables:
    
    * In Tcl: `$argv`, `[lindex $argv 0]`, etc.
    * In Python: `sys.argv[1]`, `sys.argv[2]`, etc.
    
    * **Use case:** This mode is essential for high-throughput studies where you want to rerun the same model with different inputs — like ground motions, geometry parameters, or material properties — without duplicating the script.



   
## *Parsing Arguments Inside Scripts*
    
| Language | Access Pattern              | Example            |
| -------- | --------------------------- | ------------------ |
| Tcl      | `$argv`, `[lindex $argv N]` | `[lindex $argv 0]` |
| Python   | `sys.argv`, `sys.argv[N+1]` | `sys.argv[1]`      |

* Note: In Python, `sys.argv[0]` is the script name. Arguments start at index 1.



