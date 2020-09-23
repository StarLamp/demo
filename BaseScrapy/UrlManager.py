class UrlManager(object):
    def __init__(self):
        self.new_urls=set()#未爬取的url地址
        self.old_urls = set()#已爬取的url地址
    def has_new_url(self):
        #判断是否有未爬取的url地址 return
        return self.new_urls_size()!=0
    def get_new_url(self):
        #获取一个未爬取的URL地址
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
    def add_new_url(self,url):
        #将