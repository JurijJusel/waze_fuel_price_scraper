import datetime

class Logger:
    def __init__(self, obj) -> None:
        self.name = obj.name
        self.status = obj.status
        self.url = obj.url
        self.price_D = obj.price_D
        self.name_D = obj.name_D
        self.adress = obj.adress
        self.timestamp = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
       
       
    def data_sort_logs(self):
        return f"{self.timestamp}, {self.name}, {self.status}, {self.url}, {self.name_D} {self.price_D},{self.adress}"
    

    def write_logs(self, text, txt_file):
        try:
            with open(txt_file, 'a') as file:
                file.write(text + "\n")
            print(f"Successfully wrote logs to <{txt_file}>.")
        except IOError as ioe:
            print(f"Error: {ioe}, Failed write logs to <{txt_file}>.")

