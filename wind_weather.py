#import os
import requests
import pandas as pd
from datetime import datetime

#apikey = os.environ.get('apikey')

#lat = 8.598084
#lon = 53.556563

url = "https://api.openweathermap.org/data/2.5/onecall?lat=8.598084&lon=53.556563&units=metric&exclude=hourly,current,minutely&appid=e7f11591b0d000f3b7d224113f8b1149"
data = requests.get(url).json()
#print(data)

#initiate empty columns
num = 0
date = []
speed = []
direction = []

#start with an empty df
w_df = pd.DataFrame()
   
for weather in data['daily']:
    dt = data['daily'][num]["dt"]
    ws = data['daily'][num]['wind_speed']
    wd = data['daily'][num]['wind_deg']
        
    date.append(dt)
    speed.append(ws)
    direction.append(wd)
    
    num = num + 1
#print([date, speed, direction])

#add to empty dataframe
w_df['date'] = date
w_df['speed'] = speed
w_df['direction'] = direction

#convert timestamp to datetime and add Day plus Month columns
w_df['Datetime'] = pd.to_datetime(w_df['date'], unit='s')
w_df['Day'] = w_df['Datetime'].dt.day 
w_df['Month'] = w_df['Datetime'].dt.month

#set datetime as index
w_df.set_index('Datetime', inplace = True)

print(w_df.head())

