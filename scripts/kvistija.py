import requests
from bs4 import BeautifulSoup
from constants import headers
from app import FuelCrawler
from station import Station
from utils.file import create_json
from logs import write_log

station_circle = FuelCrawler(name='Kvistija')
name = station_circle.name
selected_url = station_circle.get_url_by_company_name()


def download_response(url):
    req = requests.get(url, headers)
    if req.ok:
        req_status = req.status_code
        write_log(name, f"status code: {req_status}")
        soup = BeautifulSoup(req.content, features="lxml")
        return soup
    else:
        req_status = req.status_code
        return write_log(name, f"status code: {req_status}")


posts =[]           
def get_circle_data(soup):
    table_rows = soup.find_all('tr')
    for index in range(1, len(table_rows)): 
        table_row = table_rows[index]
        try:
            fuel_updated_date = soup.find('p', class_='last-updated').text[-19::]  
            company_row_split = table_row.text.split(' ')[1:5]
            company = ' '.join(company_row_split).rstrip()   
            adress = table_row.find('small').text
            name_D = table_row.select("td[data-id]")[0]["data-id"].split("-")[-1] 
            price_D = table_row.select("td[data-id]")[0].text
            name_A95 = table_row.select("td[data-id]")[1]["data-id"].split("-")[-1]
            price_A95 = table_row.select("td[data-id]")[1].text 
        except (AttributeError, IndexError) as err:
            write_log(name, f"fuel_updated_date error: {err}")
        
        station = Station(company, adress, fuel_updated_date, name_D, price_D, name_A95, price_A95)
        data = station.data_to_dict()
        posts.append(data)
                
     
def try_get_responce():
    try:
        soup_response = download_response(selected_url)
        get_circle_data(soup_response)
    except Exception as e:
        exc_err = e
        write_log(name, f"soup_response error: {exc_err}")
    

def data_to_json():
    try_get_responce()
    return create_json(posts, 'fuel.json')


print(data_to_json())
