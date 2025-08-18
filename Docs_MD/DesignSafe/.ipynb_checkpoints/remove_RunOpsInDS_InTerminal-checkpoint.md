<!-- # Run Script in Terminal

Most OpenSees analyses are run in **non-interactive mode**, where you execute a full input script all at once. Even if you’re in an interactive environment like Jupyter, running a script this way means the entire sequence of commands executes without waiting for further input. Jupyter Hub has an integrated editor to make things easy.

You can run therefore, run both OpenSees(Tcl) and OpenSeesPy (Python) in non-interactive, batch mode at the terminal's CLI by specifying the input script to execute. In both cases, the first argument provided after the executable is interpreted as the **main script file** to run.

Most OpenSees Analyses require that you work with an input script that you can edit as needed to fix errors and add features.
Being able to work with this script in an interactive environment allows to have immediate feedback on your changes.

This is your starting place. Develop your script for a few test cases.

The following images show how to run OpenSees Tcl and OpenSeesPy at the terminal for both sequential and parallel analyses.

<div id="slideShow">
<script>
    addSlides("slideShow","../../_static/TerminalRun/Slide","JPG",4,13)
</script>



## Example Files Used in this demo
You can find these files in Community Data:

### Tcl

```{dropdown}  Ex1a.Canti2D.Push.tcl
:icon: file-code
```{literalinclude} ../../Examples_OpenSees/BasicExamples/Ex1a.Canti2D.Push.tcl
:language: none
```
```{dropdown} Ex1a.Canti2D.Push.mp.tcl
:icon: file-code
```{literalinclude} ../../Examples_OpenSees/BasicExamples/Ex1a.Canti2D.Push.mp.tcl
:language: none
```
```{dropdown} Ex1a_many.Canti2D.Push.mp.tcl
:icon: file-code
```{literalinclude} ../../Examples_OpenSees/BasicExamples/Ex1a_many.Canti2D.Push.mp.tcl
:language: none
```

### OpenSeesPy


```{dropdown} Ex1a.Canti2D.Push.py
:icon: file-code
```{literalinclude} ../../Examples_OpenSees/BasicExamples/Ex1a.Canti2D.Push.py
:language: none
```
```{dropdown} Ex1a.Canti2D.Push.mpi.py
:icon: file-code
```{literalinclude} ../../Examples_OpenSees/BasicExamples/Ex1a.Canti2D.Push.mpi.py
:language: none
```
```{dropdown} Ex1a.Canti2D.Push.mpi4py.py
:icon: file-code
```{literalinclude} ../../Examples_OpenSees/BasicExamples/Ex1a.Canti2D.Push.mpi4py.py
:language: none
```
 -->