# from bs4 import BeautifulSoup
# import requests
from datetime import datetime 
from selenium import webdriver
from selenium.webdriver.common.by import By
import ai_translate
    
# issues:
# 在markets網址中，參雜了開頭為policy, business的類別

market_url = 'https://www.coindesk.com/markets/'
webdriver = webdriver.Firefox()
webdriver.get(market_url)

# 設定當日時間，以利在後面網址做結合
now_day = '2023/03/31'

# 取網頁最下方的新聞網址
title = webdriver.find_elements(By.CLASS_NAME, "card-title")
for i in title[-6:]:
    # 取網址
    href = i.get_attribute("href")
    if href.startswith(f'{market_url}{now_day}/'):
        # 取標題
        title = href.split(f'{now_day}/')[1]
        title = title.replace('-', ' ').replace('/', '')
        
print(ai_translate.translate_text(title))