from bs4 import BeautifulSoup
import requests
from utils.file import create_json
from constants import headers
from urls import urls
from station import Station


class FuelCrawler:
    def __init__(self, name):
        self.name = name
        self.url = self.get_url_by_name()
        self.headers = headers
        self.json_file = 'fuel.json'
        self.posts = []

    
    def get_url_by_name(self):
        selected_url = next(item['url'] for item in urls if item['name'] == self.name)
        return selected_url
    

    def download_response(self):
        req = requests.get(self.url, self.headers )
        if req.status_code == 200:
            soup = BeautifulSoup(req.content, features="lxml")
            return soup
        else:
            print("Error info:", req.status_code, self.url)
            raise Exception("Failed to download response")

        
    def get_data(self, soup):
        table_rows = soup.find_all('tr')
        for index in range(1, len(table_rows)):
            table_row = table_rows[index]
            fuel_updated_date = soup.find('p', class_='last-updated').text[-19::]
            company = table_row.find('td').text[2:27].rstrip()
            adress = table_row.find('small').text  
            name_D = table_row.find_all('td')[1].get("data-id")[-6::] 
            price_D = table_row.find_all('td')[1].get_text(strip=True)
            name_A95 = table_row.find_all('td')[2].get("data-id")[-2::]   
            price_A95 = table_row.find_all('td')[2].get_text(strip=True) 

            station = Station(company, adress, fuel_updated_date, name_D, price_D, name_A95, price_A95)
            self.posts.append(station.data) 
           
        return self.posts
    
       
    def get_responce(self):
        try:
            soup_response = self.download_response()
            return self.get_data(soup_response)
        except Exception as e:
            print("Error exception info:", str(e))
        
      
    def data_to_json(self):
        self.get_responce()
        create_json(self.posts, self.json_file )
    
            
if __name__ == '__main__':
    station = FuelCrawler('Circle')
    station.data_to_json()
   
