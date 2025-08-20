# Inputs vs Parameters
***What’s the Difference Between Inputs and Parameters?***

**Inputs** and **parameters** are both values you provide when submitting a Tapis job, but they serve different purposes and are treated differently behind the scenes.

| Feature                | **Inputs**                                                     | **Parameters**                                             |
| ---------------------- | -------------------------------------------------------------- | ---------------------------------------------------------- |
| **What they are**      | Files or folders your app needs                                | Configuration values or settings                              |
| **Examples**           | CSV file, input script, ground motion file, mesh geometry | Number of processors, damping ratio, verbosity flag                |
| **Data type**          | Paths to data files                                            | Strings, numbers, booleans, flags, or enumerated choices      |
| **Staged?**            | Yes — copied (*staged*) into the job directory before run      | No — used as plain values injected into the wrapper script    |
| **In wrapper**         | Referenced as `${inputScript}`, `${motionFile}` (`${inputId}`) | Referenced as `${numProcessors}`, `${damping}` (`${paramId}`) |
| **Command-line usage** | Becomes a file path (`OpenSees ${inputScript}`)                | Becomes part of a command line option (`-damp ${damping}`)    |

* ### Use an **input** when:

    * You need to provide a file to the app
    * The file should be staged into the job’s working directory

* ### Use a **parameter** when:

    * You need to pass in a value (like a number, switch, or keyword)
    * You want to control the app’s behavior without modifying the input data

**In short:**

* Inputs are *things* (files)
* Parameters are *instructions* (how to run the app)
Certainly! Here's the same section, now enriched with **OpenSees-specific examples** to make the distinction between inputs and parameters concrete for your readers:



:::{dropdown} **OpenSees Input Example**

```json
{
  "id": "inputScript",
  "value": {
    "required": true
  },
  "details": {
    "label": "OpenSees TCL Script",
    "description": "The main .tcl file containing the OpenSees model definition"
  }
}
```

This tells Tapis to expect a `.tcl` file as input, which will be staged into the job directory. The wrapper might include:

```bash
OpenSeesMP ${inputScript}
```
:::

---

:::{dropdown} **OpenSees Parameter Example**

```json
{
  "id": "numProcessors",
  "value": {
    "type": "number",
    "required": true,
    "default": "4"
  },
  "details": {
    "label": "Number of MPI Processes",
    "argument": "-np",
    "showArgument": true
  }
}
```

This provides a runtime setting (e.g., `-np 4`) that is substituted into the wrapper script:

```bash
ibrun -np ${numProcessors} OpenSeesMP ${inputScript}
```
:::


## Summary

* **Use an input** to provide data files like `.tcl`, `.json`, `.txt`, or `.mat`.
* **Use a parameter** to control how the model runs — such as the number of processors, damping ratios, or output flags.

This pattern makes Tapis apps flexible and adaptable to many different model configurations without needing to rewrite code.
