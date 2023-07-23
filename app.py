from urls import fuel_station_urls
from run_scripts import run_scripts
from manager import Manager

class FuelCrawler:
    def __init__(self, name:str):
        self.name = name
        self.fuel_updated_date = None
        self.company = None
        self.adress = None
        self.name_D = None
        self.price_D = None
        self.name_A95 = None
        self.price_A95 = None
        self.req_status = None
        self.url = None
       
    def get_url_by_company_name(self):
        selected_url = next(item['url'] for item in fuel_station_urls if item['name'] == self.name)
        return selected_url
    
    def run():
        run_s = run_scripts()  
        return run_s
                       
if __name__ == '__main__':
    crawler = FuelCrawler(name='Circle')
    manager = Manager(status=True)

    # manager = Manager(status=True).activate_scripts() #TODO taip geriau nedaryti jei as manager noriu veliau dar panaudoti,o tu ji ensi issaugojes butent kaip obj o i return ikisai runscript,tai manger savyje saugos ne manger obj o run_script return result
    # manager.activate_scripts()
  
    
    
     
# else:
#     # cr = FuelCrawler
#     print("else from app")
    # cr.run
# else:
#     # crawler = FuelCrawler(name='Circle')
#     run_script = run_scripts()
#     print("else")
    
    # crawler = FuelCrawler(name='Circle')
    # run_script = run_scripts()
    

    # crawler = FuelCrawler(name="Circle")
    
    # manager.activate_scripts()
 