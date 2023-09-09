import requests
from bs4 import BeautifulSoup
from constants import headers, url, json_fuel_file_path
from station import Station
from utils.file import create_json
from script_logs import Script_log

script_log = Script_log()
company_name = 'Viada'
city = 'Vilnius'
params = {'brand': company_name, 'city': city}


def download_response(url, params): 
    try:
        req = requests.get(url, headers=headers)
        if req.ok:
            soup = BeautifulSoup(req.content, features="lxml")
            script_log.write_log(company_name, f"status code: {req.status_code}")
            return soup
        else:
            script_log.write_log(company_name, f"status code: {req.status_code}")
            return None
    except (Exception, ConnectionError) as e: 
        script_log.write_log(company_name, f"download_responce: {e}")
        print(company_name, f"download_responce error: {e}")


def get_viada_data(soup):
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
            script_log.write_log(company_name, f"error in def get_circle_data: {err}")          

        station = Station(company, address, fuel_updated_date, name_D, price_D, name_A95, price_A95)
        data = station.data_to_dict()
        posts.append(data)

    return posts


response = download_response(url, params)
if response:
    data = get_viada_data(response)
    result_json = create_json(data, json_fuel_file_path)
    script_log.write_log(company_name, result_json) 
    print(f"result data of {company_name} company, {result_json}")
else:
    script_log.write_log(company_name, f"the request failed")
    print(f"{company_name} company, response failed")