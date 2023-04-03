import webbrowser
import os
import time

# URLs to open in Google Chrome
urls = ["https://boss.wee43g7h.info/login",
        "https://www.feixiaohaozh.info/exchange/notice/",
        "https://www.jin10.com/",
        "https://docs.google.com/spreadsheets/d/1EUjWV_1nCCNjS2OlIyFFZYtYXQxbYdQqomwZIUPpsoA/edit#gid=0",
        "https://www.snapmail.cc/#/emailList/hongbao@snapmail.cc",
        "https://www.investing.com/news/cryptocurrency-news",
        "https://www.linkedin.com/feed/",
        "https://www.instagram.com/",
        "https://www.facebook.com/Bikingex",
        "https://twitter.com/BiKingex",
        "https://www.reddit.com/r/BiKingex/",
        "https://weibo.com/u/3073127401",
        "https://mail.google.com/mail/u/7/#inbox",
        "https://mail.google.com/mail/u/9/#inbox",
        "https://news.bitcoin.com/",
        "https://biking.zendesk.com/knowledge/editor/01GW6QY9Y2JJ86XVYVFX22HC33/zh-cn?brand_id=10581080855057",
        ]


chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

# Paths to the Excel files
excel_paths = ["D:\\桌面\\合伙人账目\\合伙人列表更新至1.19.xlsx", "D:\\桌面\\推广\\活动报名填写.xlsx", "D:\\桌面\\推广\\活动制作教学.xlsx"]

# Paths to the executable files
exe_paths = ["C:\\Program Files\\PaoPao\\泡泡.exe", "D:\\Telegram Desktop2\\Telegram.exe", "D:\\Telegram Desktop3\\Telegram.exe","D:\\Telegram Desktop4\\Telegram.exe"]

# Open Google Chrome tabs
for url in urls:
    # Open the URL in Chrome
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open(url)
    time.sleep(2) # 5-second delay

# Open Excel files
for excel_path in excel_paths:
    os.startfile(excel_path)
    time.sleep(2) # 5-second delay

# Open executable files
for exe_path in exe_paths:
    os.startfile(exe_path)
    time.sleep(2) # 5-second delay
