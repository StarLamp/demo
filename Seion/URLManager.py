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


    def load_process(self, param):
        pass

    def new_urls_size(self):
        pass

