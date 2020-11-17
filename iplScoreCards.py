import requests
from utils import write_json_data
from utils import get_detail_json
import pathlib
import os 
import pandas as pd
import json
from io import StringIO

class ScoreCards:

    def __init__(self,start_range,end_range):
        self.start = start_range
        self.end = end_range
            
    
    def get_url(self,match_no):
        return f"https://cricketapi.platform.iplt20.com/fixtures/{match_no}/scoring"
    
    def get_video_link(self,url):
        match_info = get_detail_json(url)['matchInfo']
        additional_detail =  match_info['additionalInfo']
        jobj={}
        if('matchStatus' in match_info):
            matchStatus = match_info['matchStatus']
            if('text' in matchStatus):
                jobj['result']= matchStatus['text']
        if('toss.elected' in additional_detail):
            jobj['toss']= additional_detail['toss.elected']
        if('highlights.link' in additional_detail):
            jobj['match_link']= str(additional_detail['highlights.link'])
            return jobj
            

    def get_file_name(self,url):
        return get_detail_json(url)['matchInfo']['tournamentLabel'].replace(" ","_")+"_"+get_detail_json(url)['matchInfo']['description'].replace(" ","_")

    # def generate_file(self,directory):
 
    #     self.create_video_excel(directory,)
    
    def create_match_details_directory(self,directory):
        for index in range(self.start,self.end):
            url = self.get_url(index)
            if not os.path.exists(directory):
                os.makedirs(os.path.dirname(directory), exist_ok=True)
            write_json_data(os.path.join(directory,f"{self.get_file_name(url)}.json"),get_detail_json(url))

    def create_video_excel(self,directory,season):
        data=[]
        for index in range(self.start,self.end):
            url = self.get_url(index)
            video_data = (self.get_video_link(url))
            if (video_data):
                data.append(video_data)
        if data:
            if not os.path.exists(directory):
                os.makedirs(os.path.dirname(directory), exist_ok=True)
            pd.read_json(StringIO(json.dumps(data))).to_excel(os.path.join(directory,f"{season}_season_highlights.xlsx"))

    
                
            
        






