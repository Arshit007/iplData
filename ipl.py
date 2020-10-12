import iplAllStats
import openpyxl

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

print(IPL().getAllTimeStats())