# Command Structure
***Command Structure & Execution Modes***

OpenSees (and OpenSeesPy via Python) is a **command-driven application** designed to run simulations by executing a series of modeling and analysis instructions. How you invoke OpenSees directly determines the mode of execution, and understanding this distinction is crucial for effective and scalable use of the software.

This section introduces the three primary execution modes and the structure of typical OpenSees commands. These concepts are foundational and apply regardless of the interface you're using—whether on a local machine, an HPC cluster, or inside DesignSafe's Jupyter environment. 

At a high level, an application command (whether Tcl or Python) has **three key components**:

1. **Executable File** – Specifies the program to run
2. **Input Script** *(optional)* – File containing modeling and analysis commands
3. **Command-Line Arguments** *(optional)* – External values passed into the script

These components correspond to three primary **execution modes**, which refer to to **how you run a simulation.** This affects everything from how variables are set to how results are saved.

* **Interactive Mode** – enter commands one at a time
* **Non-Interactive Mode** – execute a full script from top to bottom
* **Advanced Non-Interactive Mode** – run a script with external input variables

Each mode plays an important role in OpenSees workflows, from quick tests to full HPC-scale parameter studies.


1. ### Executable
    
    The first part of any command is the name of the executable file.
    
    Running it alone opens an interactive session — where the program gives you a prompt and waits for you to type individual commands. You then type commands one at a time and see immediate feedback before entering the next command. This is useful for testing commands, building small models incrementally, or debugging.
    
    **NOTE:** If the executable is not in your system’s PATH, you’ll need to specify its full file path (e.g., `/path/to/OpenSees`) when calling it from Python.
    
    
    | Application         | Command                           |  Prompt      |
    | ------------------- | --------------------------------- | ------------ |
    | OpenSees-Tcl        | OpenSees                          | OpenSees > |
    | OpenSeesPy (Python) | python*                           | <base > >>> |
    
    *(then import OpenSeesPy)
    
    Use this **Interactive Mode** to experiment with commands, build up models incrementally, or inspect objects.
    
    
    #### Use Cases
    
    * Learning or prototyping
    * Inspecting or debugging model elements
    * Quick testing of syntax or parameters
    
    #### Demo:
    :::{dropdown} OpenSees-Tcl Interactive
    
        
    1. **Command-line command**.<br> An interactive Tcl-interpreter session can be run only at the terminal.<br>Start OpenSees-Tcl interactively by simply typing at the terminal:
    
            OpenSees
    
        
    You’ll see a prompt like:
    
    
    
            OpenSees -- Open System For Earthquake Engineering Simulation
                    Pacific Earthquake Engineering Research Center
                            Version xx.xx.xx 64-Bit
    
        (c) Copyright 1999-20xx The Regents of the University of California
                                All Rights Reserved
        (Copyright and Disclaimer @ http://www.berkeley.edu/OpenSees/copyright.html)
    
    
        OpenSees > 
    
    
      
    You can now enter your commands at the prompt, one at a time, as shown below:
      
    
        OpenSees > wipe
        OpenSees > model BasicBuilder -ndm 2 -ndf 3
        OpenSees > exit
    
    
    
    :::
    
    :::{dropdown} OpenSeesPy Interactive
    
    1. **Command-line command**<br>
       An interactive python-interpreter session can be run only at the terminal.<br>Start OpenSees-Tcl interactively by simply typing at the terminal:
       
           python
        
    
    The command-line command will start an interactive session. Then import OpenSeesPy and run commands directly::
    
        Python 3.10.6 | packaged by conda-forge | (main, Aug 22 2022, 20:35:26) [GCC 10.4.0] on linux
        Type "help", "copyright", "credits" or "license" for more information.
        >>> import openseespy.opensees as ops
        >>> ops.wipe()
        >>> ops.model('BasicBuilder','-ndm',2,'-ndf',3)
        >>> exit()
        Process 0 Terminating
    
    2. **Jupyter Notebook**<br>
       You can also run OpenSeesPy interactive by importing it into your Jupyter notebook:
    
           import openseespy.opensees as ops
    
    
    :::
    


1. ### Script File 
    ***Optional***
    
    Adding a script file as a second argument switches to **Non-Interactive Mode**. The file is read from top to bottom and executed automatically — no user input required. This is the recommended and most used method of interacting with OpenSees.
    
    Even if you're using an interactive platform like Jupyter, if you run a full script at once, you're still in non-interactive mode. Jupyter Notebooks with OpenSeesPy commands used explicitly in the cells is a way to run OpenSeesPy interactively while still using an *input file* -- this is a great way to develop your input since you can integrate graphics.<br>
    **NOTE** This is the most common mode for batch jobs and large analyses.
    
    * #### Use Cases
    
      * Full model execution
      * Reproducible simulations
      * Running jobs on HPC or cloud environments
        
    * #### **Sequential Execution**
    
        | Language   | Command                                            |
        | ---------- | -------------------------------------------------- |
        | Tcl        | `OpenSees inputfile.tcl`                           |
        | OpenSeesPy | `python inputfile.py` *                            |
      
      **(import OpenSeesPy inside)*
    
        * Demo:
            
          :::{dropdown} OpenSees-Tcl
        
          1. Command-line command:
          
                 OpenSees Ex1a.tcl.Canti2D.Push.tcl
            
          2. Jupyter-Notebook cell:
            
                 import os
                 os.system('OpenSees Ex1a.tcl.Canti2D.Push.tcl')
                    
          You will see the following response. Note that the program exits once the analysis has been run:
          
                    
                     OpenSees -- Open System For Earthquake Engineering Simulation
                             Pacific Earthquake Engineering Research Center
                                    Version 3.7.1 64-Bit
            
                  (c) Copyright 1999-2016 The Regents of the University of California
                                          All Rights Reserved
              (Copyright and Disclaimer @ http://www.berkeley.edu/OpenSees/copyright.html)
            
            
                Analysis-0 execution done
                Analysis-1 execution done
                Analysis-2 execution done
                Analysis-3 execution done
                Analysis-4 execution done
                Analysis-5 execution done
                Analysis-6 execution done
                Analysis-7 execution done
                ALL DONE!!!
          :::
        
          :::{dropdown} OpenSeesPy Input Script
            
          1. Command-line command:
        
                 python Ex1a.py.Canti2D.Push.py
          
          2. Jupyter-Notebook cell:
            
                 import os
                 os.system('python Ex1a.py.Canti2D.Push.py')
                    
          You will see the following response. Note that the program exits once the analysis has been run:
            
                Analysis-0 execution done
                Analysis-1 execution done
                Analysis-2 execution done
                Analysis-3 execution done
                Analysis-4 execution done
                Analysis-5 execution done
                Analysis-6 execution done
                Analysis-7 execution done
                ALL DONE!!!
                (base) jovyan@3cd0f33abec1:~/work$
            
          :::
         
            
        
    * ####  **Parallel Execution (N cores)**
    
        Use `mpiexec` or `mpirun` to launch distributed memory jobs:
        
        | Language         | Command                                                                   |
        | ---------------- | ------------------------------------------------------------------------- |
        | Tcl (MP)         | `mpiexec -np N OpenSeesMP inputfileMP.tcl`                                |
        | Tcl (SP)         | `mpiexec -np N OpenSeesSP inputfileSP.tcl`                                |
        | OpenSeesPy (MPI) | `mpiexec -np N python inputfile.py` *                                     |
      
      **(import OpenSeesPy inside. And script must use mpi4py or similar)*
      * N is the number of concurrent processors
    
      * Demo:
      
          :::{dropdown} OpenSeesMP 
    
          1. Command-line command:
      
                 mpiexec -np 3 OpenSeesMP simpleMP.tcl
        
          2. Jupyter-Notebook cell:
        
                 import os
                 os.system('mpiexec -np 3 OpenSeesMP simpleMP.tcl')
          
                
          You will see the following response. Note that the program exits once the analysis has been run:
      
                        OpenSees -- Open System For Earthquake Engineering Simulation
                                Pacific Earthquake Engineering Research Center
                                        Version 3.5.1 64-Bit
                
                    (c) Copyright 1999-2016 The Regents of the University of California
                                            All Rights Reserved
                (Copyright and Disclaimer @ http://www.berkeley.edu/OpenSees/copyright.html)
                
                
                pid 1 of 3
                pid 0 of 3
                pid 2 of 3
                tclLibUnits.tcl
                tclLibUnits.tcl
                tclLibUnits.tcl
                pid 0 source Ex4.Portal2D.build.InelasticSection.scr.tcl
                pid 0 source Ex4.Portal2D.analyze.Dynamic.EQ.Uniform.scr.tcl
                pid 1 source Ex4.Portal2D.build.InelasticSection.scr.tcl
                pid 1 source Ex4.Portal2D.analyze.Dynamic.EQ.Uniform.scr.tcl
                pid 2 source Ex4.Portal2D.build.InelasticSection.scr.tcl
                
                .....
                
                pid 0 inFiles: ./GMfiles/RSN31_PARKF_C08050.at2
                pid 0 file read
                pid 0 OpenSeesMP
                pid 0 count 4 check 1 goRun 0
                pid 0 done infile: ./GMfiles/RSN31_PARKF_C08050.at2
                pid 0 ALL DONE!!!
                Process Terminating 0
                (base) jovyan@3cd0f33abec1:~/work$ 
          :::
      
          :::{dropdown} OpenSeesPy Parallel
    
          1. Command-line command:
      
                 mpiexec -np 3 python simpleMP.py
        
          2. Jupyter-Notebook cell:
        
                 import os
                 os.system('mpiexec -np 3 python simpleMP.py')
                 
          You will see the following response. Note that the program exits once the analysis has been run:
          
                pid 0 of 3
                pid 2 of 3
                pid 1 of 3
                pyLibUnits.tcl.py
                pyLibUnits.tcl.py
                pid 2 sourced pyLibUnits.tcl.py
                pyLibUnits.tcl.py
                ....
                pid 0 inFiles: ./GMfiles/RSN122_FRIULI.A_A-COD000.at2
                pid 0 file read
                pid 0 OpenSeesMP
                pid 0 count 2 check 2 goRun 0
                pid 0 ALL DONE!!!
                Process 0 Terminating
                Process 0 Terminating
                Process 0 Terminating
                (base) jovyan@3cd0f33abec1:~/work$ 
          :::



1. ### Command-Line Arguments 
    ***Optional***
    
    A more powerful version of non-interactive execution includes **additional arguments** at the end of the command -- **Advanced Non-Interactive Mode**. These can be read inside your script to customize behavior dynamically — perfect for parameter studies and automation. You pass arguments (like numbers, file names, or parameters) into your script from the command line.
    
    * **Use Cases**:
    
      * Parameter studies
      * High-throughput computing and job arrays
      * Model calibration and uncertainty quantification
    
    * **NOTE:** In this mode, your script must include logic to read and parse the arguments.
    
    * #### **Examples – Sequential Execution**
    
        | Language   | Command                                  |
        | ---------- | ---------------------------------------- |
        | Tcl        | `OpenSees inputfile.tcl 3 5 tabasFn.at2` |
        | OpenSeesPy | `python inputfile.py 3 5 tabasFn.at2`    |
    
    * ##### **Examples – Parallel Execution**
    
        | Language         | Command                                                    |
        | ---------------- | ---------------------------------------------------------- |
        | Tcl (MP)         | `mpiexec -np N OpenSeesMP inputfileMP.tcl 3 5 tabasFn.at2` |
        | Tcl (SP)         | `mpiexec -np N OpenSeesSP inputfileSP.tcl 3 5 tabasFn.at2` |
        | OpenSeesPy (MPI) | `mpiexec -np N python inputfile.py 3 5 tabasFn.at2`        |
      
        
        Inside your script, you can access these variables:
        
        * In Tcl: `$argv`, `[lindex $argv 0]`, etc.
        * In Python: `sys.argv[1]`, `sys.argv[2]`, etc.
        
        * **Use case:** This mode is essential for high-throughput studies where you want to rerun the same model with different inputs — like ground motions, geometry parameters, or material properties — without duplicating the script.
    
    
    
       
    * #### **Parsing Arguments Inside Scripts**
        
        | Language | Access Pattern              | Example            |
        | -------- | --------------------------- | ------------------ |
        | Tcl      | `$argv`, `[lindex $argv N]` | `[lindex $argv 0]` |
        | Python   | `sys.argv`, `sys.argv[N+1]` | `sys.argv[1]`      |
        
        * Note: In Python, `sys.argv[0]` is the script name. Arguments start at index 1.
        
    



## Summary of Execution Modes

| Mode                         | How to Invoke                                              | When to Use                                 |
| ---------------------------- | ---------------------------------------------------------- | ------------------------------------------- |
| **Interactive**              | Just run the executable (e.g., `OpenSees` or `python`)     | For quick tests, model inspection, learning |
| **Non-Interactive**          | Add input file (e.g., `OpenSees model.tcl`)                | For full analyses or reproducible scripts   |
| **Advanced Non-Interactive** | Add command-line args (e.g., `OpenSees model.tcl 1.0 2.0`) | For automation, sweeps, HPC workflows       |



### Why This Matters

Each execution style supports a different stage of the modeling process:

* Interactive mode is great for **trial-and-error and exploration**.
* Non-interactive mode is essential for **repeatable workflows**.
* Advanced argument passing enables **automation and scalability**.

Understanding and switching between these modes is key to moving from small, test cases to full-scale HPC simulations.

