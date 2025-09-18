# Terminal CLI

The **CLI (Command-Line Interface)** is a text-based way to interact with a computer program or operating system by typing commands into a **Terminal** or **Console** window, instead of using graphical elements like buttons and menus. 

A CLI/Terminal  allows you to:

- Type commands to run programs, manage files, or perform tasks  
- See text-based output in response to commands  
- Work more efficiently through automation, scripting, and precise control


Most advanced scientific tools, such as **OpenSees** or **python**, are designed to be run through a **command-line interface (CLI)**. This means you launch the application by typing a command into a terminal, which tells the operating system to start the program and process your input script.

## CLI in the Context of OpenSees

Suppose you want to run an OpenSees model:
- In a graphical interface, you'd click through menus to load and run the model  
- In a CLI, you'd type: `OpenSees model.tcl`

This command immediately runs the model file using OpenSees.

The CLI allows you to:

- Enter OpenSees commands one-by-one and **see immediate results**
- Debug models interactively by modifying and re-running commands  
- Run both Tcl and Python (OpenSeesPy) scripts directly from the terminal


## Why Use a the Terminal?

| Advantage     | Description                                                               |
|--------------|---------------------------------------------------------------------------|
| Speed         | Tasks can be completed quickly using short commands                       |
| Automation    | Enables scripting to automate repetitive processes                        |
| Control       | Provides more detailed access to program features and settings            |
| Remote Access | Allows access to remote servers via SSH or other terminals                |

## Accessing the Terminal
You can access the terminal through the **Jupyter interface.**

Becoming familiar with how to open and use a terminal is the first step to unlocking the full power of command-line tools like OpenSees on both local and remote systems.

Access the terminal through the **Jupyter interface** by clicking “New > Terminal” in the Jupyter file browser or clicking the Terminal icon in the Launcher.

<div id="slideShow">
<script>
    addSlides("slideShow","../_static/TerminalRun/Slide","JPG",1,4)
</script>



## Basic Linux Commands

:::{dropdown} Here are the basic commands you **may** need when navigating the CLI in a linux environment.

```
mkdir dirname          : make a new directory
cd dirname             : change directory
pwd                    : returns current directory
ls                     : list files 
cp origFile newFile    : copy a file
mv origFile newFile    : move a file
rm filename            : remove a file
wc –l directoryname    : how many files in a directory 
wc –l filename         : how many lines in a file 
```

**Tip:** In Jupyter Hub, you can do most file operations through the navigation pane, but knowing these commands is crucial for work on the HPC.
:::
## Summary

The Command-Line Interface (CLI) at the Terminal is a fast, powerful, and flexible way to use OpenSees and other scientific tools. It’s especially helpful in high-performance computing (HPC) environments where speed, automation, and control are essential.


