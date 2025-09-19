# Run OpenSees Interactively at the CLI

## OpenSees-Tcl


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


## OpenSeesPy

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

