# # /home/jupyter/CommunityData/OpenSees/TrainingMaterial/training-OpenSees-on-DesignSafe/OpsUtils/OpsUtils/Tapis/get_tapis_job_description.py
# def get_tapis_job_description(t, tapisInput):
#     """
#     Build a complete Tapis v3 job description dict from user-friendly inputs.

#     This function:
#       1) Resolves the Files base URL for inputs from `tapisInput["storage_system"]`
#          (supports MyData/community/published; can be overridden via
#          `tapisInput["storage_system_baseURL"]`).
#       2) Ensures a concrete application version:
#          - If `appVersion` is missing or equals "latest", it resolves a pinned
#            version via `OpsUtils.get_latest_app_version(t, )`.
#       3) Validates required fields (set differs for OpenSees-Express vs. HPC apps).
#       4) Constructs job attributes, fileInputs, parameterSet, and archive settings.

#     Auto baseURL selection
#     ----------------------
#     If `storage_system_baseURL` is not provided:
#       - If `storage_system` contains "mydata": uses
#         `tapis://designsafe.storage.default/` where `` is taken
#         from `t.authenticator.get_userinfo().username`.
#       - If `storage_system` contains "community": uses
#         `tapis://designsafe.storage.community`
#       - If `storage_system` contains "published": uses
#         `tapis://designsafe.storage.published`
#       - Else: prints a message and returns -1.

#     App families and required keys
#     ------------------------------
#     *OpenSees-Express* (`appId == "opensees-express"`)
#       Required: ['name','appId','appVersion','maxMinutes','archive_system',
#                  'storage_system','input_folder','Main Script']
#       - Sets `parameterSet.envVariables` with:
#           mainProgram = OpenSees
#           tclScript   = 

#       - `fileInputs = [{"name": "Input Directory", "sourceUrl": "/"}]`
#       - Archive options:
#           archive_system == 'MyData' -> designsafe.storage.default under
#               ${EffectiveUserId}/tapis-jobs-archive/${JobCreateDate}/${JobUUID}
#           archive_system == 'Temp'   -> cloud.data:/tmp/${JobOwner}/tapis-jobs-archive/...

#     *HPC OpenSees apps* (e.g., opensees-mp-s3, opensees-sp-*, etc.)
#       Required: ['name','appId','appVersion','execSystemId','execSystemLogicalQueue',
#                  'nodeCount','coresPerNode','maxMinutes','allocation','archive_system',
#                  'storage_system','input_folder','Main Script']
#       - Sets base job attributes (system, queue, resources).
#       - `parameterSet.appArgs = [{"name": "Main Script", "arg": 
# }]`
#       - `parameterSet.schedulerOptions = [{"name": "TACC Allocation",
#                                            "arg": f"-A {allocation}"}]`
#       - `fileInputs` as above.
#       - Archive options:
#           archive_system == 'MyData' -> designsafe.storage.default under
#               ${EffectiveUserId}/tapis-jobs-archive/${JobCreateDate}/${JobUUID}
#           archive_system == 'Work'   -> exec system $WORK/tapis-jobs-archive/...

#     Returns
#     -------
#     dict
#         A fully formed Tapis job description ready for submission.
#         Returns -1 if validation fails or baseURL/appVersion cannot be determined.

#     Side effects
#     ------------
#     - Prints a list of missing required keys (if any).
#     - Prints a short confirmation ("All Input is Complete") on success.

#     Author
#     ------
#     Silvia Mazzoni, DesignSafe (silviamazzoni@yahoo.com)

#     Date
#     ----
#     2025-08-16

#     Version
#     -------
#     1.2
#     """
#     # Silvia Mazzoni, 2025
#     from OpsUtils import OpsUtils  # for get_latest_app_version

#     def checkRequirements(tapisInputIN, RequiredInputList):
#         nmiss = 0
#         for thisReq in RequiredInputList:
#             if thisReq not in tapisInputIN:
#                 nmiss += 1
#                 print(f"YOU need to define the following input: {thisReq}")
#         return nmiss


#     appId = tapisInput["appId"]
#     # print('appId',appId)

