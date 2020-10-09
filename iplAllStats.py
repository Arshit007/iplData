import utils
from pandas import ExcelWriter
import pandas as pd

class AllSeasonStats: 
    def __init__(self,url=None):
        self.baseUrl = f"https://www.iplt20.com/{url}"
        self.soup = utils.getHtmlFromLib(self.baseUrl)
        self.links = self.getAllLinks()
         

    def prepareData(self,fileName,sheetName,fullurl):
        utils.makeExcelFromData((utils.getDataFromTable(self.soup)),fileName,sheetName.replace(fullurl," "))
       
    def getAllLinks(self):
        return [links.get('href') for links in self.soup.findAll('a',{'class': 'side-menu-child-list__item side-menu__link'})]
    
        

