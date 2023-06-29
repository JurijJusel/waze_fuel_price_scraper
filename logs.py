import datetime

class Logger:
    def __init__(self, obj) -> None:
        self.timestamp = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.name = obj.name
        self.status = obj.status
        self.url = obj.url
        self.fuel_updated_date = obj.fuel_updated_date
        self.company = obj.company
        self.adress = obj.adress
        self.name_D = obj.name_D
        self.price_D = obj.price_D 
        self.name_A95 = obj.name_A95
        self.price_A95 = obj.price_A95
        self.resp_err = obj.resp_err
        
    
    def status_log(self):
        if self.status == 200: 
            log_status = f"{self.timestamp}, status code: {self.status}, {self.name}"
            self.write_logs(log_status, "logs.txt")
            if  self.fuel_updated_date == None:
                log_fuel_updated_date = f"{self.timestamp}, status code: {self.status}, {self.name}, error get fuel_updated_date"
                self.write_logs(log_fuel_updated_date, "logs.txt")
            if self.company == None:
                log_company = f"{self.timestamp}, status code: {self.status}, {self.name}, error get company"
                self.write_logs(log_company, "logs.txt")
            if self.adress == None:
                log_adress = f"{self.timestamp}, status code: {self.status}, {self.name}, error get adress"
                self.write_logs(log_adress, "logs.txt")
            if self.name_D == None:
                log_name_D = f"{self.timestamp}, status code: {self.status}, {self.name}, error get name_D"
                self.write_logs(log_name_D, "logs.txt")    
            if self.price_D == None:
                log_price_D = f"{self.timestamp}, status code: {self.status}, {self.name}, error get price_D"
                self.write_logs(log_price_D, "logs.txt") 
            if self.name_A95 == None:
                log_name_A95 = f"{self.timestamp}, status code: {self.status}, {self.name}, error get name_A95"
                self.write_logs(log_name_A95, "logs.txt")    
            if self.price_A95 == None:
                log_price_A95 = f"{self.timestamp}, status code: {self.status}, {self.name}, error get price_A95"
                self.write_logs(log_price_A95, "logs.txt")      
        else:
            log_status =  f"{self.timestamp}, {self.name}, error: {self.resp_err}"   
            self.write_logs(log_status, "logs.txt") 
        
        
    def data_value_logs(self):
        return f"{self.timestamp}, {self.name}, {self.status}, {self.url}, {self.company}, {self.adress}"  #, {self.name_D} {self.price_D}, {self.adress}"
    

    def write_logs(self, text, txt_file):
        try:
            with open(txt_file, 'a') as file:
                file.write(text + "\n")
                # file.write(str(text) + "\n")
            print(f"Successfully wrote logs to <{txt_file}>.")
        except IOError as ioe:
            print(f"Error: {ioe}, Failed write logs to <{txt_file}>.")
    