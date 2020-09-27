import pickle
import hashlib

class UrlManager(object):
    def __init__(self):
        #未爬取
        self.new_urls = self.load_process('new_urls.txt')
        #已爬取
        self.old_urls = self.load_process('old_urls.txt')
    def has_new_url(self):
        '''
        判断是否还有未爬取的url
        :return: 
        '''
        return self.new_urls_size()!=0

    def get_new_url(self):
        '''
        获取一个未爬取的url数据
        :return:
        '''
        new_url = self.new_urls.pop()
        m = hashlib.md5()
        m.update(new_url)
        self.old_urls.add(m.hexdigest()[8:-8])
        return new_url

    def add_new_url(self,url):
        '''
        将新的URL添加到未爬取的
        :param url:
        :return:
        '''
        if url is None:
            return
        m = hashlib.md5()
        m.update(url)
        url_md5 = m.hexdigest()[8:-8]
        if url not in self.new_urls and url_md5 not  in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self,urls):
        '''
        将新的URL添加到未爬取的URl集合中
        :param urls:
        :return:
        '''
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)


    def load_process(self, param):
        pass

    def new_urls_size(self):
        pass

