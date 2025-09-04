# Table of Contents

## 
- [Oview_TrainingObjectives](Docs_MD/Oview_TrainingObjectives.md)

## Overview
- [DesignSafe & TACC](Docs_MD/Oview_DesignSafeOnTACC.md)
  - [Workflow Architecture](Docs_MD/Oview_WorkflowArchitecture.md)
  - [Workflow Decision Guide](Docs_MD/Oview_WorkflowArchitectureGuide.md)
- [OpenSees on DesignSafe](Docs_MD/OpenSees_AndDesignSafe.md)
  - [OpenSees-Tcl & OpenSeesPy](Docs_MD/OpenSees_Interpreters.md)
  - [OpenSees_Applications](Docs_MD/OpenSees_Applications.md)
  - [Interpreters & Workflows](Docs_MD/OpenSees_Workflows.md)
  - [Decision Matrix](Docs_MD/OpenSees_DecisionMatrixOpsDS.md)
  - [Command Structure](Docs_MD/Ops_CommandStrux.md)
    - [Executable File (Interactive)](Docs_MD/Ops_CommandStrux_1_ExecutableFile.md)
    - [Input Script File (Non-Interactive)](Docs_MD/Ops_CommandStrux_2_ScriptFile.md)
    - [Command-Line Arguments](Docs_MD/Ops_CommandStrux_3_CommandLineArgs.md)
  - [Parallel Execution](Docs_MD/Ops_ParallelExec.md)
    - [Parallel Execution: MPI](Docs_MD/Ops_ParallelExec_MPI.md)
    - [Parallel Execution: ibrun](Docs_MD/Ops_ParallelExec_Ibrun.md)
    - [OpenSeesPy Parallel](Docs_MD/Ops_ParallelExec_python.md)
  - [Execution Guide](Docs_MD/Ops_ExecGuide.md)
