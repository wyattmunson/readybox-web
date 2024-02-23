import os
import json
import subprocess

# def create_folder_structure_json(path): 
#     # Initialize the result dictionary with folder 
#     # name, type, and an empty list for children 
#     print("CURRENT PATH", path)
#     result = {'name': os.path.basename(path), 
#             'type': 'folder', 'path': path, 'children': []} 

#     # Check if the path is a directory 
#     if not os.path.isdir(path): 
#         # result['path'] = "tes"  
#         # print("CURR PATH", path)
#         return result 

#     # Iterate over the entries in the directory 
#     for entry in os.listdir(path): 
#     # Create the full path for the current entry 
#         entry_path = os.path.join(path, entry) 
#         print("ENTRY", entry)
#         # result['path'] = entry_path

#         # If the entry is a directory, recursively call the function 
#         if os.path.isdir(entry_path): 
#             result['children'].append(create_folder_structure_json(entry_path)) 
#         # If the entry is a file, create a dictionary with name and type 
#         else: 
#             # result['path'] = entry_path
#             full_path = path + "/" + entry
#             result['children'].append({'name': entry, 'type': 'file', 'path': full_path}) 
    
#     return result
            

# # return result 
# folder_path = "/Users/wyatt/Downloads/folder1"

# # Call the function to create the JSON representation 
# folder_json = create_folder_structure_json(folder_path) 

# # Convert the dictionary to a JSON string with indentation 
# # folder_json_str = json.dumps(folder_json, indent=4) 

# # Print the JSON representation of the folder structure 
# # print(folder_json_str) 

# print("testing")
# print(folder_json)

# output = subprocess.run(['faker', '-v'], capture_output=True, )
# print (output)

package_list = {
        'docker': { 'versionCmd': ['docker', '-v']},
        'faker': { 'versionCmd': ['notcommand', '-v']},
        'git': { 'versionCmd': ['git', '-v']},
        'python': { 'versionCmd': ['python', '--version']}
        # 'node': { 'versionCmd': ['node', '-v']},
    }

# for i in package_list:
for i in package_list:
    print(i)
    print(package_list[i])
    print(package_list[i]["versionCmd"])
    sub = package_list[i]["versionCmd"]
    try: 
        res = subprocess.run(sub, capture_output=True)
        # res = package_list[i]['versionCmd']
        package_list[i]['result'] = res
        # data['faker'] = subprocess.run(['notcommand', '-v'], capture_output=True, shell=True)
        print("RES", res)
    except:
        package_list[i]['result'] = "Not installed"
        # data['faker'] = "Not installed"

print(package_list)