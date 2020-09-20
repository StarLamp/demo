from gevent import monkey;monkey.patch_all()
import gevent
from urllib import request

def run_task(url):
 print('Visit--> %s' % url)
 try:
     response = request.urlopen(url)
     data = response.read()
     print('%s bytes received from %s.' % (len(data),url))
 except Exception as e:
     print(e)
if __name__ == '__main__':
 urls = ['https://www.baidu.com','https://www.taobao.com','https://www.zhihu.com']
 greenlets = [gevent.spawn(run_task,url) for url in urls]
 gevent.joinall(greenlets)

