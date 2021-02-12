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
        "executablePath": r"C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe",
        # 关闭无头浏览器 默认是无头启动的
        "headless": False,
    }
    # 创建浏览器对象，可以传入 字典形式参数
    browser = await launch(**start_parm)

    # 创建一个页面对象， 页面操作在该对象上执行
    page = await browser.newPage()

    await page.goto('http://sou.chinanews.com/search.do?q=A%E8%82%A1')  # 页面跳转


    # await page.click('#news_list > table:nth-child(1) > tbody > tr:nth-child(1) > td:nth-child(2) > ul > li.news_title > a')
    # page.waitForNavigation({'timeout': 50000})
    # for i in range(1,1000):
    # page.click('#pagediv > a:nth-child(4)')

    elements = await page.querySelectorAll(".news_title a")
    for item in elements:
        # print(await item.getProperty('textContent'))
        # <pyppeteer.execution_context.JSHandle object at 0x000002220E7FE518>

        # 获取文本
        # title_str = await (await item.getProperty('textContent')).jsonValue()

        # 获取链接
        pages_link = await (await item.getProperty('href')).jsonValue()
        # print(title_str)
        print(pages_link)





asyncio.get_event_loop().run_until_complete(main())   # 创建异步池并执行main函数。

#pagediv > a:nth-child(4)   第二页
#pagediv > a:nth-child(5)   第三页

