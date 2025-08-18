# def make_job_meta_df(jobslist,displayIt='head'):
#     # Silvia Mazzoni, 2025
#     # make Dataframe out of Tapis-return list
#     # Convert each job to a dictionary
#     import pandas as pd
#     def flatten_dict_local(d, parent_key='', sep='.'):
#         """
#         Recursively flattens a nested dictionary, including:
#         - Lists with index notation (e.g., key[0])
#         - JSON strings that are actually dictionaries
#         - TapisResult objects into their internal attributes
#         """
#         import json
#         from tapipy.tapis import TapisResult
        
#         items = []

#         for k, v in d.items():
#             # Construct the new key path
#             new_key = f"{parent_key}{sep}{k}" if parent_key else k

#             # If value is None, add directly
#             if v is None:
#                 items.append((new_key, None))
#                 continue

#             # If it's a dictionary, flatten it recursively
#             if isinstance(v, dict):
#                 items.extend(flatten_dict_local(v, new_key, sep=sep).items())
#                 continue

#             # If it's a number (int or float), add it directly
#             if isinstance(v, (int, float)):
#                 items.append((new_key, v))
#                 continue

#             # If it's a list, handle each item
#             if isinstance(v, list):
#                 for idx, item in enumerate(v):
#                     indexed_key = f"{new_key}[{idx}]"
#                     if isinstance(item, dict):
#                         items.extend(flatten_dict_local(item, indexed_key, sep=sep).items())
#                     else:
#                         items.append((indexed_key, item))
#                 continue

#             # Handle TapisResult objects
#             if isinstance(v, TapisResult):
#                 data_dict = v.__dict__
#                 items.extend(flatten_dict_local(data_dict, new_key, sep=sep).items())
#                 continue

#             # Try to parse JSON strings that are dictionaries
#             try:
#                 parsed_json = json.loads(v)
#                 if isinstance(parsed_json, dict):
#                     items.extend(flatten_dict_local(parsed_json, new_key, sep=sep).items())
#                 else:
#                     items.append((new_key, v))
#             except (json.JSONDecodeError, TypeError):
#                 items.append((new_key, v))

#         return dict(items)

    
#     jobsdicts = [job.__dict__ for job in jobslist]
#     # Apply flattening
#     flat_jobs = [flatten_dict_local(job_dict) for job_dict in jobsdicts]
#     # Create the DataFrame
#     df = pd.DataFrame(flat_jobs)
#     df["index_column"] = df.index
#     if displayIt != False:
#         print(f'Found {len(df)} jobs')
#     startCols = ['index_column','name','uuid','status','appId','appVersion']
#     columns =  startCols + [col for col in df.columns if not col in startCols]
#     JobsData_df = df[columns]
#     # Display the first few rows
#     if displayIt=='head' or displayIt=='displayHead':
#         display(df.head())
#     elif displayIt==True or displayIt == 'displayAll':
#         display(df)
        
#     return df