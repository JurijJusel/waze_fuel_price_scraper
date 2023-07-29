from run_scripts import run_scripts
from manager import Manager

class FuelCrawler:
    def __init__(self):#, name:str):
        # self.name = name
        self.fuel_updated_date = None
        self.company = None
        self.adress = None
        self.name_D = None
        self.price_D = None
        self.name_A95 = None
        self.price_A95 = None
        self.req_status = None
        self.url = None
    
    def run(self):
        run_s = run_scripts()  
        return run_s
                       
if __name__ == '__main__':
    crawler = FuelCrawler()
    manager = Manager(status=True)
    if manager.is_activate():
        crawler.run()
       
    # manager = Manager(status=True).activate_scripts() #TODO taip
    # geriau nedaryti jei as manager noriu veliau dar panaudoti,o 
    # tu ji ensi issaugojes butent kaip obj o i return ikisai \
        # runscript,tai manger savyje saugos ne manger obj o 
        # run_script return result
    # manager.activate_scripts()
  