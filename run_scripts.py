import os
from constants import script_run_files

class Scripts:
    def __init__(self) -> None:
        self.script_dir = "scripts/"
        self.executed_files = []
        self.all_script_files = []

    def run_scripts(self):
        self.count = 0
        for script_file in os.listdir(self.script_dir):
            if script_file.endswith('.py'):
                self.all_script_files.append(script_file)  
            if script_file[:-3] in script_run_files: 
                script_path = os.path.join(self.script_dir, script_file) #path = Path(f"data/{file}")
                with open(script_path, 'r') as file:
                    script_code = file.read()
                    exec(script_code, globals())  # Include globals() as second argument!
                    self.count += 1
                    self.executed_files.append(script_file)   
        self.print_scripts_ind()
        
    def print_scripts_ind(self):     
        print(f"Number of executed files: {self.count}")
        print("Executed files:", self.executed_files)
        print("Unexecuted files from scripts folder:", [file for file in self.all_script_files if file not in self.executed_files])
        print("All files in scrips folder:", self.all_script_files)