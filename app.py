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
    