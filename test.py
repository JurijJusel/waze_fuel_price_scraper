import requests
from bs4 import BeautifulSoup as soup
url = 'https://www.glassdoor.com/member/home/index.htm'
# url = 'https://www.glassdoor.com/Job/new-york-ny-data-scientist-jobs-SRCH_IL.0,11_IC1132348_KO12,26.htm'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
result = requests.get(url, headers=headers)
print(result.status_code)

bsoj = soup(result.content, 'html.parser')
# print(bsoj.find_all('meta'))
