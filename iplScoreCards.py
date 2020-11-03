import utils
from fpdf import FPDF
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import pandas as pd

class ScoreCards:

    def __init__(self,year,match_no):
        self.url = f"https://www.iplt20.com/archive/20{year}/{match_no}"
        self.soup = utils.getHtmlfromBody(self.url)

    def toss(self):
        return [data.find("h4").text.replace("Toss: ","") for data in self.soup.findAll("div", {"class": "matchDetails"})]

    def bowlers_scorecard(self):
        for data in self.soup.findAll("li", {"class": "bowler"}):
            self.add_table_to_pdf(utils.getDataFromTable(data),"test.pdf")

    def batsman_scorecard(self):
        row_names = ["Batsmen","Mode Of Dismissal","Runs","Ballss","SR","4s","6s"]
        for data in self.soup.findAll("div", {"class": "scorecardTable batsmen"}):
            self.add_table_to_pdf(self.chaneg_first_row_name_of_df(utils.getDataFromTable(data),row_names),"test.pdf")
    
    def fall_of_wickets(self):
        for data in self.soup.findAll("li", {"class": "fow"}):
            self.add_table_to_pdf(utils.getDataFromTable(data),"test.pdf")

    def chaneg_first_row_name_of_df(self,df,data):
        for idx, val in enumerate(data):
            df.iloc[0][idx] = val
        return df
  
    def match_basic_info(self):
        for mydivs1 in self.soup.findAll("div", {"class": "eventDetails"}):
            for m in (mydivs1.findAll("p")):
                print(m.text)

    def playing_eleven(self):
        for mydivs1 in self.soup.findAll("div", {"class": "playingxi"}):
            print("-------")
            print(mydivs1.find("h1").text)
            for cell in mydivs1.find(["ol","li"]):
                print(cell.text)

    def add_table_to_pdf(self,df,filename):
        with PdfPages(filename) as pdf:
            header = df.columns
            table = np.asarray(df)
            fig = plt.figure(figsize=(16, 16))
            ax = plt.Axes(fig, [0., 0., 1., 1.])
            ax.set_axis_off()
            fig.add_axes(ax)
            tab = plt.table(cellText=table, cellLoc='center', loc='center')
            tab.set_fontsize(10)
            tab.scale(1,3)
            pdf.savefig(fig)
            plt.close()



# print(ScoreCards("08","59").batsman_scorecard())
# print(ScoreCards("08","59").fall_of_wickets())
# print(ScoreCards("08","59").bowlers_scorecard())

# print(ScoreCards("08","59").match_basic_info())
# print(ScoreCards("08","59").playing_eleven())
# print(ScoreCards("08","59").playing_eleven())
print(ScoreCards("11","06").toss())


