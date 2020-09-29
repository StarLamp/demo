from multiprocessing.managers import BaseManager
from Seion.HtmlDownloader import HtmlDownloader
from Seion.HtmlParser import HtmlParser

class SpiderWork(object):
    def __init__(self):
        #初始化节点
        #获取Queue的方法结果
        server_addr = '127.0.0.1'
        print('Connect to server %s...' % server_addr)
        self.m = BaseManager(address=(server_addr,8001),authkey='python')

        self.m.connect()

        #获取Queue对象
        self.tasks = self.m.get_task_queue()
        self.result = self.m.get_result_queue()

        #初始化网页下载器和解析器

        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()

        print('init finish')

    def crawl(self):
        while (True):
            try:
                if not self.tasks.empty():
                    url = self.tasks.get()
                    if url =='end':
                        print('控制节点通知爬虫节点停止工作...')
                        # 接着通知其他节点停止工作
                        self.result.put({'new_urls':'end','data':'end'})
                        return
                    print ('爬虫节点正在解析:%s' % url.encode('utf-8'))
                    content = self.downloader.download(url)
                    new_urls,data = self.parser.parser(url,content)
                    self.result.put({"new_urls":new_urls,"data":data})
            except EOFError as e:
                print ("连接工作节点失败")
                return
            except Exception as e:
                print (e)
                print ('Crawl  fail')

if __name__=="__main__":
    spider = SpiderWork()
    spider.crawl()
