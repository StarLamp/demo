import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

baseUrl = 'http://www.baidu.com'
# chrome_option = Options()
# chrome_option.add_argument("--headless")
# brower = webdriver.Chrome(options=chrome_option,)
brower = webdriver.Chrome()
brower.get(baseUrl)
assert '百度' in brower.title
elem = brower.find_element_by_name("wd")
elem.clear()
elem.send_keys("网络信息")
elem.send_keys(Keys.RETURN)
time.sleep(3)
assert "网络信息" in brower.page_source
time.sleep(3)
brower.close()