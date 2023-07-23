from app import FuelCrawler
class Manager:
    def __init__(self, status=True) -> None:
        self.status = status
        print("manager init method")
    
    def activate_scripts(self):
        print("running def activate_scripts")
        if self.status:
            print("run")
            FuelCrawler.run()
        else:
            print("not activate_scripts from manager")
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
            
# from run_scripts import run_scripts
# from app import *
# crawler = FuelCrawler("Circle")           
            
    #     n = input("iveskit: '1' - ")
    #     if n == "1":
    #         print("input ok activate_scripts from manager")
    #         return 
    #     else:
    #         print("else activate_scripts from manager not run")
          
    # def __str__(self):
    #     return f"self"
 
 
 
 
 
 
 
 
 
 
 
 
        
# if __name__ == '__main__':  
#     print("manager class") 
#     crawler = FuelCrawler()
#     manager = Manager()
#     manager.activate_scripts()   
# else:

#     print("else from manager")
    
    
    
    
    
#     n = input('input:"s"')
#     if n == 's':
#         manager = Manager
#         manager.activate_scripts()
#         print('else from manager')
#     else:
#         print("nesuveike")
# run = run_scripts()
    # crawler = FuelCrawler(name="Circle")
# print(crawler.req_status)
# name = crawler.get_url_by_company_name()
# print(name)
# x = manager