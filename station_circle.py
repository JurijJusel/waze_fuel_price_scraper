import time

class Station_circle:
    def __init__(self):#, name):
        pass
       
    
    def circlek_prices(self, soup):
        title = soup.title.string[-8::]
        cards = soup.find_all('div', {'class': 'atom-card'})
        updated_fuel_info = cards[0].text[-26:-5]
        price_miles_95 = cards[0].text[43:48]
        price_miles_plus_95 = cards[1].text[43:48]
        price_miles_D = cards[3].text[43:48]
        price_miles_D_plus = cards[4].text[43:48]

        time_now = time.strftime("%Y-%m-%d %H:%M:%S")
        
        circlek_data = {
            'company': title,
            'scrap_time': time_now,
            'updated_fuel_info': updated_fuel_info, 
            'miles_95': price_miles_95, 
            'miles_plus_95': price_miles_plus_95,
            'miles_D': price_miles_D,
            'miles_D_plus': price_miles_D_plus,
            }      
        return circlek_data
    
    

    
