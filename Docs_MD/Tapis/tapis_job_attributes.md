# Job Attributes
***Job Submission Attributes in Tapis***


<!-- Unlike traditional schedulers, Tapis provides a consistent interface for job submission, regardless of the underlying scheduler or system. Whether you're running on a supercomputer or a container-based environment, you interact with Tapis Jobs using the same structured request—either through a web form or a JSON POST to the Jobs API.<br>
Importantly, Tapis decouples application logic from system-level details. When you submit a job, you don’t need to understand how the scheduler works or what modules to load on the compute nodes. Instead, you focus on specifying inputs and parameters for a registered app, and Tapis handles the rest—resource provisioning, environment setup, execution, and archiving.<br>
To submit a job, you send a job request (in JSON or form format) that includes both required fields and optional attributes. At minimum, this includes the job name and the app ID. Additional job submission attributes control how the job is run and managed. -->

When submitting a job to Tapis, the job request JSON includes fields that describe how the job should be scheduled and executed on the compute system. These are called **job submission attributes**. They are interpreted by the Tapis platform—not the app itself—to control resource requests, queuing, archiving, and naming.<br>
These fields are distinct from application parameters and inputs. <br>
Job submission attributes are evaluated by the Tapis system and are not automatically passed into your application logic or wrapper scripts.





## Common Job Submission Attributes

The optional and required attributes common to all job submissions.

| Attribute           | Description                              | Notes                                            |  type   | ...more    |
| ------------------- | ---------------------------------------- | ------------------------------------------------ | --- |  --- |
| `name`              | A user-defined name for the job          | Required in every job submission                 | string | 	Descriptive name of the job. This will be slugified and used as one component of directory names in certain situations. |
| `appId`             | The ID of the application to run         | Must match a registered Tapis app                | string | 	The unique name of the application being run by this job. This must be a valid application that the calling user has permission to run. |
| `batchQueue`        | HPC queue to use (e.g., `skx`)           | Optional; may default based on app configuration | string | The batch queue on the execution system to which this job is submitted. Defaults to the app's defaultQueue property if specified. Otherwise a best-fit algorithm is used to match the job parameters to a queue on the execution system with sufficient capabilities to run the job. |
| `nodeCount`         | Number of nodes to request               | Optional; app-specific requirements may vary     | integer | 	The number of nodes to use when running this job. Defaults to the app's defaultNodes property or 1 if no default is specified. |
| `processorsPerNode` | Number of cores per node                 | Optional                                         | integer | The number of processors this application should utilize while running. Defaults to the app's defaultProcessorsPerNode property or 1 if no default is specified. If the application is not of executionType PARALLEL, this should be 1. |
| `memoryPerNode`     | Memory per node (e.g., `128GB`)          | Optional                                         | string | 	The maximum amount of memory needed per node for this application to run given in ####.#[E|P|T|G]B format. Defaults to the app's defaultMemoryPerNode property if it exists. GB are assumed if no magnitude is specified. |
| `maxRunTime`        | Wall time limit (e.g., `02:00:00`)       | Optional                                         | string | The estimated compute time needed for this application to complete given in hh:mm:ss format. This value must be less than or equal to the max run time of the queue to which this job is assigned. |
| `archive*`           | Whether to archive job outputs           | Default is usually `true`                        | boolean | Whether the output from this job should be archived. If true, all new files created by this application's execution will be archived to the archivePath in the user's default storage system. |
| `archiveSystem*`     | Storage system to archive results to     | Optional                                         | string | System to which the job output should be archived. Defaults to the user's default storage system if not specified. |
| `archivePath*`       | Path under the archive system            | Optional                                         | string | 	Location where the job output should be archived. A relative path or absolute path may be specified. If not specified, a unique folder will be created in the user's home directory of the archiveSystem at 'archive/jobs/job-$JOB_ID' |
| `notifications*`     | List of callback URLs or email addresses | Optional                                         | JSON array | An array of one or more JSON objects describing an event and url which the service will POST to when the given event occurs. For more on Notifications, see the section on webhooks below. |
| `tags**`              | User-defined job labels                  | Optional                                         | string | -- |
| `description**`       | Optional job-level description           | Optional                                         | string | -- |

In addition to the standard fields for all jobs, the application you specify in the appId field will also have its own set of inputs and parameters specified during registration that are unique to that app. (For more information about app registration and descriptions, see the Apps section.

*:  Optional fields are marked with an astericks.
**: These fields were not in Tapis documentation

https://tacc-cloud.readthedocs.io/projects/agave/en/latest/agave/guides/jobs/job-submission.html

## Resource-Related Attributes

The following fields directly control what resources are requested from the compute system:

* `nodeCount`
* `processorsPerNode`
* `memoryPerNode`
* `maxRunTime`

These fields map to scheduler directives (e.g., for SLURM) and ensure the correct execution environment is provisioned.

## Archiving and Notifications

These fields control what happens after the job completes.
These four fields relate to **result archiving and notifications**. You can often ignore them unless you need something specific.


| Field           | What it does   | When to use it                                                                               |
| --------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `notifications` | Webhooks or emails triggered by job events   |   When you want to trigger a webhook or receive email updates on job events                    |
| `archive`       | Set to `false` to skip archiving (not recommended)   |   Set to `false` only if you don’t want Tapis to copy job outputs to storage (not recommended) |
| `archiveSystem` | If you want to archive to a system other than the default   |   Use if you want to store results somewhere other than your default storage system            |
| `archivePath`   | Custom location under the archive system   |   Use to organize results by project, date, or custom folder path                              |



## Example Job Request

```json
{
  "name": "run-opensees",
  "appId": "opensees-mp-s3",
  "nodeCount": 2,
  "processorsPerNode": 48,
  "memoryPerNode": "192GB",
  "maxRunTime": "02:00:00",
  "archive": true,
  "inputs": {
    "inputScript": "agave://designsafe.storage/community/opensees/model.tcl"
  },
  "parameters": {
    "numProcessors": "96"
  }
}
```

In this example:

* Tapis provisions 2 Stampede3 nodes with 48 cores each and 192 GB per node.
* Job outputs are archived after completion.
* Input and parameter values are passed into the app logic (not part of job attributes).

## Summary

* **Job attributes** are essential for resource scheduling and job lifecycle control.
* They are distinct from app parameters and inputs.
* You must coordinate job attributes with application-level parameters when running parallel or performance-sensitive workloads.

