# encoding:utf-8


import asyncio
from pyppeteer import launch
from time import sleep
import requests


async def main():
    browser = await launch({'headless': False,'executablePath': 'F:\star_download\chrome-win/Chrome','ignoreDefaultArgs': ["--enable-automation"]})
    page = await browser.newPage()
    await page.goto('http://sou.chinanews.com/search.do?q=A%E8%82%A1')

    for i in range(4,1000):
        await page.click('#pagediv > a:nth-child({})'.format(i))
        await page.waitForNavigation()
        sleep(2)



    # await browser.close()


asyncio.get_event_loop().run_until_complete(main())


#pagediv > a:nth-child(4)
#pagediv > a:nth-child(5)
#pagediv > a:nth-child(6)
