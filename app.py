from urls import urls
from run_scripts import run_scripts

class FuelCrawler:
    def __init__(self, name):
        self.name = name
        self.fuel_updated_date = None
        self.company = None
        self.adress = None
        self.name_D = None
        self.price_D = None
        self.name_A95 = None
        self.price_A95 = None
        self.req_status = None
        self.exc_err = None
        self.url = None
        
    def get_url_by_company_name(self):
        selected_url = next(item['url'] for item in urls if item['name'] == self.name)
        return selected_url
    
                  
if __name__ == '__main__':
    run_scripts()
    
    
    
    # station_c = FuelCrawler(name='Circle')
    # selected_url = station.get_url_by_company_name()
    # station.get_url_by_company_name()
    # print(selected_url)
    # station.data_to_json() 
    # logger = Logger(station)
    # logger.status_log()


 # def download_response(self):
    #     req = requests.get(self.url, self.headers)
    #     if req.ok:
    #         self.status = req.status_code
    #         soup = BeautifulSoup(req.content, features="lxml")
    #         return soup
    #     else:
    #         self.status = req.status_code
    
      
    # def get_data(self, soup):
    #     table_rows = soup.find_all('tr')
    #     for index in range(1, len(table_rows)): 
    #         table_row = table_rows[index]
    #         try:
    #             self.fuel_updated_date = soup.find('p', class_='last-updated').text[-19::]  
    #         except AttributeError as ae:
    #             self.fuel_updated_date = None
    #         try: 
    #             company_row_split = table_row.text.split(' ')[1:5]
    #             self.company = ' '.join(company_row_split).rstrip()   
    #         except AttributeError as ae:
    #             self.company = None
    #         try:   
    #             self.adress = table_row.find('small').text
    #         except AttributeError as ae:
    #             self.adress = None
    #         try:  
    #             self.name_D = table_row.select("td[data-id]")[0]["data-id"].split("-")[-1] 
    #         except IndexError as ie:
    #             self.name_D = None
    #         try:
    #             self.price_D = table_row.select("td[data-id]")[0].text
    #         except IndexError as ie:
    #             self.price_D = None
    #         try:
    #             self.name_A95 = table_row.select("td[data-id]")[1]["data-id"].split("-")[-1]
    #         except IndexError as ie:
    #              self.name_A95 = None
    #         try:
    #             self.price_A95 = table_row.select("td[data-id]")[1].text 
    #         except IndexError as ie:
    #             self.price_A95 = None
            
    #         station = Station(self.company, self.adress, self.fuel_updated_date, self.name_D, self.price_D, self.name_A95, self.price_A95)
    #         data = station.data_to_dict()
    #         self.posts.append(data)
            
        # return self.posts
    
    # def try_get_responce(self):
    #     try:
    #         soup_response = self.download_response()
    #         # return self.get_data(soup_response)
    #         return soup_response
        
    #     except requests.exceptions.ConnectionError as rqe:
    #         # print("Error get responce exception info:", rqe)
    #         self.resp_err = rqe
            
               
    # def data_to_json(self):
    #     self.get_url_by_company_name()
    #     create_json(self.posts, self.json_file )
    
        
