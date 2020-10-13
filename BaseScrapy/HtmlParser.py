import json
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
        new_data = self._get_new_data(page_url,soup)
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
        return new_urls

    def _get_new_data(self,page_url,soup):
        '''抽取有效数据
        '''
        data = {}
        data['url'] = page_url
        title = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        data['title'] = title.get_text()
        summary = soup.find('div',class_='lemma-summary')
        # 获取tag中包含的所有文本内容，包括子孙tag中的内容,并将结果作为Unicode字符串返回
        data['summary']=summary.get_text()
        return data

    def parser_url(self,page_url,response):
        pattern = re.compile('http://movie.mtime.com/(\d+)')
        urls = pattern.findall(response)
        if urls is not None:
            #将urls进行去重
            return list(set(urls))
        else:
            return None

    def pareser_json(self,page_url,response):
        '''
        解析响应
        :param page_url:
        :param response:
        :return:
        '''

        pattern = re.compile('=(.*);')
        result = pattern.findall(response)
        if result is not None:
            value = json.loads(result)
            try:
                isRelease = value.get('value').get('isRelease')
            except Exception as e :
                print(e)
                return None
            if isRelease:
                if value.get('value').get('hotValue') is None:
                    return self._parser_release(page_url,value)
                else:
                    return self._parser_no_release(page_url,value,isRelease = 2)

    def _parser_release(self, page_url, value):
        '''
        解析已经上映的影片
        :param page_url:电影链接
        :param value:json数据
        :return: 
        '''
        try:
            isRlease = 1
            movieRating = value.get('value').get('movieRating')
            boxOffice = value.get('value').get('boxOffice')
            moiveTitle = value.get('value').get('movieTitle')

            RPictureFinal = movieRating.get('RPictureFinal')
            RStoryFinal = movieRating.get('RStoryFinal')
            RDirectorFinal = movieRating.get('RDirectorFinal')
            ROtherFinal = movieRating.get('ROtherFinal')
            RatingFinal = movieRating.get('RatingFinal')
            MovieId =  movieRating.get('MovieId')
            Usercount = movieRating.get('Usercount')
            AttitudeCount =  movieRating.get('AttitudeCount')
            TotalBoxOffice =  boxOffice.get('TotalBoxOffice')
            TotalBoxOfficeUnit =  boxOffice.get('TotalBoxOfficeUnit')
            TodayBoxOffice =  boxOffice.get('TodayBoxOffice')
            TodayBoxOfficeUnit =  boxOffice.get('TodayBoxOfficeUnit')

            ShowDays = boxOffice.get('ShowDays')
            try:
                Rank = boxOffice.get('Rank')
            except Exception as e :
                print(e)
                return None
                
        except Exception as e:
            print(e)
            return None

    def _parser_no_release(self, page_url, value, isRelease):
        pass
