from sklearn import linear_model
import pandas as pd
from sklearn.model_selection import train_test_split
import pickle

#IMPORT CSV FILES
dSolar_2 = pd.read_csv('solar_generation_data.csv')

#DATA EXPLORATION AND CLEANING
#view the number of rows and columns of the two main data sets
print(dSolar_2.shape)

#view first five rows form the two data sets
dSolar_2.head()

#remove the degree symbol
dSolar_2['Temp Hi'] = dSolar_2['Temp Hi'].replace('\u00b0','', regex=True)
dSolar_2['Temp Low'] = dSolar_2['Temp Low'].replace('\u00b0','', regex=True)

#confirm all column names for solar data
dSolar_2.columns

#check column data types
dSolar_2.info()

#change Temp Hi and Temp Low to numeric
cols=[i for i in dSolar_2.columns if i in ['Temp Hi', 'Temp Low']]
for col in cols:
    dSolar_2[col]=pd.to_numeric(dSolar_2[col], errors='coerce')
dSolar_2.info()

#check for any missing values
dSolar_2.isnull().sum()

#drop remaining missing values
dSolar_clean = dSolar_2.dropna()
dSolar_clean.isnull().sum()

#ML MODEL USING SOLAR DATA
#split data into training and test sets
X = dSolar_clean.drop(['Month ', 'Day', 'Power Generated in MW'], axis = 1).values # X are the input (or independent) variables
y = dSolar_clean['Power Generated in MW'].values # Y is output (or dependent) variable

# create training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#FIT THE MODEL
lm = linear_model.LinearRegression()
model = lm.fit(X_train,y_train)

#MAKE PREDICITONS
#y_pred_solar = lm.predict(X_test)
#print(y_pred_solar[0:5]) # print the first 5 predictions

#side by side of actual values and predicated values
#y_pred_solar = lm.predict(X_test)

#connect predictions with actual power output values
#for i in range(10):
    #print(y_test[i], y_pred_solar[i])

#add predictions column to the dataFrame
#predictions = pd.DataFrame(y_pred)
#dSolar_2['Solar_predictions'] = predictions
#dSolar_2.head(10)

# save the model to disk
filename = 'solar_model.pkl'
outfile = open(filename,'wb')
pickle.dump(model, outfile)
outfile.close()

# load the model from disk
model_frm_disk = pickle.load(open(filename, 'rb'))
result = model_frm_disk.score(X_test, y_test)
print(result)

