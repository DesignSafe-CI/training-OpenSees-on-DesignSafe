## Using Public Apps vs. Writing Your Own

### Use an existing (public) app

Public apps on DesignSafe are vetted templates for common tools (e.g., OpenSees, OpenFOAM). They’re the fastest path to results.

**Where to find them**

* **Web Portal → Tools & Applications**: browse/search, read the app’s help page.
* In notebooks/CLI: identify the app’s ***appId*** (and optional version) from the portal, then submit jobs programmatically.

**How to run effectively**

* Review the app’s **inputs** and **parameters** (defined by the app schema).
* Start with a **small test case**; use defaults for resources (you can tune later).
* Prefer **stable** or **latest** versions noted in the catalog.
* Keep your inputs on a Tapis-visible system (e.g., **MyData**, **Work**).

**When public apps are ideal**

* Your workflow matches the app’s interface.
* You want a **supported**, **reproducible** environment with minimal setup.
* You don’t need custom launch logic or nonstandard dependencies.

---

### Write your own app

Create a Tapis app when you need custom behavior, a different software version, or a specialized interface for your lab/project.

**Building blocks**

1. **Wrapper** (e.g., *tapisjob_app.sh*): non-interactive, writes outputs to *$PWD*, handles launch (*ibrun*/*mpirun*/*srun*) and logging.
2. ***app.json* (required)**: ID, version, execution system, execution type (*HPC*), job type (*MPI*/*SERIAL*), defaults (nodes, ppn, walltime), **inputs** and **parameters**.
3. ***profile.json* (optional)**: modules and env vars (or rely on containers).
4. **Test dataset**: a tiny, shareable case for validation.

**Registration & sharing**

* Register the app (via portal form or API), then **share** with your project/team.
* For broader visibility in the portal catalog, follow DesignSafe’s publication/review process.

**Best practices**

* **Version** every change (e.g., *1.2.0*), keep a changelog, don’t break existing users.
* Avoid hard-coded paths; use **Tapis URIs** and app parameters.
* Set **sensible defaults** (resources, inputs) and document them.
* Keep profiles minimal; prefer containers or a small *modules* list for stability.
* Provide **clear labels/descriptions** for inputs/parameters so users don’t guess.

**When custom apps shine**

* You need a new executable/version, custom pre/post steps, or a lab-specific interface.
* You’re automating **parameter sweeps**, ensembles, or multi-stage workflows.
* You want your group’s **reproducible** template others can reuse.

---

### Quick chooser

| Need                                    | Use a public app | Write your own |
| --------------------------------------- | ---------------- | -------------- |
| Fast start with a standard tool         | ✅                |                |
| Custom binaries, flags, or launch logic |                  | ✅              |
| Team-specific interface & defaults      |                  | ✅              |
| Minimal maintenance                     | ✅                |                |
| Full control / special dependencies     |                  | ✅              |

> In the next sections you can dive into: finding *appId*s, reading an app’s input/parameter schema, authoring *app.json*/*profile.json*, and testing/iterating your own apps.
