class Station:
    def __init__(self, company, address, fuel_updated_date, name_D, price_D, name_A95, price_A95):
        self.company = company
        self.address = address
        self.fuel_updated_date = fuel_updated_date
        self.name_D = name_D
        self.price_D = price_D
        self.name_A95 = name_A95
        self.price_A95 = price_A95
               
    def data_to_dict(self):
        return {
            'company': self.company,
            'address': self.address,
            'fuel_updated_date': self.fuel_updated_date,
            self.name_D: self.price_D,
            self.name_A95: self.price_A95  
            }

    def __str__(self):
        return f"company: {self.company}, address: {self.address}, fuel_updated_date: {self.fuel_updated_date}, {self.name_D}: {self.price_D}, {self.name_A95}: {self.price_A95}" 