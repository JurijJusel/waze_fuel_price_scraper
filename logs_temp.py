import datetime
from utils.file import write_logs

time_stamp = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def write_log(name, message):
    log_status = f"{time_stamp}, {name}, {message}"
    return write_logs(log_status, "logs.txt")
    
  