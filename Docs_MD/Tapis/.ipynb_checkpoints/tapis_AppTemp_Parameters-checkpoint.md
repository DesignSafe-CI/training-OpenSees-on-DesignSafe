# Tapis App Parameters
***Parameters in a Tapis App Template***

While inputs provide files to your application, **parameters** are used to pass in configuration values—such as numbers, flags, or options—that control how the app behaves. Parameters are also defined in the app’s `app-definition.json` file and made available to the wrapper script just like inputs.

They’re commonly used to specify things like:

* The number of processors to use
* A Boolean switch (e.g., enable/disable a feature)
* A string or number (e.g., timestep size, output format)
* An enumerated option from a dropdown menu

## Key Properties of a Parameter

Each parameter is defined in the `parameters` array of the app definition. Common fields include:

| Field                  | Description                                                                              |
| ---------------------- | ---------------------------------------------------------------------------------------- |
| `id`                   | Unique identifier used to reference the parameter in the wrapper (e.g., `numProcessors`) |
| `value.required`       | Whether the user must provide a value                                                    |
| `value.type`           | The expected data type: `string`, `number`, `bool`, `enumeration`, or `flag`             |
| `value.default`        | Default value to use if the user doesn’t specify one                                     |
| `value.visible`        | Whether the parameter appears in the submission UI                                       |
| `value.validator`      | Optional regex to restrict allowed input values                                          |
| `details.label`        | Human-readable label shown in forms                                                      |
| `details.description`  | Help text for users in the UI                                                            |
| `details.argument`     | Command-line flag to prepend before the value (e.g., `-m`)                               |
| `details.showArgument` | Whether to show the argument when generating the run command                             |

## How Parameters Work at Runtime

Just like inputs, parameter values are injected into the wrapper script using `${paramId}` placeholders.

Example:

```bash
OpenSeesMP ${modelFile} -np ${numProcessors}
```

If a user specifies `numProcessors = 8`, the wrapper becomes:

```bash
OpenSeesMP model.tcl -np 8
```

## Parameter Types at a Glance

| Type          | Meaning                                                           |
| ------------- | ----------------------------------------------------------------- |
| `string`      | Any string value (e.g., `"concrete"`)                             |
| `number`      | Numeric value (e.g., `0.01`, `100`)                               |
| `bool`        | `true` or `false` (mapped to `1` or empty string)                 |
| `flag`        | A command-line flag that’s present or not (e.g., `--verbose`)     |
| `enumeration` | Dropdown menu of predefined values (e.g., `"fast"`, `"accurate"`) |
