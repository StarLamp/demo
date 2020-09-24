import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup

class HtmlParser(object):
    def parser(self,page_url,html_cont):
        #解析网页内容，抽取URL和数据
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self.get_new_data(page_url,soup)
        return new_urls,new_data

    def _get_new_urls(self, page_url, soup):
        '''抽取新的URL集合: param
        page_url: 下载页面的URL:param
        soup: soup:return: 返回新的URL集合
        '''
        new_urls = set()
        # 抽取符合要求的a标记
        links = soup.find_all('a')
        for link in links:
            # 提取href属性
            new_url = link['href']
            new_full_url = urlparse(page_url,new_url)
            new_urls.add(new_full_url)
    def get_new_data(self, page_url, soup):
        pass
