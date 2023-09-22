import datetime

logs_write_count = 0
class Script_log:
    # logs_write_count = 0
        
    def __init__(self):
        self.txt_file = 'logs.txt'
        
    # def init_log_count(self):
    #     self.__class__.logs_write_count += 1   
    
    def write_log(self, name, message):
        time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_status = f"{time_stamp}, {name}, {message}"
        # self.init_log_count() 
        # __class__.logs_write_count += 1
        # type(self).logs_write_count += 1
        # self.logs_write_count += 1
        global logs_write_count
        logs_write_count += 1
        
        with open(self.txt_file, 'a') as file:
            file.write(log_status + "\n")
            # print(f"Logs {name}, successfully written to <{self.txt_file}>.") 
        
    def __str__(self):
        return f"Number of script logs: {logs_write_count}"
    
# logs_write_count = 0
   
# s = Script_log()

# print(dir(s))
