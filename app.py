from bs4 import BeautifulSoup
import requests
import time
from urls import urls
from utils.file import create_json


class FuelCrawler:
    def __init__(self, url):
        self.url = url
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}


    def download_response(self):
        req = requests.get(self.url, headers=self.headers).text
        soup = BeautifulSoup(req, features="lxml")
        return soup


    def circlek_prices(self, soup):
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

        time_now = time.strftime("%Y-%m-%d %H:%M:%S")
        
        circlek_data = {
            'company': title,
            'scrap_time': time_now,
            'updated_fuel_info': updated_fuel_info, 
            'fuel_prices': {
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
        return circlek_data


    def get_prices(self):
        soup_response = self.download_response()
        return self.circlek_prices(soup_response)
    

if __name__ == '__main__':
    station = FuelCrawler(urls[1]['url'])
    print(station.get_prices())
    # print(prices)
    # data_to_json = circlek_prices(download_response(urls[1]['url']))
    # print(create_json(data_to_json, 'fuel.json'))
    # print(circlek_prices(download_response(urls[1]['url'])))
    # print(get_prices(urls[1]['url']))
