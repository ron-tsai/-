from selenium import webdriver
import pandas as pd
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import time
import random
from selenium.webdriver.chrome.options import Options

import requests

chrome_options=Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#防止被屏蔽
from selenium.webdriver import ChromeOptions
option=ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])

option.add_experimental_option('useAutomationExtension', False)
option.add_argument(
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36")

bro=webdriver.Chrome()
with open('C:\\Users\Administrator\Desktop/stealth.min.js') as f:
    js = f.read()

bro.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": js
})


bro.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})




df=pd.DataFrame(columns=['url'])

bro.get(url='http://sou.chinanews.com/search.do')
search_input=bro.find_element_by_id('q')
search_input.send_keys('A股')
bro.find_element_by_xpath('//input[@type="button"]').click()
for i in range(1,490):
    print(i)

    a=random.random()
    time.sleep(a+1)
    li_list = WebDriverWait(bro, 10, 0.5).until(EC.presence_of_all_elements_located((By.XPATH, '//li/a')))
    # li_list=bro.find_elements_by_xpath('//li/a')
    for li in li_list:
        b=li.get_attribute('href')
        s = pd.Series([b], index=['url'])

        df=df.append(s,ignore_index=True)

    try:
        time.sleep(a + 1)

        bro.find_element_by_xpath('//a[@href="javascript:ongetkey({})"]'.format(i)).click()
    except TimeoutException:
        pass
        df.to_excel('C:\\Users\Administrator\Desktop\\url1.xlsx')
        break




df.to_excel('C:\\Users\Administrator\Desktop\\url.xlsx')





