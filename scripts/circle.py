import requests
from bs4 import BeautifulSoup
from constants import headers
from station import Station
from utils.file import create_json
from logs import Script_log

response_log = Script_log()
content_log = Script_log()
name = 'Circle'
fuel_data = 'fuel.json'
url = 'https://gas.didnt.work/?country=lt&brand=Circle+K&city=Vilnius'


def download_response(url):
    try:
        req = requests.get(url, headers=headers)
        if req.ok:
            req_status = req.status_code
            response_log.write_log(name, f"status code: {req_status}")
            soup = BeautifulSoup(req.content, features="lxml")
            return soup
        else:
            req_status = req.status_code
            response_log.write_log(name, f"status code: {req_status}")
            return None
    except (Exception, ConnectionError) as e: 
        response_log.write_log(name, f"download_responce: {e}")
        return None


def get_circle_data(soup):
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
            content_log.write_log(name, f"attribute_error in def get_circle_data: {err}")          
            return None
        
        station = Station(company, address, fuel_updated_date, name_D, price_D, name_A95, price_A95)
        data = station.data_to_dict()
        posts.append(data)

    return posts


response = download_response(url)
if response:
    data = get_circle_data(response)
    result_json = create_json(data, fuel_data)
    print(result_json)                 
else:
    response_log.write_log(name, f"the request failed")
