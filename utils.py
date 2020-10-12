import requests
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import utils
import urllib.request as urllib2
import pandas as pd
import requests
from pandas import ExcelWriter

from openpyxl import load_workbook

import os 

def getDataFromTable(soup): 
        tables = soup.find_all("table")
        if tables:
            table = tables[0]
            tab_data = [[(cell.text.replace("\n"," ").strip()).replace("  ", "") for cell in row.find_all(["th","td"])]
                            for row in table.find_all("tr")]
            df = pd.DataFrame(tab_data)
            return df
        return pd.DataFrame()

def makeExcelFromData(df=None,fileName=None,sheetName=None):
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)),fileName)
    if os.path.exists(path):
        saveIntoExcel(df,fileName,sheetName,path)
    else:
        writer = pd.ExcelWriter(fileName, engine='xlsxwriter')
        df.to_excel(writer,sheet_name="sheet1",index=0)
        writer.save()
        saveIntoExcel(df,fileName,sheetName,path)

def saveIntoExcel(df,fileName,sheetName,path):
    if not df.empty:
        book = load_workbook(path)
        writer = pd.ExcelWriter(path, engine = 'openpyxl')
        writer.book = book
        if len(sheetName)>=31:       
            df.to_excel(writer,sheet_name=sheetName[:30],index=0)     
        else:
            df.to_excel(writer,sheet_name=sheetName,index=0)
        writer.save()
        
def getHtmlFromLib(url):
    response = urllib2.urlopen(url) 
    return BeautifulSoup(response.read(),'html.parser')

def getBrowser(url):
    options = Options()
    # options.add_argument("--headless") # Runs Chrome in headless mode.
    options.add_argument('--no-sandbox') # Bypass OS security model
    options.add_argument('--disable-gpu')  # applicable to windows os only
    options.add_argument('start-maximized') # 
    options.add_argument('disable-infobars')
    options.add_argument("--disable-extensions")
    browser = webdriver.Chrome(chrome_options=options,executable_path="driver/chromedriver.exe")
    browser.maximize_window()
    browser.get(url)
    # browser.set_window_size(1440, 900)
    browser.implicitly_wait(20)
    return browser



def getHtmlfromBody(url):
        browser = getBrowser(url)
        elem = browser.find_element_by_tag_name("body")
        no_of_pagedowns =30
        while no_of_pagedowns:
            elem.send_keys(Keys.PAGE_DOWN)
            no_of_pagedowns-=1
        return BeautifulSoup(browser.page_source,'html.parser') 