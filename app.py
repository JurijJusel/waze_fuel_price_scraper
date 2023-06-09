from bs4 import BeautifulSoup
import requests
from utils.file import create_json
from constants import headers, fuel_types_circle
from urls import urls
from station_circle import Station_circle

class FuelCrawler:
    def __init__(self, name):
        self.name = name
        self.url = self.get_url_by_name()
        self.station_circle = Station_circle()
        self.headers = headers
        self.json_file = 'fuel1.json'

    
    def get_url_by_name(self):
        selected_url = next(item['url'] for item in urls if item['name'] == self.name)
        return selected_url
    

    def download_response(self):
        req = requests.get(self.url, self.headers )
        if req.status_code == 200:
            soup = BeautifulSoup(req.text, features="lxml")
            return soup
        else:
            print("Error info:", req.status_code, self.url)
            raise Exception("Failed to download response")


    def get_prices(self):
        try:
            soup_response = self.download_response()
            self.circle_data = self.station_circle.circlek_prices(soup_response)
            return self.circle_data
        except Exception as e:
            print("Error exception info:", str(e))
        
      
    def print_data(self):
        self.get_prices()
        create_json(self.circle_data, self.json_file )
        updated_fuel_info = self.circle_data['updated_fuel_info']
        company = self.circle_data['company']
        for fuel_type in fuel_types_circle:
            fuel_value = self.circle_data[fuel_type]
            print(f"{updated_fuel_info}:  {company}  {fuel_type} - {fuel_value}")
      
    
if __name__ == '__main__':
    station = FuelCrawler('Circle')
    station.print_data()
   
