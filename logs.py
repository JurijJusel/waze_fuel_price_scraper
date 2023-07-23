import datetime
from pathlib import Path

class Crawl_logs:
    def __init__(self, name: str, message: str, txt_file="logs.txt"):
        self.name = name
        self.message = message
        self.txt_file = txt_file
    
    # def log_entry(self):
    #     return f"{self.time_stamp}, {self.name}, {self.message}"
    
    def write_log(name, message ):
        txt_file="logs.txt"
        time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        path = Path(f"data/{txt_file}")
        log_status = f"{time_stamp}, {name}, {message}"
        with open(path, 'a') as file:
            file.write(log_status + "\n")
            print(f"Logs successfully written to <{txt_file}>.") 
            
         
  
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
