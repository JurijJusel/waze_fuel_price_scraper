import os
from constants import script_run_files


script_dir = "scripts/"
executed_files = []
all_script_files = []

def run_scripts():
    count = 0
    for script_file in os.listdir(script_dir):
        if script_file.endswith('.py'):
            all_script_files.append(script_file)  
        if script_file[:-3] in script_run_files: 
            script_path = os.path.join(script_dir, script_file) #path = Path(f"data/{file}")
            with open(script_path, 'r') as file:
                script_code = file.read()
                exec(script_code, globals())  # Include globals() as second argument!!!!
                count += 1
                executed_files.append(script_file)
                
    print(f"Number of files executed: {count}")
    print("Executed files:", executed_files)
    print("Unexecuted files from scripts folder:", [file for file in all_script_files if file not in executed_files])
    print("All files in scrips folder", all_script_files)







  # import subprocess   
        # if script_file[:-3] in script_run_files:
        #     script_path = os.path.join(script_dir, script_file)
        #     process = subprocess.Popen(['python3', script_path])
        #     process.wait()
        #     if process.returncode == 0:
        #         count += 1
        #         executed_files.append(script_file)
        
        
        
# run_scripts()
# all_script_files = [file for file in os.listdir(script_dir) if file.endswith('.py')]

# for script_file in os.listdir(script_dir):
#     if script_file.endswith('.py'):
#         script_name = script_file[:-3]  # Remove the .py extension
#         script_path = os.path.join(script_dir, script_file)
#         if os.path.isfile(script_path):
#             with open(script_path, 'r') as file:
#                 script_code = file.read()
#             exec(script_code)
#             count += 1
#             executed_files.append(script_name)

# for script_file in script_files.script_files:
#     script_path = os.path.join(script_dir, f"{script_file}.py")
#     if os.path.isfile(script_path):
#         with open(script_path, 'r') as file:
#             script_code = file.read()
#         exec(script_code)
#         count += 1
#         executed_files.append(script_file)

# for script_file in os.listdir(script_dir):
#     if script_file.endswith('.py'):
#         script_name = script_file[:-3]  # Remove the .py extension
#         script_path = os.path.join(script_dir, script_file)
#         if os.path.isfile(script_path):
#             with open(script_path, 'r') as file:
#                 script_code = file.read()
#             exec(script_code)
#             count += 1
#             executed_files.append(script_name)

