from sklearn import linear_model
import pandas as pd
from sklearn.model_selection import train_test_split
import pickle

#IMPORT CSV FILES
#dSolar_1 = pd.read_csv('solar_farm.csv')
dSolar_2 = pd.read_csv('solar_generation_data.csv')
#dWind_1 = pd.read_csv('wind_farm.csv')

#DATA EXPLORATION AND CLEANING
#view the number of rows and columns of the two main data sets
print(dSolar_2.shape)

#view first five rows form the two data sets
print(dSolar_2.head())

#remove the degree symbol
dSolar_2['Temp Hi'] = dSolar_2['Temp Hi'].replace('\u00b0','', regex=True)
dSolar_2['Temp Low'] = dSolar_2['Temp Low'].replace('\u00b0','', regex=True)

#confirm all column names for solar data
print(dSolar_2.columns)

#check column data types
print(dSolar_2.info())

#change Temp Hi and Temp Low to numeric
cols=[i for i in dSolar_2.columns if i in ['Temp Hi', 'Temp Low']]
for col in cols:
    dSolar_2[col]=pd.to_numeric(dSolar_2[col], errors='coerce')
print(dSolar_2.info())

#check for any missing values
print(dSolar_2.isnull().sum())

#drop remaining missing values
dSolar_clean = dSolar_2.dropna()
print(dSolar_clean.isnull().sum())

#ML MODEL USING SOLAR DATA
#split data into training and test sets
X = dSolar_clean.drop(['Month ', 'Power Generated in MW'], axis = 1).values # X are the input (or independent) variables
y = dSolar_clean['Power Generated in MW'].values # Y is output (or dependent) variable

# create training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#FIT THE MODEL
lm = linear_model.LinearRegression()
model = lm.fit(X_train,y_train)

#MAKE PREDICITONS
y_pred = lm.predict(X_test)
print(y_pred[0:5]) # print the first 5 predictions

#side by side of actual values and predicated values
y_pred = lm.predict(X_test)

#connect predictions with actual power output values
for i in range(10):
    print(y_test[i], y_pred[i])

# save the model to disk
fileObj = open('data.obj', 'wb')
pickle.dump(lm,fileObj)
fileObj.close()

fileObj = open('data.obj', 'rb')
y_pred = lm.predict(X_test)
fileObj.close()
print(print(y_pred[0:7]))