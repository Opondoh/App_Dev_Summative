from sklearn import linear_model
import pandas as pd
from sklearn.model_selection import train_test_split

#IMPORT CSV FILES
dWind_2 = pd.read_csv('wind_generation_data.csv')

#DATA EXPLORATION AND CLEANING
#view the number of rows and columns of the two main data sets
print(dWind_2.shape)

#view first five rows form the two data sets
print(dWind_2.head())

#confirm all column names for solar data
print(dWind_2.columns)

#check column data types
print(dWind_2.info())

#check for any missing values
print(dWind_2.isnull().sum())

#ML MODEL USING SOLAR DATA
#split data into training and test sets
X = dWind_2.drop(['Power Output'], axis = 1).values # X are the input (or independent) variables
y = dWind_2['Power Output'].values # Y is output (or dependent) variable

# create training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#FIT THE MODEL
lm = linear_model.LinearRegression()
model = lm.fit(X_train,y_train)

#MAKE PREDICITONS
y_pred_wind = lm.predict(X_test)
print(y_pred_wind[0:5]) # print the first 5 predictions

#side by side of actual values and predicated values
y_pred_wind = lm.predict(X_test)

#connect predictions with actual banking crisis values
for i in range(10):
    print(y_test[i], y_pred_wind[i])
