from manager import Manager
from logs import Script_log
from run_scripts import Scripts

class FuelCrawler:
    def __init__(self):
        pass
       
    def run(self, script_obj):
        script_obj.run_scripts()
        script_obj.print_scripts()
     
                            
if __name__ == '__main__':
    crawler = FuelCrawler()
    script_log = Script_log()
    scripts = Scripts()
    
    manager = Manager(status=True)
    if manager.is_activate():
        crawler.run(scripts)
    
    script_log.print_logs_obj_count()
  
    