#     # --- Ensure a concrete appVersion (resolve 'latest' or missing) ---
#     if ("appVersion" not in tapisInput) or (str(tapisInput["appVersion"]).lower() == "latest"):
#         resolved = OpsUtils.get_latest_app_version(t, appId)
#         if not resolved or resolved in ("none", ""):
#             print(f"Unable to resolve latest version for appId='{appId}'. Please specify appVersion.")
#             return -1
#         tapisInput["appVersion"] = resolved
        


#     # --- Get App Schema ---
#     appMetaData = t.apps.getAppLatestVersion(appId=appId)
#     app_MetaData = appMetaData.__dict__
#     app_jobAttributes = app_MetaData['jobAttributes'].__dict__
#     app_parameterSet = app_jobAttributes['parameterSet'].__dict__

    
    
#     # --- Resolve storage baseURL if needed ---
#     if len(app_jobAttributes['fileInputs'])>0:
#         if "sourceUrl" not in tapisInput:
#             if "storage_system_baseURL" not in tapisInput:
#                 if 'storage_system' not in tapisInput:
#                     print('NEED more info for your input directory')
#                     return -1
#                 storage_system_lower = tapisInput.get("storage_system", "").lower()
#                 tapisInput['storage_system_baseURL'] = OpsUtils.get_user_path_tapis_uri(t,storage_system_lower)
#                 # print("tapisInput['storage_system_baseURL']",tapisInput['storage_system_baseURL'])
#             tapisInput["sourceUrl"] = f"{tapisInput['storage_system_baseURL']}"
#             if 'input_folder' in tapisInput:
#                 tapisInput["sourceUrl"] = f"{tapisInput['sourceUrl']}/{tapisInput['input_folder']}"
        
#         print('input directory URI:',tapisInput["sourceUrl"])
        



#     inputKeys_App = ['id','version']
#     inputKeys_jobAttributes = ['execSystemId', 'execSystemLogicalQueue', 'archiveSystemId', 'archiveSystemDir', 'nodeCount', 'coresPerNode', 'memoryMB', 'maxMinutes']    
    
    
#     # --- Defaults & branching ---
#     # If Express, default the exec system to the Express VM unless provided
#     if appId == "opensees-express" and "execSystemId" not in tapisInput:
#         tapisInput["execSystemId"] = "wma-exec-01"
#     if "execSystemId" not in tapisInput:
#         tapisInput["execSystemId"] = "stampede3"

#     job_description = {}
#     nmiss = 999

#     # Express (runs on wma-exec-01)
#     if appId == "opensees-express":
#         RequiredInputList = [
#             "name", "appId", "maxMinutes", "archive_system",
#             "storage_system", "input_folder", "Main Script"
#         ]
#         nmiss = checkRequirements(tapisInput, RequiredInputList)
#         if nmiss == 0:
#             parameterSet = {}
#             job_description["name"] = tapisInput["name"]
#             job_description["maxMinutes"] = tapisInput["maxMinutes"]
#             job_description["appId"] = tapisInput["appId"]
#             if 'appVersion' in tapisInput.keys():
#                 job_description["appVersion"] = tapisInput["appVersion"]
#             fileInputs = [{"name": "Input Directory", "sourceUrl": tapisInput["sourceUrl"]}]; # keep as is!
#             if not 'Main Program' in tapisInput.keys():
#                 tapisInput["Main Program"] = 'OpenSees'
#             parameterSet["envVariables"] = [
#                 {"key": "mainProgram", "value": tapisInput["Main Program"]},
#                 {"key": "tclScript", "value": tapisInput["Main Script"]},
#             ]
#             job_description["fileInputs"] = fileInputs
#             job_description["parameterSet"] = parameterSet

#     else:
#         # HPC (e.g., OpenSeesMP/SP on Stampede3)

