from bs4 import BeautifulSoup
import requests
from utils.file import create_json
from constants import headers
from urls import urls
from station import Station
from logs import Logger


class FuelCrawler:
    def __init__(self, name):
        self.name = name
        self.url = self.get_url_by_company_name()
        self.headers = headers
        self.json_file = 'fuel.json'
        self.posts = []
        self.company = None
        self.adress = None
        self.status = None
        self.fuel_updated_date = None
        self.name_D = None
        self.price_D = None
        self.name_A95 = None
        self.price_A95 = None
        self.resp_err = None
        
        
    def get_url_by_company_name(self):
        selected_url = next(item['url'] for item in urls if item['name'] == self.name)
        return selected_url
    
        
    def download_response(self):
        req = requests.get(self.url, self.headers)
        if req.ok:
            self.status = req.status_code
            soup = BeautifulSoup(req.content, features="lxml")
            return soup
        else:
            self.status = req.status_code
    
      
    def get_data(self, soup):
        table_rows = soup.find_all('tr')
        for index in range(1, len(table_rows)): 
            table_row = table_rows[index]
            try:
                self.fuel_updated_date = soup.find('p', class_='last-updated').text[-19::]  
            except AttributeError as ae:
                self.fuel_updated_date = None
            try: 
                company_row_split = table_row.text.split(' ')[1:5]
                self.company = ' '.join(company_row_split).rstrip()   
            except AttributeError as ae:
                self.company = None
            try:   
                self.adress = table_row.find('small').text
            except AttributeError as ae:
                self.adress = None
            try:  
                self.name_D = table_row.select("td[data-id]")[0]["data-id"].split("-")[-1] 
            except IndexError as ie:
                self.name_D = None
            try:
                self.price_D = table_row.select("td[data-id]")[0].text
            except IndexError as ie:
                self.price_D = None
            try:
                self.name_A95 = table_row.select("td[data-id]")[1]["data-id"].split("-")[-1]
            except IndexError as ie:
                 self.name_A95 = None
            try:
                self.price_A95 = table_row.select("td[data-id]")[1].text 
            except IndexError as ie:
                self.price_A95 = None
            
            station = Station(self.company, self.adress, self.fuel_updated_date, self.name_D, self.price_D, self.name_A95, self.price_A95)
            data = station.data_to_dict()
            self.posts.append(data)
            
        return self.posts
       
    
    def try_get_responce(self):
        try:
            soup_response = self.download_response()
            return self.get_data(soup_response)
        # except Exception as e:
        #     print("!!!!!!!!!!!!!!!!!", type(e))
        #     print(soup_response)
        #     print("Error get responce exception info:", str(e))
        except requests.exceptions.ConnectionError as rqe:
            # print("Error get responce exception info:", rqe)
            self.resp_err = rqe
            
               
    def data_to_json(self):
        self.try_get_responce()
        create_json(self.posts, self.json_file )
        
            
if __name__ == '__main__':
    station = FuelCrawler('Circle')
    station.data_to_json()
    logger = Logger(station)
    # logger.write_logs(logger.status_log(), "logs.txt")
    # logger.write_logs(logger.data_value_logs(), "logs.txt")
    logger.status_log()
  
    
    
    
        
