# Tapis App Inputs
***Inputs in a Tapis App Template***

**Inputs** are files or directories that a Tapis app needs in order to run. These could include simulation scripts, configuration files, models, datasets, or any other resources the application consumes at runtime.

Inputs are defined in the app’s `app-definition.json` file, and they are automatically **staged into the job’s working directory** before execution. This means users don’t need to move files manually or worry about where things go — Tapis handles that part for them.

## Key Properties of an Input

Each input is defined by an object in the `inputs` section of the app definition. Here are the most important fields:

| Field                  | Description                                                                                  |
| ---------------------- | -------------------------------------------------------------------------------------------- |
| `id`                   | A unique identifier used to refer to this input (e.g., `inputScript`, `modelFile`)           |
| `value.required`       | Whether this input must be provided when submitting a job                                    |
| `value.default`        | A default file path to use if the user doesn’t specify one                                   |
| `value.visible`        | Whether this input appears in the submission form or UI                                      |
| `semantics.fileTypes`  | A list of accepted file types (typically `"raw-0"` is used)                                  |
| `details.label`        | A human-readable label for the input                                                         |
| `details.description`  | A tooltip or description shown in the UI                                                     |
| `details.argument`     | (Optional) The command-line flag associated with this input                                  |
| `details.showArgument` | Whether to prepend the argument before the input value when inserted into the wrapper script |

## How Inputs Work at Runtime

When a job is submitted:

1. Tapis stages each input file into the job directory on the remote system.
2. The wrapper script uses placeholder variables like `${inputScript}` to reference them.
3. Tapis replaces these placeholders with the actual file paths from the job submission.

For example, if your input has an ID of `modelFile`, your wrapper might contain:

```bash
OpenSeesMP ${modelFile}
```

At runtime, `${modelFile}` will be replaced with the actual file path (e.g., `model01.tcl`), which was staged into the job directory.

## Important Notes

* You can have multiple inputs, each with its own validation rules or defaults.
* Inputs can be optional or required, and Tapis will enforce this during submission.
* Inputs can come from any Tapis storage system (e.g., `agave://`, `https://`, `sftp://`).

