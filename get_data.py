#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 01:15:09 2018

@author: zhangtiangu
"""

from bs4 import BeautifulSoup
from selenium import webdriver 
import os

from time import sleep
def download_data(ticker,freq="1d"):    
    if isinstance(ticker,str):
        ticker = [ticker]
        
    option = webdriver.ChromeOptions()
    prefs = {"download.default_directory" : os.getcwd()}
    option.add_experimental_option("prefs",prefs)
    browser = webdriver.Chrome(chrome_options=option)
    
    for i in ticker:
        url = "https://finance.yahoo.com/quote/{}/history?period1=1167627600&period2=1476936000&interval=1d&filter=history&frequency={}".format(i,freq)
        browser.get(url)
        soup=BeautifulSoup(browser.page_source,"html.parser")
        a = soup.find_all("a",{"class":"Fl(end) Mt(3px) Cur(p)"})
        try:
            assert len(a)==1
            browser.get(a[0].get("href"))
        except AssertionError as e:
            print("can't find tag 'a'")
        sleep(1)
        
    browser.close() 

if __name__ == "__main__":
    ticker = ["FXE","EWJ","GLD","QQQQ","SPY","SHV","DBA","USO","XBI","ILF","GAF","EPP","FEZ"]
    download_data(ticker)