- [Compute Environments](Docs_MD/ComputeEnvironments.md)
  - [HPC Hardware](Docs_MD/HPC_Intro.md)
    - [Nodes](Docs_MD/HPC_Node.md)
    - [Stampede3 Nodes](Docs_MD/HPC_NodeStampede3.md)
    - [Cores](Docs_MD/HPC_Core.md)
    - [Queues](Docs_MD/HPC_Queue.md)
    - [Stampede3 Queues](Docs_MD/HPC_QueueStampede3.md)
    - [Queue Selection](Docs_MD/HPC_QueueSelexn.md)
    - [Allocations](Docs_MD/HPC_allocations.md)
    - [Accessing HPC](Docs_MD/HPCenv_Access.md)
    - [DesignSafe's HPC Jupyter Lab](Docs_MD/HPCenv_HPCjupyter.md)
  - [TACC SLURM Jobs](Docs_MD/SLURM_TACCjobs.md)
    - [SLURM](Docs_MD/SLURM_Intro.md)
    - [SLURM_Workflow](Docs_MD/SLURM_Workflow.md)
    - [Job Scheduling](Docs_MD/SLURM_Scheduling.md)
    - [Job Input](Docs_MD/SLURM_Input.md)
    - [Job Script](Docs_MD/SLURM_Script.md)
    - [Run a SLURM Job](Docs_MD/SLURM_Run.md)
    - [SLURM Job Output](Docs_MD/SLURM_OutErrFiles.md)
    - [Parameter Sweeps](Docs_MD/SLURMmanual_ParameterSweep.md)
      - [Write SLURM with Python](Docs_MD/SLURMmanual_PythonFunction.md)
      - [Advanced Python Function](Docs_MD/SLURMmanual_PythonFunction2.md)
- [File Storage](Docs_MD/FileStorage_a_Concepts.md)
  - [Practical Usage](Docs_MD/FileStorage_b_PracticalUsage.md)
  - [Reference Tools](Docs_MD/FileStorage_c_ReferenceTools.md)
  - [On Corral](Docs_MD/FileStorage_1_corral.md)
  - [On Compute System](Docs_MD/FileStorage_2_compsys.md)
  - [On Compute Nodes](Docs_MD/FileStorage_3_compnode.md)
  - [Compare Storage Options](Docs_MD/FileStorage_4_compare.md)
  - [Understanding Paths](Docs_MD/Paths_Overview.md)
  - [Storage-System Paths](Jupyter_Notebooks/paths_StorageSystems.ipynb)
      <sub>📂 <a href='https://jupyter.designsafe-ci.org/hub/user-redirect/notebooks/CommunityData/OpenSees/TrainingMaterial/training-OpenSees-on-DesignSafe/Jupyter_Notebooks/paths_StorageSystems.ipynb' target='_blank'>Open in JupyterHub</a></sub>

## JupyterHub
- [JupyterHub Environment](Docs_MD/JupyterHub_Intro.md)
  - [Accessing JupyterHub](Docs_MD/AccessJupyter.md)
  - [Workflow in JupyterHub](Docs_MD/JupyterHub_Workflow.md)
- [JupyterHub Tools](Docs_MD/JupyterHub_Tools.md)
- [Paths in Python](Jupyter_Notebooks/paths_InPython.ipynb)
      <sub>📂 <a href='https://jupyter.designsafe-ci.org/hub/user-redirect/notebooks/CommunityData/OpenSees/TrainingMaterial/training-OpenSees-on-DesignSafe/Jupyter_Notebooks/paths_InPython.ipynb' target='_blank'>Open in JupyterHub</a></sub>
  - [Absolute vs Relative Path](Jupyter_Notebooks/paths_InPython_AbsVsRelative.ipynb)
      <sub>📂 <a href='https://jupyter.designsafe-ci.org/hub/user-redirect/notebooks/CommunityData/OpenSees/TrainingMaterial/training-OpenSees-on-DesignSafe/Jupyter_Notebooks/paths_InPython_AbsVsRelative.ipynb' target='_blank'>Open in JupyterHub</a></sub>
  - [Root & Home Paths](Jupyter_Notebooks/paths_InPython_RootAndHome.ipynb)
      <sub>📂 <a href='https://jupyter.designsafe-ci.org/hub/user-redirect/notebooks/CommunityData/OpenSees/TrainingMaterial/training-OpenSees-on-DesignSafe/Jupyter_Notebooks/paths_InPython_RootAndHome.ipynb' target='_blank'>Open in JupyterHub</a></sub>
  - [Managing Paths](Jupyter_Notebooks/paths_InPython_Manage.ipynb)
      <sub>📂 <a href='https://jupyter.designsafe-ci.org/hub/user-redirect/notebooks/CommunityData/OpenSees/TrainingMaterial/training-OpenSees-on-DesignSafe/Jupyter_Notebooks/paths_InPython_Manage.ipynb' target='_blank'>Open in JupyterHub</a></sub>
  - [Directory Contents](Jupyter_Notebooks/paths_InPython_Contents.ipynb)
      <sub>📂 <a href='https://jupyter.designsafe-ci.org/hub/user-redirect/notebooks/CommunityData/OpenSees/TrainingMaterial/training-OpenSees-on-DesignSafe/Jupyter_Notebooks/paths_InPython_Contents.ipynb' target='_blank'>Open in JupyterHub</a></sub>
  - [Building Paths](Jupyter_Notebooks/paths_InPython_BuildPath.ipynb)
      <sub>📂 <a href='https://jupyter.designsafe-ci.org/hub/user-redirect/notebooks/CommunityData/OpenSees/TrainingMaterial/training-OpenSees-on-DesignSafe/Jupyter_Notebooks/paths_InPython_BuildPath.ipynb' target='_blank'>Open in JupyterHub</a></sub>

## OpenSees in the Web Portal
- [DesignSafe Web Portal](Docs_MD/WebPortal_Overview.md)
- [Web-Portal Demo](Docs_MD/WebPortal_Overview_Workflow.md)
  - [1 Create Input](Docs_MD/WebPortal_1_CreateInput.md)
  - [2 Submit OpenSees-Express](Docs_MD/WebPortal_2_SubmitJob_OpenSeesExpress.md)
  - [2 Submit OpenSeesMP](Docs_MD/WebPortal_2_SubmitJob_OpenSeesMP.md)
  - [3 Monitor OpenSees-Express](Docs_MD/WebPortal_3_MonitorJob_OpenSeesExpress.md)
  - [3 Monitor OpenSeesMP](Docs_MD/WebPortal_3_MonitorJob_OpenSeesMP.md)
  - [4 PostProcess Ops-Express](Jupyter_Notebooks/webPortal_4_PostProcess_OpenSeesExpress.ipynb)
      <sub>📂 <a href='https://jupyter.designsafe-ci.org/hub/user-redirect/notebooks/CommunityData/OpenSees/TrainingMaterial/training-OpenSees-on-DesignSafe/Jupyter_Notebooks/webPortal_4_PostProcess_OpenSeesExpress.ipynb' target='_blank'>Open in JupyterHub</a></sub>
  - [4 PostProcess Ops-MP](Jupyter_Notebooks/webPortal_4_PostProcess_OpenSeesMP.ipynb)
      <sub>📂 <a href='https://jupyter.designsafe-ci.org/hub/user-redirect/notebooks/CommunityData/OpenSees/TrainingMaterial/training-OpenSees-on-DesignSafe/Jupyter_Notebooks/webPortal_4_PostProcess_OpenSeesMP.ipynb' target='_blank'>Open in JupyterHub</a></sub>

## OpenSees on JupyterHub
- [JupyterHub for OpenSees](Docs_MD/RunOpsInDS_JupyterHub_intro.md)
  - [Terminal CLI](Docs_MD/CLI.md)
  - [Python Console](Docs_MD/RunOpsInDS_Console.md)
- [Jupyter Notebooks](Docs_MD/RunOpsInDS_JupyterNotebook.md)
  - [OpenSeesPy Interactive](Jupyter_Notebooks/runOps_Ex1a.py.Canti2D.Push.ipynb)
      <sub>📂 <a href='https://jupyter.designsafe-ci.org/hub/user-redirect/notebooks/CommunityData/OpenSees/TrainingMaterial/training-OpenSees-on-DesignSafe/Jupyter_Notebooks/runOps_Ex1a.py.Canti2D.Push.ipynb' target='_blank'>Open in JupyterHub</a></sub>
  - [Run ANY OpenSees in Python](Jupyter_Notebooks/runOps_RunAnyOpenSeesInPython.ipynb)
      <sub>📂 <a href='https://jupyter.designsafe-ci.org/hub/user-redirect/notebooks/CommunityData/OpenSees/TrainingMaterial/training-OpenSees-on-DesignSafe/Jupyter_Notebooks/runOps_RunAnyOpenSeesInPython.ipynb' target='_blank'>Open in JupyterHub</a></sub>
  - [Python Script within Notebook](Docs_MD/RunOpsInDS_PythonWithinPython.md)

## Tapis
- [What is Tapis?](Docs_MD/tapis_intro.md)
  - [Interfacing with Tapis](Docs_MD/tapis_interfacing.md)
  - [Tapis Paths](Jupyter_Notebooks/paths_Tapis.ipynb)
      <sub>📂 <a href='https://jupyter.designsafe-ci.org/hub/user-redirect/notebooks/CommunityData/OpenSees/TrainingMaterial/training-OpenSees-on-DesignSafe/Jupyter_Notebooks/paths_Tapis.ipynb' target='_blank'>Open in JupyterHub</a></sub>
  - [System Specifications](Jupyter_Notebooks/tapisConnect_getSystemSpecs.ipynb)
      <sub>📂 <a href='https://jupyter.designsafe-ci.org/hub/user-redirect/notebooks/CommunityData/OpenSees/TrainingMaterial/training-OpenSees-on-DesignSafe/Jupyter_Notebooks/tapisConnect_getSystemSpecs.ipynb' target='_blank'>Open in JupyterHub</a></sub>
- [Tapis Authentication](Jupyter_Notebooks/tapisConnect_connectToTapis.ipynb)
      <sub>📂 <a href='https://jupyter.designsafe-ci.org/hub/user-redirect/notebooks/CommunityData/OpenSees/TrainingMaterial/training-OpenSees-on-DesignSafe/Jupyter_Notebooks/tapisConnect_connectToTapis.ipynb' target='_blank'>Open in JupyterHub</a></sub>
  - [Establish TMS Credentials](Jupyter_Notebooks/tapisConnect_establishSystemCredentials.ipynb)
      <sub>📂 <a href='https://jupyter.designsafe-ci.org/hub/user-redirect/notebooks/CommunityData/OpenSees/TrainingMaterial/training-OpenSees-on-DesignSafe/Jupyter_Notebooks/tapisConnect_establishSystemCredentials.ipynb' target='_blank'>Open in JupyterHub</a></sub>
- [Tapis Jobs](Docs_MD/tapis_jobs.md)
  - [Query and Retrieve Jobs](Docs_MD/tapis_queryJobs.md)
    - [Step 1: Explore All Jobs](Jupyter_Notebooks/tapis_queryJobs_ExploreAllJobs.ipynb)
      <sub>📂 <a href='https://jupyter.designsafe-ci.org/hub/user-redirect/notebooks/CommunityData/OpenSees/TrainingMaterial/training-OpenSees-on-DesignSafe/Jupyter_Notebooks/tapis_queryJobs_ExploreAllJobs.ipynb' target='_blank'>Open in JupyterHub</a></sub>
    - [Step 2: Inspect Job](Jupyter_Notebooks/tapis_queryJobs_InspectJob.ipynb)
      <sub>📂 <a href='https://jupyter.designsafe-ci.org/hub/user-redirect/notebooks/CommunityData/OpenSees/TrainingMaterial/training-OpenSees-on-DesignSafe/Jupyter_Notebooks/tapis_queryJobs_InspectJob.ipynb' target='_blank'>Open in JupyterHub</a></sub>
    - [Step 3: Retrieve Output](Jupyter_Notebooks/tapis_queryJobs_RetrieveOutput.ipynb)
      <sub>📂 <a href='https://jupyter.designsafe-ci.org/hub/user-redirect/notebooks/CommunityData/OpenSees/TrainingMaterial/training-OpenSees-on-DesignSafe/Jupyter_Notebooks/tapis_queryJobs_RetrieveOutput.ipynb' target='_blank'>Open in JupyterHub</a></sub>
  - [Explore All Jobs](Jupyter_Notebooks/tapis_getJobList_AllJobs.ipynb)
      <sub>📂 <a href='https://jupyter.designsafe-ci.org/hub/user-redirect/notebooks/CommunityData/OpenSees/TrainingMaterial/training-OpenSees-on-DesignSafe/Jupyter_Notebooks/tapis_getJobList_AllJobs.ipynb' target='_blank'>Open in JupyterHub</a></sub>
  - [Filter Tapis Jobs](Jupyter_Notebooks/tapis_getJobList_FilterJobs.ipynb)
      <sub>📂 <a href='https://jupyter.designsafe-ci.org/hub/user-redirect/notebooks/CommunityData/OpenSees/TrainingMaterial/training-OpenSees-on-DesignSafe/Jupyter_Notebooks/tapis_getJobList_FilterJobs.ipynb' target='_blank'>Open in JupyterHub</a></sub>
  - [Job Status](Jupyter_Notebooks/tapis_getJobMeta_JobStatus.ipynb)
      <sub>📂 <a href='https://jupyter.designsafe-ci.org/hub/user-redirect/notebooks/CommunityData/OpenSees/TrainingMaterial/training-OpenSees-on-DesignSafe/Jupyter_Notebooks/tapis_getJobMeta_JobStatus.ipynb' target='_blank'>Open in JupyterHub</a></sub>
  - [Job Metadata](Jupyter_Notebooks/tapis_getJobMeta_JobMetaData.ipynb)
      <sub>📂 <a href='https://jupyter.designsafe-ci.org/hub/user-redirect/notebooks/CommunityData/OpenSees/TrainingMaterial/training-OpenSees-on-DesignSafe/Jupyter_Notebooks/tapis_getJobMeta_JobMetaData.ipynb' target='_blank'>Open in JupyterHub</a></sub>
  - [Job History](Jupyter_Notebooks/tapis_getJobMeta_JobHistoryData.ipynb)
      <sub>📂 <a href='https://jupyter.designsafe-ci.org/hub/user-redirect/notebooks/CommunityData/OpenSees/TrainingMaterial/training-OpenSees-on-DesignSafe/Jupyter_Notebooks/tapis_getJobMeta_JobHistoryData.ipynb' target='_blank'>Open in JupyterHub</a></sub>
  - [Job Profiling](Docs_MD/tapis_job_profiling.md)
  - [Access Output Data](Jupyter_Notebooks/tapis_getJobOutData_AccessData.ipynb)
      <sub>📂 <a href='https://jupyter.designsafe-ci.org/hub/user-redirect/notebooks/CommunityData/OpenSees/TrainingMaterial/training-OpenSees-on-DesignSafe/Jupyter_Notebooks/tapis_getJobOutData_AccessData.ipynb' target='_blank'>Open in JupyterHub</a></sub>
  - [List All Job Output](Jupyter_Notebooks/tapis_getJobOutData_OutputFiles_Metadata.ipynb)
      <sub>📂 <a href='https://jupyter.designsafe-ci.org/hub/user-redirect/notebooks/CommunityData/OpenSees/TrainingMaterial/training-OpenSees-on-DesignSafe/Jupyter_Notebooks/tapis_getJobOutData_OutputFiles_Metadata.ipynb' target='_blank'>Open in JupyterHub</a></sub>
  - [Download All Job Output](Jupyter_Notebooks/tapis_getJobOutData_OutputFiles_Download.ipynb)
      <sub>📂 <a href='https://jupyter.designsafe-ci.org/hub/user-redirect/notebooks/CommunityData/OpenSees/TrainingMaterial/training-OpenSees-on-DesignSafe/Jupyter_Notebooks/tapis_getJobOutData_OutputFiles_Download.ipynb' target='_blank'>Open in JupyterHub</a></sub>
  - [Explore Jobs Interactively](Jupyter_Notebooks/tapis_getJobList_ExploreJobsInteractive.ipynb)
      <sub>📂 <a href='https://jupyter.designsafe-ci.org/hub/user-redirect/notebooks/CommunityData/OpenSees/TrainingMaterial/training-OpenSees-on-DesignSafe/Jupyter_Notebooks/tapis_getJobList_ExploreJobsInteractive.ipynb' target='_blank'>Open in JupyterHub</a></sub>
  - [Cancel Tapis Job](Docs_MD/tapis_cancelJob.md)
- [Tapis Apps](Docs_MD/tapis_apps.md)

## Run OpenSees using Tapis Apps
- [OpenSees Tapis Apps](Docs_MD/tapis_OpenSeesApps.md)
- [Process Overview](Docs_MD/tapis_submit_process.md)
- [Run Tapis OpenSees](Jupyter_Notebooks/tapis_submitJob_DSapp_OpenSees_Detailed.ipynb)
      <sub>📂 <a href='https://jupyter.designsafe-ci.org/hub/user-redirect/notebooks/CommunityData/OpenSees/TrainingMaterial/training-OpenSees-on-DesignSafe/Jupyter_Notebooks/tapis_submitJob_DSapp_OpenSees_Detailed.ipynb' target='_blank'>Open in JupyterHub</a></sub>
- [Run Tapis OpenSees-Express](Jupyter_Notebooks/tapis_submitJob_DSapp_OpenSees_Compact_OpsExpress.ipynb)
      <sub>📂 <a href='https://jupyter.designsafe-ci.org/hub/user-redirect/notebooks/CommunityData/OpenSees/TrainingMaterial/training-OpenSees-on-DesignSafe/Jupyter_Notebooks/tapis_submitJob_DSapp_OpenSees_Compact_OpsExpress.ipynb' target='_blank'>Open in JupyterHub</a></sub>
- [Run Tapis OpenSeesMP](Jupyter_Notebooks/tapis_submitJob_DSapp_OpenSees_Compact_OpsMP.ipynb)
      <sub>📂 <a href='https://jupyter.designsafe-ci.org/hub/user-redirect/notebooks/CommunityData/OpenSees/TrainingMaterial/training-OpenSees-on-DesignSafe/Jupyter_Notebooks/tapis_submitJob_DSapp_OpenSees_Compact_OpsMP.ipynb' target='_blank'>Open in JupyterHub</a></sub>

## Python Utilities
- [OpsUtils](OpsUtils_Docs/Misc/OpsUtils_Intro.md)
- [Miscellaneous OpsUtils](OpsUtils_Docs/Misc/OpsUtils_Misc.md)
  - [convert_tacc_time](OpsUtils_Docs/Misc/convert_tacc_time.md)
  - [convert_time_unix](OpsUtils_Docs/Misc/convert_time_unix.md)
  - [display_images_in_xbox](OpsUtils_Docs/Misc/display_images_in_xbox.md)
  - [empty_folder](OpsUtils_Docs/Misc/empty_folder.md)
  - [flatten_dict](OpsUtils_Docs/Misc/flatten_dict.md)
  - [get_files_recursive](OpsUtils_Docs/Misc/get_files_recursive.md)
  - [get_now_unix](OpsUtils_Docs/Misc/get_now_unix.md)
  - [queryDF](OpsUtils_Docs/Misc/queryDF.md)
  - [show_text_file_in_accordion](OpsUtils_Docs/Misc/show_text_file_in_accordion.md)
  - [show_video](OpsUtils_Docs/Misc/show_video.md)
  - [unix_to_tacc_time](OpsUtils_Docs/Misc/unix_to_tacc_time.md)
- [Tapis OpsUtils](OpsUtils_Docs/Tapis/OpsUtils_Tapis.md)
  - [analyze_tacc_job_history](OpsUtils_Docs/Tapis/analyze_tacc_job_history.md)
  - [bump_app_version()](OpsUtils_Docs/Tapis/bump_app_version.md)
  - [cancel_tapis_job](OpsUtils_Docs/Tapis/cancel_tapis_job.md)
  - [connect_tapis](OpsUtils_Docs/Tapis/connect_tapis.md)
  - [display_tapis_app_schema](OpsUtils_Docs/Tapis/display_tapis_app_schema.md)
  - [establish_tms_credentials](OpsUtils_Docs/Tapis/establish_tms_credentials.md)
  - [explore_tapis_job](OpsUtils_Docs/Tapis/explore_tapis_job.md)
  - [filter_tapis_jobs_df](OpsUtils_Docs/Tapis/filter_tapis_jobs_df.md)
  - [find_work_path_path](OpsUtils_Docs/Tapis/find_work_path_path.md)
  - [find_work_path](OpsUtils_Docs/Tapis/find_work_path.md)
  - [get_latest_app_version](OpsUtils_Docs/Tapis/get_latest_app_version.md)
  - [get_system_queues](OpsUtils_Docs/Tapis/get_system_queues.md)
  - [get_tapis_app_schema](OpsUtils_Docs/Tapis/get_tapis_app_schema.md)
  - [get_tapis_job_all_files](OpsUtils_Docs/Tapis/get_tapis_job_all_files.md)
  - [get_tapis_job_description](OpsUtils_Docs/Tapis/get_tapis_job_description.md)
  - [get_tapis_job_history_data](OpsUtils_Docs/Tapis/get_tapis_job_history_data.md)
  - [get_tapis_job_metadata](OpsUtils_Docs/Tapis/get_tapis_job_metadata.md)
  - [get_tapis_job_status](OpsUtils_Docs/Tapis/get_tapis_job_status.md)
  - [get_tapis_jobs_df](OpsUtils_Docs/Tapis/get_tapis_jobs_df.md)
  - [get_tapis_jobs](OpsUtils_Docs/Tapis/get_tapis_jobs.md)
  - [get_tapis_tenant_and_username](OpsUtils_Docs/Tapis/get_tapis_tenant_and_username.md)
  - [get_tapis_username](OpsUtils_Docs/Tapis/get_tapis_username.md)
  - [get_user_path_tapis_uri](OpsUtils_Docs/Tapis/get_user_path_tapis_uri.md)
  - [get_user_work_tapis_uri](OpsUtils_Docs/Tapis/get_user_work_tapis_uri.md)
  - [interactive_tapis_job_explorer](OpsUtils_Docs/Tapis/interactive_tapis_job_explorer.md)
  - [monitor_tapis_job](OpsUtils_Docs/Tapis/monitor_tapis_job.md)
  - [print_nested_tapisresult](OpsUtils_Docs/Tapis/print_nested_tapisresult.md)
  - [revoke_tms_credentials](OpsUtils_Docs/Tapis/revoke_tms_credentials.md)
  - [run_tapis_job](OpsUtils_Docs/Tapis/run_tapis_job.md)
  - [submit_tapis_job](OpsUtils_Docs/Tapis/submit_tapis_job.md)
  - [validate_app_folder](OpsUtils_Docs/Tapis/validate_app_folder.md)
