from pathlib import Path
import datetime

class Script_log:
    logs_obj_count = 0
    
    def __init__(self):
        self.txt_file = 'logs.txt'
        
    def write_log(self, name, message):
        time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        Script_log.logs_obj_count += 1
        log_status = f"{time_stamp}, {name}, {message}"
        path = Path(f"data/{self.txt_file}")
        
        with open(path, 'a') as file:
            file.write(log_status + "\n")
            print(f"Logs {name}, successfully written to <{self.txt_file}>.") 
    
    def print_logs_obj_count(self):
        print(f"Number of script logs: {Script_log.logs_obj_count}")
