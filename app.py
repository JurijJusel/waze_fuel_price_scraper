# from bs4 import BeautifulSoup
import requests
# from utils.file import create_json
# from urllib.request import Request, urlopen
# import httpx
# from parsel import Selector
# import urllib3
# from fake_useragent import UserAgent


url = 'https://www.glassdoor.com/member/home/index.htm'
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36'}
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13'}


# http = urllib3.PoolManager()
# resp = http.request('GET', url)
# print(resp.status)
# print(resp.data)
# ua = UserAgent()
# print(ua.chrome)


req = requests.get(url, headers=headers)
# selector = Selector(text=req)
# print(selector.xpath('//title/text()').getall())
print(req.status_code)


# req = Request(url, headers=headers)
# print(req)
# web = urlopen(req).read()
# response = httpx.get(url)  #, follow_redirects=True)
# print(response.status_code)
# selector = Selector(response.text)
# meta_tags = selector.get()
# print(selector)
# html_selector = Selector(text=selector)
# g = html_selector.xpath('//head/text()').get()
# print(g)
# h = selector.css('meta')
# for i in h:
#     print(i)
# req = Request(url=url, headers=headers)
# webpage = urlopen(req).read()
# print(webpage)

# # def download_meta():
# meta_data=[]
# # req = requests.get(url, headers=headers)
# soup = BeautifulSoup(req, features="lxml")

# soup = BeautifulSoup(selector, 'html.parser')
# meta_tags = soup.find_all('meta')
# print(meta_tags)
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
