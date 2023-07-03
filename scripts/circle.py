from station import Station
from logs import Logger
from utils.file import create_json
from app import FuelCrawler

# class Circle:
#     def __init__(self) -> None:
#         self.json_file = 'fuel.json'
#         self.posts = []

posts =[]           
def get_circle_data(soup):
        table_rows = soup.find_all('tr')
        for index in range(1, len(table_rows)): 
            table_row = table_rows[index]
            try:
                fuel_updated_date = soup.find('p', class_='last-updated').text[-19::]  
            except AttributeError as ae:
                fuel_updated_date = None
            try: 
                company_row_split = table_row.text.split(' ')[1:5]
                company = ' '.join(company_row_split).rstrip()   
            except AttributeError as ae:
                company = None
            try:   
                adress = table_row.find('small').text
            except AttributeError as ae:
                adress = None
            try:  
                name_D = table_row.select("td[data-id]")[0]["data-id"].split("-")[-1] 
            except IndexError as ie:
                name_D = None
            try:
                price_D = table_row.select("td[data-id]")[0].text
            except IndexError as ie:
                price_D = None
            try:
                name_A95 = table_row.select("td[data-id]")[1]["data-id"].split("-")[-1]
            except IndexError as ie:
                name_A95 = None
            try:
                price_A95 = table_row.select("td[data-id]")[1].text 
            except IndexError as ie:
                price_A95 = None
            
            station = Station(company, adress, fuel_updated_date, name_D, price_D, name_A95, price_A95)
            data = station.data_to_dict()
            posts.append(data)
            
        return posts
    
get_circle_data(FuelCrawler.download_response())  

# if __name__ == '__main__':
#     circle_station = Circle()
#     crawler = FuelCrawler('Circle')
#     circle_station.get_circle_data(crawler.try_get_responce())
#     # circle_station.get_circle_data(crawler.download_response())
    
#     # logger = Logger(crawler)
#     # logger.status_log()
#     circle_station.data_to_json()