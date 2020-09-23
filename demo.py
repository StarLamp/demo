from urllib.request import urlretrieve
from lxml import etree
import requests
def Schedule(blocknum,blocksize,totalsize):
    #blocknum：已经下载的数据块
    #blocksize:数据块的大小
    #totalsize:远程文件的大小
    per = 100.0*blocknum*blocksize/totalsize
    if  per>100 :
        per = 100
        print('当前下载进度:%d'%per)
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
headers = {'User-Agent':user_agent}
r = requests.get('https://www.ivsky.com/tupian/ziranfengguang/',headers=headers)
html = etree.HTML(r.text)
img_urls = html.xpath('.//img/@src')
i = 0
for img_url in img_urls:
    urlretrieve("http:"+img_url,'img'+str(i)+'.jpg',Schedule)
    i+=1


