import datetime
from utils.file import write_logs

class Logger:
    def __init__(self, obj) -> None:
        self.timestamp = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.name = obj.name
        self.req_status = obj.req_status
        # self.exc_err = obj.exc_err
        
        # self.url = obj.url
        # self.fuel_updated_date = obj.fuel_updated_date
        # self.company = obj.company
        # self.adress = obj.adress
        # self.name_D = obj.name_D
        # self.price_D = obj.price_D 
        # self.name_A95 = obj.name_A95
        # self.price_A95 = obj.price_A95
        # self.exc_err= obj.exc_err

    def write_status_log(self):
        log_messages = []
        log_status = f"{self.timestamp}, status code: {self.req_status}, {self.name}"
        log_messages.append(log_status)
        log_text = "\n".join(log_messages)
        # write_logs(log_status, "logs.txt")
        write_logs(log_text, "logs.txt")
        
        # # if self.status == 200:
        # if self.req_status == 200:
        #     log_status = f"{self.timestamp}, status code: {self.req_status}, {self.name}"
        #     print(log_status)
        #     log_messages.append(log_status)

        #     attribute_checks = {
        #         "fuel_updated_date": "error get fuel_updated_date",
        #         "company": "error get company",
        #         "adress": "error get adress",
        #         "name_D": "error get name_D",
        #         "price_D": "error get price_D",
        #         "name_A95": "error get name_A95",
        #         "price_A95": "error get price_A95"
        #     }

        #     for attribute, error_message in attribute_checks.items():
        #         if getattr(self, attribute) is None:
        #             log_message = f"{self.timestamp}, status code: {self.req_status}, {self.name}, {error_message}"
        #             log_messages.append(log_message)
        # else:
        #     print("status_log, else!!!!!")
        #     log_status = f"{self.timestamp}, {self.name}, error: {self.exc_err}"
        #     log_messages.append(log_status)

        # log_text = "\n".join(log_messages)
        # write_logs(log_text, "logs.txt")
        
        
           
    # def status_log(self):
    #     log_messages = []

    #     # if self.status == 200:
    #     if self.req_status == 200:
    #         log_status = f"{self.timestamp}, status code: {self.req_status}, {self.name}"
    #         print(log_status)
    #         log_messages.append(log_status)

    #         attribute_checks = {
    #             "fuel_updated_date": "error get fuel_updated_date",
    #             "company": "error get company",
    #             "adress": "error get adress",
    #             "name_D": "error get name_D",
    #             "price_D": "error get price_D",
    #             "name_A95": "error get name_A95",
    #             "price_A95": "error get price_A95"
    #         }

    #         for attribute, error_message in attribute_checks.items():
    #             if getattr(self, attribute) is None:
    #                 log_message = f"{self.timestamp}, status code: {self.req_status}, {self.name}, {error_message}"
    #                 log_messages.append(log_message)
    #     else:
    #         print("status_log, else!!!!!")
    #         log_status = f"{self.timestamp}, {self.name}, error: {self.exc_err}"
    #         log_messages.append(log_status)

    #     log_text = "\n".join(log_messages)
    #     write_logs(log_text, "logs.txt")
    
    
    
    
    
    # write_logs()   

    # def write_logs(self, text, txt_file):
    #     try:
    #         with open(txt_file, 'a') as file:
    #             file.write(text + "\n")
    #             # file.write(str(text) + "\n")
    #         print(f"Logs successfully written to <{txt_file}>.") 
    #     except IOError as ioe:
    #         print(f"Error: {ioe}, Failed write logs to <{txt_file}>.")


 # def status_log(self):
    #     if self.status == 200: 
    #         log_status = f"{self.timestamp}, status code: {self.status}, {self.name}"
    #         self.write_logs(log_status, "logs.txt")
    #         if  self.fuel_updated_date == None:
    #             log_fuel_updated_date = f"{self.timestamp}, status code: {self.status}, {self.name}, error get fuel_updated_date"
    #             self.write_logs(log_fuel_updated_date, "logs.txt")
    #         if self.company == None:
    #             log_company = f"{self.timestamp}, status code: {self.status}, {self.name}, error get company"
    #             self.write_logs(log_company, "logs.txt")
    #         if self.adress == None:
    #             log_adress = f"{self.timestamp}, status code: {self.status}, {self.name}, error get adress"
    #             self.write_logs(log_adress, "logs.txt")
    #         if self.name_D == None:
    #             log_name_D = f"{self.timestamp}, status code: {self.status}, {self.name}, error get name_D"
    #             self.write_logs(log_name_D, "logs.txt")    
    #         if self.price_D == None:
    #             log_price_D = f"{self.timestamp}, status code: {self.status}, {self.name}, error get price_D"
    #             self.write_logs(log_price_D, "logs.txt") 
    #         if self.name_A95 == None:
    #             log_name_A95 = f"{self.timestamp}, status code: {self.status}, {self.name}, error get name_A95"
    #             self.write_logs(log_name_A95, "logs.txt")    
    #         if self.price_A95 == None:
    #             log_price_A95 = f"{self.timestamp}, status code: {self.status}, {self.name}, error get price_A95"
    #             self.write_logs(log_price_A95, "logs.txt")      
    #     else:
    #         log_status =  f"{self.timestamp}, {self.name}, error: {self.resp_err}"   
    #         self.write_logs(log_status, "logs.txt") 