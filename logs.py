import datetime

class Logger:
    def __init__(self, name, status, url, timestamp=str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))):
        self.name = name
        self.status = status
        self.url = url
        self.timestamp = timestamp 
       
       
    def data_to_log(self):
        return f"{self.timestamp}, {self.status}, {self.name}, {self.url}"
    

    def write_logs_to_txt(self, text, txt_file):
        try:
            with open(txt_file, 'a') as file:
                file.write(text + "\n")
            print(f"Successfully wrote logs to <{txt_file}>.")
        except IOError as ioe:
            print(f"Error: {ioe}, Failed write logs to <{txt_file}>.")
            
            