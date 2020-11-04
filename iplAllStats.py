import utils
from pandas import ExcelWriter
import pandas as pd

class AllSeasonStats: 
    def __init__(self,url=None):
        self.baseUrl = f"https://www.iplt20.com/{url}"
        self.soup = utils.getHtmlFromLib(self.baseUrl)
        self.links = self.getAllLinks()
         

    def prepare_data(self,fileName,sheetName,fullurl,directory):
        utils.make_excel_from_data((utils.getDataFromTable(self.soup)),fileName,sheetName.replace(fullurl," "),directory)
       
    def getAllLinks(self):
        return [links.get('href') for links in self.soup.findAll('a',{'class': 'side-menu-child-list__item side-menu__link'})]
    

