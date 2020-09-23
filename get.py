import bs4
from bs4 import BeautifulSoup
import requests
from pip._vendor import chardet
r = requests.get('http://jx.ah.gov.cn/')
data = r.content
soup = BeautifulSoup(data,'html.parser',from_encoding='utf-8')
# for child in soup.stripped_strings:
#     print((repr(child)))
# for child in soup.head.meta.next_sibling:
#   print(child)
# for s in soup.find_all('link'):
#     print(s)
for s in soup.body.stripped_strings:
    print(repr(s))

