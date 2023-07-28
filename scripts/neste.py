import requests
from bs4 import BeautifulSoup
from constants import headers
from app import FuelCrawler
from station import Station
from utils.file import create_json
from logs import Script_log


log = Script_log()
station_neste = FuelCrawler(name='Neste')
name = station_neste.name
selected_url = station_neste.get_url_by_company_name()
fuel_data = 'fuel.json'


def download_response(url):
    try:
        req = requests.get(url, headers=headers)
    except (Exception, ConnectionError) as e: 
        log.write_log(name, f"try_get_responce: {e}")
        return False
    if req.ok:
        req_status = req.status_code
        log.write_log(name, f"status code: {req_status}")
        soup = BeautifulSoup(req.content, features="lxml")
        return soup
    else:
        req_status = req.status_code
        log.write_log(name, f"status code: {req_status}")
        return False


def get_neste_data(soup):
    posts = []
    table_rows = soup.find_all('tr')
    for index in range(1, len(table_rows)):
        table_row = table_rows[index]
        try:
            fuel_updated_date = soup.find('p', class_='last-updated').text[-19::]
            company_row_split = table_row.text.split(' ')[1:5]
            company = ' '.join(company_row_split).rstrip()
            address = table_row.find('small').text
            name_D = table_row.select("td[data-id]")[0]["data-id"].split("-")[-1]
            price_D = table_row.select("td[data-id]")[0].text
            name_A95 = table_row.select("td[data-id]")[1]["data-id"].split("-")[-1]
            price_A95 = table_row.select("td[data-id]")[1].text
        except (AttributeError, IndexError) as err:
            log.write_log(name, f"attribute_error in def get_circle_data: {err}")
           

        station = Station(company, address, fuel_updated_date, name_D, price_D, name_A95, price_A95)
        data = station.data_to_dict()
        posts.append(data)

    return posts


data = get_neste_data(download_response(selected_url))
print(create_json(data, fuel_data))
