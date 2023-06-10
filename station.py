
class Station:
    def __init__(self, company, adress, fuel_updated_date, name_D, price_D, name_A95, price_A95):
        self.name = company,
        self.adress = adress,
        self.fuel_updated_date = fuel_updated_date,
        self.name_D = name_D,
        self.price_D = price_D,
        self.name_A95 = name_A95,
        self.price_A95 = price_A95
        
  
        self.data = {
            'company': self.company,
            ' adress': self.adress,
            'fuel_updated_date': self.fuel_updated_date, 
            self.name_D: self.price_D,
            self.name_A95: self.price_A95       
        }
        
    def print_data(self):
        print(f"{self.company}, {self.adress}, {self.fuel_updated_date}, {self.name_D}: {self.price_D}, {self.name_A95}: {self.price_A95}") 
        
   
  
  