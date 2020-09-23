import json

import requests
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
headers = {'User-Agent':user_agent}
r = requests.get('http://seputu.com/',headers = headers)
soup = BeautifulSoup(r.text,'lxml')
contents = []
list = []
for mulu in soup.find_all(class_='mulu'):
    h2 = mulu.find('h2')
    if h2!=None:
        h2_title = h2.string
        contents.append({'title':h2_title,'list':list})
    for a in mulu.find_all('a'):
        box_title = a.string
        list.append({'box_title':box_title,'href':a['href']})
with open('json','w') as fp:
    json.dump()