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

    def new_urls_size(self):
        '''
        获取未爬取URL集合的大小
        :return:
        '''
        return len(self.new_urls)

    def old_url_size(self):
        '''
        获取已经爬取URL集合的大小
        :return:
        '''
        return len(self.old_urls)


    def save_progress(self,path,data):
        '''
        保持进度
        :param path: 文件路径
        :param data: 数据
        :return:
        '''
        with open(path,'wb') as f:
            pickle.dump(data,f)


    def load_process(self, path):
        '''
        从本地加载文件
        :param path:
        :return:
        '''

        print('文件加载进度：%s' % path)
        try:
            with open(path,'wb') as f:
                tmp = pickle.load(f)
                return tmp
        except:
            print('文件进度失败')

        return set()


