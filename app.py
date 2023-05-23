from bs4 import BeautifulSoup
# import requests
from utils.file import create_json
from urllib.request import Request, urlopen
import httpx
from parsel import Selector

# url = 'https://www.glassdoor.com/member/home/index.htm'
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}

response = httpx.get(
    'https://www.glassdoor.com/Reviews/index.htm?overall_rating_low=3.5&page=1&filterType=RATING_OVERALL',
    follow_redirects=True
)

selector = Selector(response.text).get()
# meta_tags = selector.get()
print(selector)
    

# req = Request(url=url, headers=headers)
# webpage = urlopen(req).read()
# print(webpage)

# # def download_meta():
# meta_data=[]
# # req = requests.get(url, headers=headers)
# # soup = BeautifulSoup(req.content, features="lxml")
# soup = BeautifulSoup(selector, 'html.parser')
# meta_tags = soup.find_all('meta')
#     # print(meta_tags)
#     # meta_data.append(meta_tags)
# for tag in meta_tags: 
#     meta_data.append(tag)
#     print(meta_data) 
# print(req)
# print(meta_data)

# print(create_json(meta_data, 'meta.json'))
    # print(meta_data)



# if __name__ == '__main__':
    
    # pass
