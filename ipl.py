import iplAllStats
import openpyxl
import iplScoreCards

class IPL:
    def __init__(self):
        pass
    def getAllSeasonStats(self):
        for i in range(8,21):
            items = []
            value = "{0:0=2d}".format(i)
            items = (iplAllStats.AllSeasonStats(f"/stats/20{value}/most-runs").links)            
            items.append(f"/stats/20{value}/most-runs")
            for data in items:
                fileName = f"ipl20{value}allstats.xlsx"
                iplAllStats.AllSeasonStats(data).prepareData(fileName,data,f"/stats/20{value}/")
            self.deleteSheet('sheet1',fileName)


    def getAllTimeStats(self):
        links = []
        links = (iplAllStats.AllSeasonStats(f"/stats/all-time/most-runs").links)         
        links.append(f"/stats/all-time/most-runs")
        fileName = f"iplallTimeStats.xlsx"        
        for data in links:
            iplAllStats.AllSeasonStats(data).prepareData(fileName,data,f"/stats/all-time/")
        self.deleteSheet('sheet1',fileName)
        return links
    
    def deleteSheet(self,sheetName,fileName):
        workbook=openpyxl.load_workbook(fileName)
        workbook.remove_sheet(workbook.get_sheet_by_name(sheetName))
        workbook.save(fileName)

    def get_season_range(self):
        return [ {"season":2008,"start":275,"end":334},{"season":2009,"start":216,"end":275},{"season":2010,"start":156,"end":216},
            {"season":2011,"start":82,"end":156},{"season":2012,"start":2,"end":78}, {"season":2013,"start":606,"end":607},
            {"season":2013,"start":616,"end":651},{"season":2013,"start":652,"end":690},{"season":2013,"start":691,"end":693}, 
            {"season":2014,"start":2424,"end":2484},{"season":2015,"start":3226,"end":3286},{"season":2016,"start":4042,"end":4102},
            {"season":2017,"start":5839,"end":5899},{"season":2018,"start":7894,"end":7954},{"season":2019,"start":11137,"end":11154},
            {"season":2019,"start":11309,"end":11348},
            {"season":2019,"start":11412,"end":11416} ]

    def generate_scorecards(self):
        for data in self.get_season_range():
            iplScoreCards.ScoreCards(data['start'],data['end']).generate_file(f"dataset/allMatchDetail/{data['season']}/")

# IPL().getAllSeasonStats()
IPL().getAllTimeStats()

# IPL().generate_scorecards()
