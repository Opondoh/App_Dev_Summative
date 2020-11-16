import pandas as pd
import pickle
from sklearn import linear_model

#MAKE SOLAR_PREDICITONS
infile = open('solar_model','rb')
smodel_frm_disk = pickle.load(infile)
result = smodel_frm_disk.score(X_test, y_test)
infile.close()

y_pred_solar = lm.predict(X_test)
print(y_pred_solar[0:5]) # print the first 5 predictions

#side by side of actual values and predicated values
y_pred_solar = lm.predict(X_test)

#connect predictions with actual power output values
for i in range(10):
    print(y_test[i], y_pred_solar[i])

#add predictions column to the dataFrame
Spredictions = pd.DataFrame(y_pred)
dSolar_2['Solar_predictions'] = predictions
dSolar_2.head(10)