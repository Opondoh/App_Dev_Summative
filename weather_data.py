#import os
import requests
import pandas as pd
from datetime import datetime

#apikey = os.environ.get('apikey')

#lat = 8.598084
#lon = 53.556563

url = "https://api.openweathermap.org/data/2.5/onecall?lat=8.598084&lon=53.556563&units=metric&exclude=hourly,current,minutely&appid=e7f11591b0d000f3b7d224113f8b1149"
wind_data = requests.get(url).json()
#print(wind_data)

#initiate empty columns
num = 0
date = []
speed = []
direction = []

#start with an empty df
w_df = pd.DataFrame()
   
for weather in wind_data['daily']:
    dt = wind_data['daily'][num]["dt"]
    ws = wind_data['daily'][num]['wind_speed']
    wd = wind_data['daily'][num]['wind_deg']
        
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

#print(w_df.head())

url = "https://api.openweathermap.org/data/2.5/onecall?lat=-19.461907&lon=142.110216&units=metric&exclude=hourly,current,minutely&appid=e7f11591b0d000f3b7d224113f8b1149"
solar_data = requests.get(url).json()
#print(solar_data)

#initiate empty columns
num1 = 0
date = []
temp_hi = []
temp_low = []
solar = []
cloud_cover = []
rainfall = []

#start with an empty df
s_df = pd.DataFrame()
   
for weather in wind_data['daily']:
    s_dt = solar_data['daily'][num1]["dt"]
    l_temp = solar_data['daily'][num1]['temp']['min']
    h_temp = solar_data['daily'][num1]['temp']['max']
    cloud = solar_data['daily'][num1]['clouds']
    rain = solar_data['daily'][num1]['pop']
    sol = solar_data['daily'][num1]['uvi']
        
    date.append(s_dt)
    temp_hi.append(h_temp)
    temp_low.append(l_temp)
    solar.append(sol)
    cloud_cover.append(cloud)
    rainfall.append(rain)
    
    num1 = num1 + 1
#print([date, speed, direction])

#add to empty dataframe
s_df['date'] = date
s_df['temp_hi'] = temp_hi
s_df['temp_low'] = temp_low
s_df['solar'] = solar
s_df['cloud_cover'] = cloud_cover
s_df['rainfall'] = rainfall

#convert timestamp to datetime and add Day plus Month columns
s_df['Datetime'] = pd.to_datetime(w_df['date'], unit='s')
#s_df['Day'] = w_df['Datetime'].dt.day 
#s_df['Month'] = w_df['Datetime'].dt.month

#set datetime as index
s_df.set_index('Datetime', inplace = True)
print(s_df.head())