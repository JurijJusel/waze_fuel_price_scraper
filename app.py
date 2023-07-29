from run_scripts import run_scripts
from manager import Manager

class FuelCrawler:
    def __init__(self):#TODO station ir fuel-crawler ju init identiski,reiktu vienu  atsikratyti
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
       