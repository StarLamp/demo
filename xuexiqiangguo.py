#!usr/bin/python3
# encoding:utf-8

from selenium import webdriver
import time
import random
import re
from bs4 import BeautifulSoup
import json


class Xuexiqiangguo():
    def __init__(self):
        # base_url = "https://www.xuexi.cn/"
        base_url = "https://pc.xuexi.cn/points/login.html?ref=https%3A%2F%2Fwww.xuexi.cn%2F"
        browser = webdriver.Chrome()
        js = 'var q=document.documentElement.scrollTop=800'
        self.base_url = base_url
        self.browser = browser
        self.js = js

    def login_xuexi(self):
        self.browser.get(self.base_url)
        time.sleep(3)
        self.browser.execute_script(self.js)
        time.sleep(30)
        # self.browser.find_element_by_xpath(
        #     '//*[@id="root"]/div/div/section/div/div/div/div/div[4]/section/div[4]').click()
        # time.sleep(3)

    def get_ponits(self):
        points_url = 'https://pc.xuexi.cn/points/my-points.html'
        self.browser.get(points_url)
        time.sleep(3)

        login_point_text = self.browser.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]').text
        login_point = re.findall('\d*\d', login_point_text)
        print(login_point)
        self.login_point = login_point[0]
        self.login_point = login_point[1]

        read_point_text = self.browser.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div/div[3]/div[2]/div[2]/div[3]/div[1]/div[2]').text
        read_point = re.findall('\d*\d', read_point_text)
        print(read_point)
        self.read_point = read_point[0]
        self.read_points = read_point[1]

        watch_point_text = self.browser.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div/div[3]/div[2]/div[3]/div[2]/div[1]/div[2]').text
        watch_point = re.findall('\d*\d', watch_point_text)
        print(watch_point)
        self.watch_point = watch_point[0]
        self.watch_points = watch_point[1]

        watch_time_point_text = self.browser.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div/div[3]/div[2]/div[4]/div[2]/div[1]/div[2]').text
        watch_time_point = re.findall('\d*\d', watch_time_point_text)
        print(watch_time_point)
        self.watch_time_point = watch_time_point[0]
        self.watch_time_points = watch_time_point[1]

        answer_day_point_text = self.browser.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div/div[3]/div[2]/div[5]/div[2]/div[1]/div[2]').text
        answer_day_point = re.findall('\d*\d', answer_day_point_text)
        print(answer_day_point)
        self.answer_day_point = answer_day_point[0]
        self.answer_day_points = answer_day_point[1]

        answer_week_point_text = self.browser.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div/div[3]/div[2]/div[6]/div[2]/div[1]/div[2]').text
        answer_week_point = re.findall('\d*\d', answer_week_point_text)
        print(answer_week_point)
        self.answer_week_point = answer_week_point[0]
        self.answer_week_points = answer_week_point[1]

        earmarked_point_text = self.browser.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/div/div[3]/div[2]/div[7]/div[2]/div[1]/div[2]').text
        earmarked_point = re.findall('\d*\d', earmarked_point_text)
        print(earmarked_point)
        self.earmarked_point = earmarked_point[0]
        self.earmarked_points = earmarked_point[1]

    def read_paragraph(self):
        if int(self.read_point) < int(self.read_points):
            need_read = int(self.read_points) - int(self.read_point)
            print('选读文章还需%s分' % need_read)
            points_url = 'https://pc.xuexi.cn/points/my-points.html'
            self.browser.get(points_url)
            time.sleep(3)
            read_url = 'https://www.xuexi.cn/72ac54163d26d6677a80b8e21a776cfa/9a3668c13f6e303932b5e0e100fc248b.html'
            self.browser.get(read_url)
            # html = self.browser.page_source

            for x in range(random.randint(int(need_read / 2 + 1), int(need_read / 2 + 3))):
                time.sleep(3)
                self.browser.switch_to.window(self.browser.window_handles[0])
                num = random.randint(1, 20)
                print(num)
                self.browser.find_element_by_xpath(
                    '//*[@id="root"]/div/div/section/div/div/div/div/div/section/div/div/div/div[1]/div/section/div/div/div/div/div/section/div/div/div/div/div[3]/section/div/div/div/div/div/section/div/div/div[1]/div/div[%s]/div/div/div[1]/span' % num).click()
                time.sleep(3)
                self.browser.switch_to.window(self.browser.window_handles[1])
                count_time=random.uniform(61, 90)
                time.sleep(count_time)
                print(count_time)
                self.browser.close()

                # self.browser.execute(self.js)
                # time.sleep(1)
                # self.browser.back()
                # time.sleep(3)

            # soup = BeautifulSoup(html, 'lxml')
            # cc = soup
            # print(cc.text)
            # res = json.loads(cc.text)
            # print(res)

            # self.browser.execute_script(self.js)
            # self.browser.find_element_by_xpath(
            #     '//*[@id="root"]').click()

        else:
            print('已完成选读文章')

    def watch_video(self):
        if int(self.watch_point) < int(self.watch_points) or int(self.watch_time_point) < int(self.watch_time_points):
            need_watch = int(self.watch_points) - int(self.watch_point) + int(self.watch_time_points) - int(
                self.watch_time_point)
            print('观看视频还需%s分' % need_watch)
            watch_url = 'https://www.xuexi.cn/4426aa87b0b64ac671c96379a3a8bd26/db086044562a57b441c24f2af1c8e101.html#17th9fq5c7l-5'
            self.browser.get(watch_url)
            for x in range(random.randint(int(need_watch / 2 + 1), int(need_watch / 2 + 3))):
                time.sleep(5)
                self.browser.switch_to.window(self.browser.window_handles[0])
                num1 = random.randint(1, 5)
                num2 = random.randint(1, 4)
                print(num1, num2)
                self.browser.find_element_by_xpath(
                    '//*[@id="17th9fq5c7l-5"]/div/div/div/div/div/div/section/div[3]/section/div/div/div[1]/div[%s]/div[%s]/section/div/div/div/div/div[1]/div/div/span/div' % (
                    num1, num2)).click()
                time.sleep(3)
                self.browser.switch_to.window(self.browser.window_handles[1])
                count_time=random.uniform(61, 90)
                print(count_time)
                time.sleep(count_time)
                self.browser.close()
        else:
            print('已完成观看视频')


if __name__ == '__main__':
    xue = Xuexiqiangguo()
    xue.login_xuexi()
    xue.get_ponits()
    xue.read_paragraph()
    xue.watch_video()
