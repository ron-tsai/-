from selenium import webdriver
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import time
import random
from selenium.webdriver.chrome.options import Options

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
    "user-agent=Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)")

bro=webdriver.Chrome(options=option,chrome_options=chrome_options)
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

df=pd.DataFrame(columns=['timer_source','title','content'])

bro.get(url='http://sou.chinanews.com/search.do')
search_input=bro.find_element_by_id('q')
search_input.send_keys('A股')
bro.find_element_by_xpath('//input[@type="button"]').click()
for i in range(1,1000):
    print(i)
    a=random.random()

    time.sleep(a+1)
    li_list = WebDriverWait(bro, 60, 0.5).until(EC.presence_of_all_elements_located((By.XPATH, '//li/a/@href')))

    for li in li_list:
        print(li)

    bro.find_element_by_xpath('//a[@href="javascript:ongetkey({})"]'.format(i)).click()




