import os
from constants import script_run_files
import requests
from constants import url, scripts_dir
from script_logs import Script_log
import asyncio


script_log = Script_log()
class Scripts:
    def __init__(self) -> None:
        self.executed_files = []
        self.all_script_files = []

    async def run_scripts(self):
        self.count = 0
        self.req = requests.get(url)
        if self.req.status_code == 200:          
            for script_file in os.listdir(scripts_dir):
                if script_file.endswith('.py'):
                    self.all_script_files.append(script_file)  
                if script_file[:-3] in script_run_files: 
                    script_path = os.path.join(scripts_dir, script_file) #path = Path(f"data/{file}")
                    with open(script_path, 'r') as file:
                        script_code = file.read()
                        exec(script_code, globals())  # Include globals() as second argument!
                        self.count += 1
                        self.executed_files.append(script_file)   
            self.print_scripts_ind()
        else:
            script_log.write_log(url, f"status code: {self.req.status_code}, ConnectionError")
            return None
       
    def print_scripts_ind(self):     
        print(f"Number of running files: {self.count}")
        print("Executed files:", self.executed_files)
        print("Unexecuted files from scripts folder:", [file for file in self.all_script_files if file not in self.executed_files])
        print("All files in scrips folder:", self.all_script_files)
    
    def async_run_scripts(self):
        main_loop = asyncio.get_event_loop()
        main_task = main_loop.create_task(self.run_scripts())
        main_loop.run_until_complete(main_task)
        main_loop.close()
