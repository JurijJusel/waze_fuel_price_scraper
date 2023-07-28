import datetime
from pathlib import Path

class Script_log:
    def __init__(self):
        self.txt_file = "logs.txt"
        self.time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def write_log(self, name, message):
        path = Path(f"data/{self.txt_file}")
        log_status = f"{self.time_stamp}, {name}, {message}"
        
        with open(path, 'a') as file:
            file.write(log_status + "\n")
            print(f"Logs {name}, successfully written to <{self.txt_file}>.") 
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
         
  
# def write_logs(name, message, txt_file="logs.txt"):
#     path = Path(f"data/{txt_file}")
#     try:
#         time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         log_status = f"{time_stamp}, {name}, {message}"
        
#         with open(path, 'a') as file:
#             file.write(log_status + "\n")
        
#         print(f"Logs successfully written to <{txt_file}>.") 
#     except IOError as ioe:
#         print(f"Error: {ioe}, Failed to write logs to <{txt_file}>.")
