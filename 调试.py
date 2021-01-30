from selenium import webdriver

import pandas as pd



df=pd.DataFrame(columns=['timer','title','source','content'])

driver=webdriver.Chrome()
driver.get(url='https://news.cnstock.com/news/sns_jg/index.html')


handle = driver.current_window_handle

li_list=driver.find_elements_by_xpath('//li/h2/a')
for li in li_list:
    link=li.click()

    handles = driver.window_handles
    for newhandle in handles:
        # 筛选新打开的窗口B
        if newhandle != handle:

            driver.switch_to.window(newhandle)

            # 在新打开的窗口B中操作
            title=driver.find_element_by_xpath('.//h1[@class="title"]').text
            timer=driver.find_element_by_xpath('.//span[@class="timer"]').text
            source=driver.find_element_by_xpath('.//span[@class="source"]').text
            elements=driver.find_element_by_xpath('.//div[@class="content"]')
            contents=elements.find_elements_by_xpath('.//p')
            contain=''
            for content in contents:
                text=content.get_attribute('innerText')
                contain=contain+' '+text
            s=pd.Series([timer,title,source,contain],index=['timer','title','source','content'])
            df=df.append(s,ignore_index=True)


            driver.close()
            driver.switch_to.window(handle)

df.to_excel('C:\\Users\Administrator\Desktop\\调试.xlsx')