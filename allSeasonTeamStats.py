import utils
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class TeamStats:

    def __init__(self,url):
        self.baseUrl = f"https://www.iplt20.com{url}"
        self.soup = utils.getHtmlFromLib(self.baseUrl)

    def getAllTeams(self):
        return [[item.text.strip() for item in data.findAll("li", {"class": "drop-down__dropdown-list__option"}) if (item.text.strip()!="All Teams") ] for data in self.soup.findAll("div", {"class": "stats-table__filter drop-down js-drop-down js-teams"})]    
    
    def chooseTeams(self):
        driver = utils.getBrowser(self.baseUrl)
        select = driver.find_elements_by_xpath("//*[contains(text(), 'All Teams')]")        
        return select


print(TeamStats("/stats/2008/most-runs").getAllTeams())
# print(TeamStats("/stats/2008/most-runs").chooseTeams())