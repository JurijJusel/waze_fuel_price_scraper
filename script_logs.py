import datetime


class Script_log:
      
    def __init__(self):
        self.txt_file = 'logs.txt'

    def count_write_logs(func):
        def inner(*args, **kwargs):
            inner.calls += 1
            func(*args, **kwargs)
        inner.calls = 0
        return inner  
  
    @count_write_logs
    def write_log(self, name, message):
        time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_status = f"{time_stamp}, {name}, {message}"
        
        with open(self.txt_file, 'a') as file:
            file.write(log_status + "\n")

    def __str__(self):
        return f"Number of script logs: {self.write_log.calls}"