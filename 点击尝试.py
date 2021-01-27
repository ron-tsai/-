from selenium import webdriver
import time
bro=webdriver.Chrome(executable_path='C:\\Users\Administrator\AppData\Local\Google\Chrome\Application/chromedriver')

driver=webdriver.Chrome()
driver.get(url='https://news.cnstock.com/news/sns_jg/index.html')
time.sleep(10)
driver.find_element_by_id('j_more_btn').click()
time.sleep(3)
driver.find_element_by_id('j_more_btn').click()