#         RequiredInputList = [
#             "name","appId","execSystemId","execSystemLogicalQueue",
#             "nodeCount","coresPerNode","maxMinutes","allocation","archive_system",
#         ]
#         nmiss = checkRequirements(tapisInput, RequiredInputList)
#         if nmiss == 0:
#             parameterSet = {}
#             job_description["name"] = tapisInput["name"]
#             job_description["execSystemId"] = tapisInput["execSystemId"]
#             job_description["execSystemLogicalQueue"] = tapisInput["execSystemLogicalQueue"]
#             job_description["maxMinutes"] = tapisInput["maxMinutes"]
#             job_description["nodeCount"] = tapisInput["nodeCount"]
#             job_description["coresPerNode"] = tapisInput["coresPerNode"]
#             job_description["appId"] = tapisInput["appId"]
#             if 'appVersion' in tapisInput.keys():
#                 job_description["appVersion"] = tapisInput["appVersion"]
#             if len(app_jobAttributes['fileInputs'])>0:
#                 fileInputs = [{"name": "Input Directory", "sourceUrl": tapisInput["sourceUrl"]}]
#             # if not 'Main Program' in tapisInput.keys():
#             #     tapisInput["Main Program"] = 'OpenSeesMP'
#             # if not 'CommandLine Arguments' in tapisInput:
#             #     tapisInput["CommandLine Arguments"] = ''


            
#             HEREkey = 'appArgs'
#             # print('HEREkey',HEREkey)
#             parameterSet[HEREkey] = []
#             for app_Dict in app_parameterSet[HEREkey]:
#                 app_Dict = app_Dict.__dict__
#                 # print('app_Dict',app_Dict)
#                 here_name = app_Dict['name']
#                 here_dict = {"name":here_name,"arg":app_Dict['arg']}
#                 if 'notes' in app_Dict:
#                     app_Dict_notes = app_Dict['notes'].__dict__
#                     if 'isHidden' in app_Dict_notes and app_Dict_notes['isHidden']==True:
#                         continue
#                 if here_name in tapisInput:
#                     here_dict["arg"] = tapisInput[here_name]
#                 parameterSet[HEREkey].append(here_dict)
#             HEREkey = 'envVariables'
#             # print('HEREkey',HEREkey)
#             parameterSet[HEREkey] = []
#             for app_Dict in app_parameterSet[HEREkey]:
#                 app_Dict = app_Dict.__dict__
#                 # print('app_Dict',app_Dict)
#                 here_name = app_Dict['key']
#                 here_dict = {"key":here_name,"value":app_Dict['value']}
#                 if 'notes' in app_Dict:
#                     app_Dict_notes = app_Dict['notes'].__dict__
#                     if 'isHidden' in app_Dict_notes and app_Dict_notes['isHidden']==True:
#                         continue
#                 if here_name in tapisInput:
#                     here_dict["value"] = tapisInput[here_name]
#                 parameterSet[HEREkey].append(here_dict)



            
            
#             parameterSet["schedulerOptions"] = [{"name": "TACC Allocation", "arg": f"-A {tapisInput['allocation']}"}]
#             if len(app_jobAttributes['fileInputs'])>0:
#                 job_description["fileInputs"] = fileInputs
#             job_description["parameterSet"] = parameterSet


    
#     if nmiss == 0:
#         # print('app_MetaData_keys',app_MetaData.keys())
#         for hereKey in tapisInput.keys():
#             # print('hereKey',hereKey)
#             if hereKey in app_MetaData.keys() or hereKey in ['moduleLoads']:
#                 # print('yes')
#                 job_description[hereKey] = tapisInput[hereKey]
        
#         # Archive location
#         if "archive_system" in tapisInput:
#             if tapisInput["archive_system"] == "MyData":
#                 job_description["archiveSystemId"] = "designsafe.storage.default"
#                 job_description["archiveSystemDir"] = "${EffectiveUserId}/tapis-jobs-archive/${JobCreateDate}/${JobUUID}"
#             elif tapisInput["archive_system"] == "Work" and tapisInput["execSystemId"] != "wma-exec-01":
#                 job_description["archiveSystemId"] = tapisInput["execSystemId"]
#                 job_description["archiveSystemDir"] = "HOST_EVAL($WORK)/tapis-jobs-archive/${JobCreateDate}/${JobName}-${JobUUID}"
#             else:
#                 job_description["archiveSystemId"] = "designsafe.storage.default"
#                 job_description["archiveSystemDir"] = "${EffectiveUserId}/tapis-jobs-archive/${JobCreateDate}/${JobUUID}"
#         else:
#             job_description["archiveSystemId"] = "designsafe.storage.default"
#             job_description["archiveSystemDir"] = "${EffectiveUserId}/tapis-jobs-archive/${JobCreateDate}/${JobUUID}"



#     # --- Finalize ---
#     if nmiss > 0:
#         print("Please resubmit with all required input")
#         return -1
#     else:
#         # print("All Input is Complete")
#         # print('job_description',job_description)
#         return job_description
