from sklearn import linear_model
import pandas as pd

#import the csv files
#dSolar_1 = pd.read_csv('solar_farm.csv')
dSolar_2 = pd.read_csv('solar_generation_data.csv')
#dWind_1 = pd.read_csv('wind_farm.csv')
dWind_2 = pd.read_csv('wind_generation_data.csv')

#view the number of rows and columns of the two main data sets
print(dSolar_2.shape, dWind_2.shape)

#view first five rows form the two data sets
print(dSolar_2.head())

print(dWind_2.head())

#remove the degree symbol
dSolar_2['Temp Hi'] = dSolar_2['Temp Hi'].replace('\u00b0','', regex=True)
dSolar_2['Temp Low'] = dSolar_2['Temp Low'].replace('\u00b0','', regex=True)

#confirm all column names for solar data
print(dSolar_2.columns)