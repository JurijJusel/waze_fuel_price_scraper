from bs4 import BeautifulSoup
import requests
import time
from urls import urls
from utils.file import create_json

time_now = time.strftime("%Y-%m-%d %H:%M:%S")

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}

req = requests.get(urls[1], headers=headers).text
soup = BeautifulSoup(req, features="lxml")

title = soup.title.string[-8::]
cards = soup.find_all('div', {'class': 'atom-card'})
updated_fuel_info = cards[0].text[139:160]
miles_95 = cards[0].text[43:48]
miles_plus_95 = cards[1].text[43:48]
miles_plus_98 = cards[2].text[43:48]
miles_D = cards[3].text[43:48]
miles_D_plus = cards[4].text[43:48]
dz = cards[5].text[43:48]
lpg = cards[6].text[43:48]
ad_blue = cards[7].text[43:48]


circlek_data = {'scrap_time': time_now,
        'website': title,
        'updated_fuel_info': updated_fuel_info, 
        'fuel_price': {
            'miles_95': miles_95, 
            'miles_plus_95': miles_plus_95,
            'miles_plus_98': miles_plus_98,
            'miles_D': miles_D,
            'miles_D_plus': miles_D_plus,
            'DZ': dz,
            'lpg': lpg,
            'ad_blue': ad_blue
            }
        }

print(circlek_data)

# print(create_json(circlek_data, 'fuel.json'))




# if __name__ == '__main__':
    
    # pass
