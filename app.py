from manager import Manager
from script_logs import Script_log
from run_scripts import Scripts
from data_to_db import connection, run_create_tables, json_data_to_db
from constants import json_fuel_file_path
import time

class FuelCrawler:
    def __init__(self):
        pass
       
    def run(self, script_obj):
        script_obj.async_run_scripts()

                             
if __name__ == '__main__':
    start_time = time.monotonic()
    crawler = FuelCrawler()
    script_log = Script_log()
    scripts = Scripts()
    
    
    manager = Manager(status=True)
    if manager.is_activate():
        crawler.run(scripts)    

        run_create_tables(connection)
        json_data_to_db(connection, json_fuel_file_path)
        print(script_log.__str__())
        print(f"{time.monotonic() - start_time} stopwatch time")