# Run OpenSees in CLI

Running an OpenSees at the command line allows you to test the program and make sure you have set up the right environment. This is ideal for:

* Testing syntax or exploring commands in real time
* Building a small model step-by-step
* Debugging specific lines of code without running an entire script


## Run OpenSees Interactively at the CLI

### OpenSees-Tcl


Start OpenSees-Tcl interactively by simply typing at the terminal:

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

<div id="slideShowTCL">
<script>
    addSlides("slideShowTCL","../_static/Interactive_Tcl/Slide","JPG",1,7)
</script>



### OpenSeesPy

Start python interactively by simply typing at the terminal:

       python
    

The command-line command will start an interactive session. 

    Python 3.10.6 | packaged by conda-forge | (main, Aug 22 2022, 20:35:26) [GCC 10.4.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 

You can now enter your commands at the prompt, one at a time, as shown below. You need to import OpenSeesPy before you can run OpenSees commands:

    >>> import openseespy.opensees as ops
    >>> ops.wipe()
    >>> ops.model('BasicBuilder','-ndm',2,'-ndf',3)
    >>> exit()
    Process 0 Terminating

<div id="slideShowPY">
<script>
    addSlides("slideShowPY","../_static/Interactive_Py/Slide","JPG",1,8)
</script>


    
## Run OpenSees Script at the CLI


Most OpenSees analyses are run in **non-interactive mode**, where you execute a full input script all at once. Even if you’re in an interactive environment like Jupyter, running a script this way means the entire sequence of commands executes without waiting for further input. Jupyter Hub has an integrated editor to make things easy.

You can run therefore, run either OpenSees(Tcl) and OpenSeesPy (Python) in non-interactive batch mode at the terminal's CLI by specifying the input script to execute. In both cases, the first argument provided after the executable is interpreted as the **main script file** to run.

Most OpenSees Analyses require that you work with an input script that you can edit as needed to fix errors and add features.
Being able to work with this script in an interactive environment allows to have immediate feedback on your changes.

This is your starting place. Develop your script for a few test cases.

The following images show how to run OpenSees Tcl and OpenSeesPy at the terminal for both sequential and parallel analyses.

<div id="slideShow">
<script>
    addSlides("slideShow","../_static/TerminalRun/Slide","JPG",4,13)
</script>



