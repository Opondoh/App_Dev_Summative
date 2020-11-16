#import os
import pickle
import requests
import pandas as pd
from datetime import datetime

#apikey = os.environ.get('apikey')

#lat = 8.598084
#lon = 53.556563

##WIND DATA

url1 = "https://api.openweathermap.org/data/2.5/onecall?lat=8.598084&lon=53.556563&units=metric&exclude=hourly,current,minutely&appid=e7f11591b0d000f3b7d224113f8b1149"
wind_data = requests.get(url1).json()
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
#print([date1, speed, direction])

#add to empty dataframe
w_df['date1'] = date
w_df['speed'] = speed
w_df['direction'] = direction

#convert timestamp to datetime and add Day plus Month columns
w_df['Datetime'] = pd.to_datetime(w_df['date1'], unit='s')
#w_df['Day'] = w_df['Datetime'].dt.day 
#w_df['Month'] = w_df['Datetime'].dt.month

#set datetime as index
w_df.set_index('Datetime', inplace = True)
#print(w_df.head())

##SOLAR DATA

url2 = "https://api.openweathermap.org/data/2.5/onecall?lat=-19.461907&lon=142.110216&units=metric&exclude=hourly,current,minutely&appid=e7f11591b0d000f3b7d224113f8b1149"
solar_data = requests.get(url2).json()
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
s_df['date2'] = date
s_df['temp_hi'] = temp_hi
s_df['temp_low'] = temp_low
s_df['solar'] = solar
s_df['cloud_cover'] = cloud_cover
s_df['rainfall'] = rainfall

#convert timestamp to datetime and add Day plus Month columns
s_df['Datetime'] = pd.to_datetime(s_df['date2'], unit='s')
#s_df['Day'] = w_df['Datetime'].dt.day 
#s_df['Month'] = w_df['Datetime'].dt.month

#set datetime as index
s_df.set_index('Datetime', inplace = True)
#print(s_df.head())

#merge wind data set to solar data set
weather_data = pd.DataFrame()

weather_data['date'] = date
weather_data['speed'] = speed
weather_data['direction'] = direction
weather_data['temp_hi'] = temp_hi
weather_data['temp_low'] = temp_low
weather_data['solar'] = solar
weather_data['cloud_cover'] = cloud_cover
weather_data['rainfall'] = rainfall

#print(weather_data.head())

#predict solar power output
solar_vals = weather_data.drop(['date', 'speed', 'direction'], axis = 1).values 
wind_vals = weather_data.drop(['date','temp_hi', 'temp_low', 'solar', 'cloud_cover', 'rainfall'], axis = 1).values

#load models from disk

solar_model = pickle.load(open('solar_model.pkl', 'rb'))
s_power_predictions = solar_model.predict(solar_vals)

predictions_s = pd.DataFrame(s_power_predictions)
weather_data['solar_predictions'] = predictions_s
print(weather_data.head(10))

#load wind model from disk
wind_model = pickle.load(open("wind_model.pkl", 'rb'))
w_power_predictions = wind_model.predict(wind_vals)

predictions_w = pd.DataFrame(w_power_predictions)
weather_data['wind_predictions'] = predictions_w
print(weather_data.head(10))