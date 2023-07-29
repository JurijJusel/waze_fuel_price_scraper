fuel_station_urls = [
    {'name': 'Circle', 'url': 'https://gas.didnt.work/?country=lt&brand=Circle+K&city=Vilnius'},
    {'name': 'Viada', 'url': 'https://gas.didnt.work/?country=lt&brand=Viada&city=Vilnius'},
    {'name': 'Neste', 'url': 'https://gas.didnt.work/?country=lt&brand=Neste&city=Vilnius'},
    {'name': 'Emsi', 'url': 'https://gas.didnt.work/?country=lt&brand=EMSI&city=Vilnius'},
    {'name': 'Jozita', 'url': 'https://gas.didnt.work/?country=lt&brand=Jozita&city=Vilnius'},
    {'name': 'Orlen', 'url': 'https://gas.didnt.work/?country=lt&brand=Orlen&city=Vilnius'},
    {'name': 'Baltic_Petroleum', 'url': 'https://gas.didnt.work/?country=lt&brand=Baltic+Petroleum&city=Vilnius'},
    {'name': 'Alausa', 'url': 'https://gas.didnt.work/?country=lt&brand=Alau%C5%A1a&city=Vilnius'},
    {'name': 'Kvistija', "url": 'https://gas.didnt.work/?country=lt&brand=Kvistija&city=Vilnius'},
    {'name': 'Statela', 'url': 'https://gas.didnt.work/?country=lt&brand=Stateta&city=Vilnius'},
    {'name': 'Ecoil', 'url': 'https://gas.didnt.work/?country=lt&brand=Ecoil&city=Vilnius'},
    {'name': 'Saurida', 'url': 'https://gas.didnt.work/?country=lt&brand=Saurida&city=Vilnius'},
    {'name': 'Takuras', 'url': 'https://gas.didnt.work/?country=lt&brand=Takuras&city=Vilnius'},
    {'name': 'Stateta', 'url': 'https://gas.didnt.work/?country=lt&brand=Stateta&city=Vilnius'},
    {'name': 'Skulas', 'url': 'https://gas.didnt.work/?country=lt&brand=Skulas&city=Vilnius'},    
]

def get_url_by_company_name(self):
        selected_url = next(item['url'] for item in fuel_station_urls if item['name'] == self.name)
        return selected_url
#TODO kurioje vietoj sio failo turinys yra naudojamas?