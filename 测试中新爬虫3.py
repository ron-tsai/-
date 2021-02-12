from selenium import webdriver
import pandas as pd
import time
import random
from selenium.common.exceptions import NoSuchElementException

#防止被屏蔽
from selenium.webdriver import ChromeOptions
option=ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])
bro=webdriver.Chrome(options=option)



df=pd.DataFrame(columns=['timer_source','title','content'])

bro.get(url='http://sou.chinanews.com/search.do')
search_input=bro.find_element_by_id('q')
search_input.send_keys('A股')
bro.find_element_by_xpath('//input[@type="button"]').click()

for i in range(1000):
    print(i)
    if i ==0:
        print('第1页翻页成功')
    else:
        a = random.random()
        time.sleep(a+1)
        while True:
            try:
                bro.find_element_by_xpath('//a[@href="javascript:ongetkey({})"]'.format(i)).click()

                print('第{}页翻页成功'.format(i))
                break
            except NoSuchElementException:
                pass
                bro.back()

                time.sleep(3+a)
                try:
                    bro.find_element_by_xpath('//a[@href="javascript:ongetkey({})"]'.format(i+1)).click()

                except NoSuchElementException:
                    pass
                    time.sleep(1)
                try:
                    bro.find_element_by_xpath('//a[@href="javascript:ongetkey({})"]'.format(i+2)).click()
                except NoSuchElementException:
                    pass
                    time.sleep(1)
                try:
                    bro.find_element_by_xpath('//a[@href="javascript:ongetkey({})"]'.format(i)).click()
                    print('报错解决')

                except NoSuchElementException:
                    pass



