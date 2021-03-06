from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import pandas as pd
import requests
import time
import numpy as np
import datetime as dt

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"   
    }
driver = webdriver.Chrome()
driver.get('https://datacenter.jin10.com/market')

while True:
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    control_time = now[14:16]
    soup = BeautifulSoup(driver.page_source,'html.parser')
    product = soup.find_all('h3',{'class':'jin-pricewall_list-item_name'})
    trade_price = soup.find_all('span',{'class':'J_last'})
    # print(product)
    target_trade_price = float(trade_price[47].text)
    product_test = product[47].text
    print("商品:",product_test)
    print("成交價",str(target_trade_price))
    print("操作時間:",now)
