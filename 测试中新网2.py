from selenium import webdriver
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import time
df=pd.DataFrame(columns=['timer_source','title','content'])
bro=webdriver.Chrome()
bro.get(url='http://www.chinanews.com/sh/2021/01-25/9395449.shtml')







try:
    # 在新打开的窗口B中操作
    title = bro.find_element_by_xpath('.//h1[@style="display:block; position:relative; clear:both"]').text
    timer_source = bro.find_element_by_xpath('.//div[@class="left-t"]').text

    elements = bro.find_element_by_xpath('.//div[@class="left_zw"]')
    contents = elements.find_elements_by_xpath('.//p')


    contain = ''
    for content in contents:
        text = content.get_attribute('innerText')
        contain = contain + ' ' + text
    s = pd.Series([timer_source, title, contain], index=['timer_source', 'title', 'content'])
    df = df.append(s, ignore_index=True)
except NoSuchElementException:
    pass

bro.close()



df.to_excel('C:\\Users\Administrator\Desktop\\测试中新网2.xlsx')