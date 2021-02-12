#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@time:2020/04/04
"""

import asyncio


from pyppeteer import launch



async def main():
    # 浏览器 启动参数
    start_parm = {
        # 启动chrome的路径
        "executablePath": r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        # 关闭无头浏览器 默认是无头启动的
        "headless": False,
    }
    # 创建浏览器对象，可以传入 字典形式参数

    browser = await launch(**start_parm)

    # 创建一个页面对象， 页面操作在该对象上执行
    page = await browser.newPage()
    await page.evaluateOnNewDocument('''() => {
            Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
            })
            }
        ''')

    await page.goto('https://www.chinanews.com/')  # 页面跳转
    await page.click('#q')
    await page.type('#q', 'A股')
    await page.click('#zxss > div.searchinput.right > a')
    # await page.click('#news_list > table:nth-child(1) > tbody > tr:nth-child(1) > td:nth-child(2) > ul > li.news_title > a')


    page_text = await page.content()  # 页面内容
    print(page_text)
    input('==========')
    # await browser.close()  # 关闭浏览器对象
    #

asyncio.get_event_loop().run_until_complete(main())   # 创建异步池并执行main函数。

