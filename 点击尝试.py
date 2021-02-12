from selenium import webdriver
import time
import pandas as pd



df=pd.DataFrame(columns=['timer','title','source','content'])

bro=webdriver.Chrome()
bro.get(url='https://news.cnstock.com/news/sns_jg/index.html')
time.sleep(2)


for i in range(1000):
    if i <1000:
        time.sleep(1)
        bro.find_element_by_id('j_more_btn').click()
        bro.find_element_by_id('j_more_btn').click()

handle = bro.current_window_handle

li_list=bro.find_elements_by_xpath('//li/h2/a')
for li in li_list:
    link=li.click()

    handles = bro.window_handles
    for newhandle in handles:
        # 筛选新打开的窗口B
        if newhandle != handle:

            bro.switch_to.window(newhandle)

            # 在新打开的窗口B中操作
            title=bro.find_element_by_xpath('.//h1[@class="title"]').text
            timer=bro.find_element_by_xpath('.//span[@class="timer"]').text
            source=bro.find_element_by_xpath('.//span[@class="source"]').text
            elements = bro.find_element_by_xpath('.//div[@class="content"]')
            contents = elements.find_elements_by_xpath('.//p')
            contain = ''
            for content in contents:
                text = content.get_attribute('innerText')
                contain = contain + ' ' + text
            s = pd.Series([timer, title, source, contain], index=['timer', 'title', 'source', 'content'])
            df = df.append(s, ignore_index=True)


            bro.close()
            bro.switch_to.window(handle)

df.to_excel('C:\\Users\Administrator\Desktop\\完结.xlsx')














