import requests
from bs4 import BeautifulSoup
from constants import headers
from station import Station
from utils.file import create_json
from logs import Script_log


log = Script_log()
name = 'Circle'
fuel_data = 'fuel.json'
url = 'https://gas.didnt.work/?country=lt&brand=Circle+K&city=Vilnius'


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
            log.write_log(name, f"attribute_error in def get_circle_data: {err}")          

        station = Station(company, address, fuel_updated_date, name_D, price_D, name_A95, price_A95)
        data = station.data_to_dict()
        posts.append(data)

    return posts


data = get_circle_data(download_response(url))
print(create_json(data, fuel_data))


# def try_get_responce():
#     global circle_data
#     try:
#         soup_response = download_response(selected_url)
#         circle_data = get_circle_data(soup_response)
#         if circle_data is None:
#             log.write_log(name, f"try_get_responce: {circle_data}")
#             return True
#         else:
#             return circle_data
#     except (Exception, ConnectionError) as e: 
#         log.write_log(name, f"try_get_responce: {e}")
#         return False
        
# def data_to_json():
#     try_get_responce()
#     return create_json(circle_data, 'fuel.json')


# print(data_to_json())
