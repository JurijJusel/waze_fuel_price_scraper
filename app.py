from bs4 import BeautifulSoup
import requests
from utils.file import create_json


url = 'https://www.glassdoor.com/member/home/index.htm'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}


# def download_meta():
meta_data=[]
req = requests.get(url, headers=headers)
# soup = BeautifulSoup(req.content, features="lxml")
soup = BeautifulSoup(req.content, 'html.parser')
# meta_tags = soup.find_all('meta')
    # print(meta_tags)
    # meta_data.append(meta_tags)
# for tag in meta_tags: 
#     meta_data.append(tag.attrs)
#     print(meta_data) 
print(req)
# print(meta_tags)

# print(create_json(meta_data, 'meta.json'))
    # print(meta_data)



# if __name__ == '__main__':
    
    # pass
