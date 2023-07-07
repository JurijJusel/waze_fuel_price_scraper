import requests
from bs4 import BeautifulSoup
from constants import headers
from app import FuelCrawler
from station import Station
from utils.file import create_json
from logs_temp import write_log

station_circle = FuelCrawler(name='Circle')
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
        return write_log(f"status code: {req_status}")


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
                
    return posts 
    
     
def try_get_responce():
    try:
        soup_response = download_response(selected_url)
        get_circle_data(soup_response)
        return soup_response 
    except Exception as e:
        exc_err = e
        write_log(name, f"soup_response error: {exc_err}")
    

def data_to_json():
    try_get_responce()
    return create_json(posts, 'fuel.json')


print(data_to_json())






#  posts =[]           
# # error_messages = []
# def get_circle_data(soup):
#     table_rows = soup.find_all('tr')
#     for index in range(1, len(table_rows)): 
#         table_row = table_rows[index]
#         try:
#             fuel_updated_date = soup.find('p', class_='last-updated').text[-19::]  
#         except AttributeError as ae:
#             # fuel_updated_date = None
#             write_log(name, f"fuel_updated_date error: {ae}")
#             # error_messages.append(f"fuel_updated_date error: {ae}")     
#         try: 
#             company_row_split = table_row.text.split(' ')[1:5]
#             company = ' '.join(company_row_split).rstrip()   
#         except AttributeError as ae:
#             # company = None
#             write_log(name, f"company error: {ae}")
#             # error_messages.append(f"company error: {ae}")
#         try:   
#             adress = table_row.find('small').text
#         except AttributeError as ae:
#             # adress = None
#             write_log(name, f"adress error: {ae}")
#             # error_messages.append(f"adress error: {ae}")
#         try:  
#             name_D = table_row.select("td[data-id]")[0]["data-id"].split("-")[-1] 
#         except IndexError as ie:
#             # name_D = None
#             write_log(name, f"name_D error: {ie}")
#             # error_messages.append(f"name_D error: {ie}")
#         try:
#             price_D = table_row.select("td[data-id]")[0].text
#         except IndexError as ie:
#             # price_D = None
#             write_log(name, f"price_D error: {ie}")
#             # error_messages.append(f"price_D error: {ie}")
#         try:
#             name_A95 = table_row.select("td[data-id]")[1]["data-id"].split("-")[-1]
#         except IndexError as ie:
#             # name_A95 = None
#             write_log(name, f"name_A9 error: {ie}")
#         try:
#             price_A95 = table_row.select("td[data-id]")[1].text 
#         except IndexError as ie:
#             # price_A95 = None
#             write_log(name, f"price_A95 error: {ie}")
        
#         station = Station(company, adress, fuel_updated_date, name_D, price_D, name_A95, price_A95)
#         data = station.data_to_dict()
#         posts.append(data)
    
    # if error_messages:
    #     for error in error_messages:
    #         write_log(name, error)
    # else:
    #     write_log(name, "No errors encountered")
                
    # return posts
    


# # if __name__ == '__main__':
# #     circle_station = Circle()
# #     crawler = FuelCrawler('Circle')
# #     circle_station.get_circle_data(crawler.try_get_responce())
# #     # circle_station.get_circle_data(crawler.download_response())
    
# #     # logger = Logger(crawler)
# #     # logger.status_log()
# #     circle_station.data_to_json()
# logger.status_log()
# logger.write_status_log(station_circle.req_status)