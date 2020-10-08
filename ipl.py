import iplAllStats
import openpyxl

class IPL:
    def __init__(self):
        pass
    def getAllStats(self):
        for i in range(8,21):
            items = []
            value = "{0:0=2d}".format(i)
            items = (iplAllStats.IPLAllStats(f"/stats/20{value}/most-runs").links)            
            items.append(f"/stats/20{value}/most-runs")
            for data in items:
                fileName = f"ipl20{value}allstats.xlsx"
                print(data,i)
                iplAllStats.IPLAllStats(data).prepareData(fileName,data,f"/stats/20{value}/")
            workbook=openpyxl.load_workbook(fileName)
            workbook.remove_sheet(workbook.get_sheet_by_name('sheet1'))
            workbook.save(fileName)
            
IPL().getAllStats()