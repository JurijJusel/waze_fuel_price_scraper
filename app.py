from manager import Manager
from script_logs import Script_log
from run_scripts import Scripts
from data_to_db import connection, run_create_tables, json_data_to_db
from constants import json_fuel_file_path

class FuelCrawler:
    def __init__(self):
        pass
       
    def run(self, script_obj):
        script_obj.run_scripts()
   
                                 
if __name__ == '__main__':
    crawler = FuelCrawler()
    script_log = Script_log()
    scripts = Scripts()
    
    manager = Manager(status=True)
    if manager.is_activate():
        crawler.run(scripts)    

        run_create_tables(connection)
        # json_data_to_db(connection, json_fuel_file_path)
        print(script_log.__str__())
  
    