import numpy as np
import pandas as pd 

from sklearn import preprocessing;
from sklearn import model_selection;
from sklearn import linear_model;

def prepare_data(df,forecast_col,forecast_out,test_size):
    label = df[forecast_col].shift(-forecast_out);#creating new column called label with the last 5 rows are nan
    X = np.array(df[[forecast_col]]); #creating the feature array
    X = preprocessing.scale(X) #processing the feature array
    X_lately = X[-forecast_out:] #creating the column i want to use later in the predicting method
    X = X[:-forecast_out] # X that will contain the training and testing
    label.dropna(inplace=True); #dropping na values
    y = np.array(label)  # assigning Y
    X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, y, test_size=test_size) #cross validation

    response = [X_train,X_test , Y_train, Y_test , X_lately];
    return response;





df = pd.read_csv("prices.csv")
df=df[df.symbol=='FAST']#choosing stock symbol



forecast_col = 'close'#choosing which column to forecast
forecast_out = 5 #how far to forecast 
test_size = 0.2; #the size of my test set

X_train, X_test, Y_train, Y_test , X_lately =prepare_data(df,forecast_col,forecast_out,test_size); #calling the method were the cross validation and data preperation is in

learner = linear_model.LinearRegression(); #initializing linear regression model

learner.fit(X_train,Y_train); #training the linear regression model
score=learner.score(X_test,Y_test);#testing the linear regression model

forecast= learner.predict(X_lately); #set that will contain the forecasted data

response={};
response['test_score']=score; 
response['forecast_set']=forecast;

print(response);

