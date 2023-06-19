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
        except IOError:
            print(f"Error: Failed write logs to <{txt_file}>.")




    # def __str__(self):
    #     return f"{self.timestamp}, {self.status}, {self.name}, {self.url}"


# log = Logger("1", "2", "6", "4")
# print(log)
# a_to_txt = log.data_to_txt()

# print("id:", log.id)
# print(log.name)
# print(log.url)
# print(log.status)
# print(log.timestamp)

# write_to_txt_file(a_to_txt, 'logs.txt')