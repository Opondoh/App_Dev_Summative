from sklearn import linear_model
import pandas as pd
from sklearn.model_selection import train_test_split
import pickle

#IMPORT CSV FILES
dWind_2 = pd.read_csv('wind_generation_data.csv')

#DATA EXPLORATION AND CLEANING
#view the number of rows and columns of the two main data sets
dWind_2.shape

#view first five rows form the two data sets
dWind_2.head()

#confirm all column names for solar data
dWind_2.columns

#check column data types
dWind_2.info()

#check for any missing values
dWind_2.isnull().sum()

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
#y_pred_wind = lm.predict(X_test)
#print(y_pred_wind[0:5]) # print the first 5 predictions

#side by side of actual values and predicated values
#y_pred_wind = lm.predict(X_test)

#connect predictions with actual banking crisis values
#for i in range(10):
    #print(y_test[i], y_pred_wind[i])

#add predictions column to the dataFrame
#predictions = pd.DataFrame(y1_pred)
#dWind_2['Wind_predictions'] = predictions
#print(dWind_2.head(10))

# save the model to disk
filename = 'wind_model.pkl'
outfile = open(filename,'wb')
pickle.dump(model, outfile)
outfile.close()

# load the model from disk
model_frm_disk = pickle.load(open(filename, 'rb'))
result = model_frm_disk.score(X_test, y_test)
print(result)

