import requests
from utils import write_json_data
from utils import get_detail_json
import pathlib
import os 
class ScoreCards:

    def __init__(self,start_range,end_range):
        self.start = start_range
        self.end = end_range
            
    
    def get_url(self,match_no):
        return f"https://cricketapi.platform.iplt20.com/fixtures/{match_no}/scoring"
    
    

    def get_file_name(self,url):
        return get_detail_json(url)['matchInfo']['tournamentLabel'].replace(" ","_")+"_"+get_detail_json(url)['matchInfo']['description'].replace(" ","_")

    def generate_file(self,directory):
        for index in range(self.start,self.end):
            url = self.get_url(index)
            if not os.path.exists(directory):
                os.makedirs(os.path.dirname(directory), exist_ok=True)
            write_json_data(os.path.join(directory,f"{self.get_file_name(url)}.json"),get_detail_json(url))
                
            
        






