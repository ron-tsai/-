from selenium import webdriver
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

chrome_options=Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')


#防止被屏蔽
from selenium.webdriver import ChromeOptions

def getDriver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    #options.add_argument("--no-sandbox") # linux only
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    driver = webdriver.Chrome(options=options)
    driver.execute_cdp_cmd("Network.enable", {})
    driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"User-Agent": "browserClientA"}})
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            })
        """
    })
    return driver

bro = getDriver()


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

df=pd.DataFrame(columns=['timer_source','title','content'])

bro.get(url='https://www.chinanews.com/')


bro.implicitly_wait(10)
search_input=bro.find_element_by_id('q')
search_input.click()
bro.implicitly_wait(10)
search_input.send_keys('A股')
bro.find_element_by_xpath('//a[@class="search_a"]').click()
for i in range(1000):
    print(i)

    if i ==0:
        handle = bro.current_window_handle
        li_list = WebDriverWait(bro, 15, 0.1).until(EC.presence_of_all_elements_located((By.XPATH, '//li/a')))

        # li_list = bro.find_elements_by_xpath('//li/a')
        for li in li_list:
            link = li.click()
            handles = bro.window_handles
            for newhandle in handles:
                # 筛选新打开的窗口B
                if newhandle != handle:

                    bro.switch_to.window(newhandle)
                    try:
                        # 在新打开的窗口B中操作
                        element=WebDriverWait(bro,10,0.2).until(EC.presence_of_element_located((By.CLASS_NAME,'content')))
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
                    bro.switch_to.window(handle)
    else:

        try:
            element = WebDriverWait(bro, 15, 0.1).until(EC.presence_of_element_located((By.XPATH, '//table')))

            bro.find_element_by_xpath('//a[@href="javascript:ongetkey({})"]'.format(i)).click() ####翻页！！！
            bro.implicitly_wait(10)
        except NoSuchElementException or TimeoutException :
            pass
            bro.back()
            time.sleep(2)
            element = WebDriverWait(bro, 15, 0.1).until(EC.presence_of_element_located((By.XPATH, '//table')))

            bro.find_element_by_xpath('//a[@href="javascript:ongetkey({})"]'.format(i)).click()  ####翻页！！！



        handle = bro.current_window_handle
        li_list = WebDriverWait(bro, 15, 0.1).until(EC.presence_of_all_elements_located((By.XPATH, '//li/a')))

        for li in li_list:
            link = li.click()
            bro.implicitly_wait(10)
            handles = bro.window_handles
            for newhandle in handles:
                # 筛选新打开的窗口B
                if newhandle != handle:

                    bro.switch_to.window(newhandle)
                    try:
                        # 在新打开的窗口B中操作
                        bro.implicitly_wait(10)
                        title = bro.find_element_by_xpath('.//h1[@style="display:block; position:relative; clear:both"]')

                        timer_source = bro.find_element_by_xpath('.//div[@class="left-t"]').text

                        elements = bro.find_element_by_xpath('.//div[@class="left_zw"]')

                        contents = elements.find_elements_by_xpath('.//p')

                        contain = ''
                        for content in contents:
                            text = content.get_attribute('innerText')
                            contain = contain + ' ' + text
                        s = pd.Series([timer_source, title, contain], index=['timer_source', 'title', 'content'])
                        df = df.append(s, ignore_index=True)
                    except NoSuchElementException or TimeoutException:
                        pass



                    bro.close()
                    bro.switch_to.window(handle)


df.to_excel('C:\\Users\Administrator\Desktop\\中新网1.xlsx')



