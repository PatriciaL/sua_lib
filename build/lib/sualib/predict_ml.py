"""
This functions .py document is oriented to used such us basic exploratory data analysis 
data prep and machine learning models basing in linear regression to predict store openings based in the dates
"""

#Libraries you need to work with this functions

#1//Data storing and anaysis
import pandas as pd
import geopandas as gpd
import datetime as dt
from datetime import datetime
import re


#2//Visualization
import matplotlib.pyplot as plt
import folium
import plotly.express as px
import shapely
import seaborn as sns

#3//Machine Learning Libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score
import pickle

# --------------------- PREDICTING STORE OPENING ---------------

def predict_store_opening(df):

    """
    This function creates a linear regression model to predict store openings and export
    the model
    """

    #We pass the date into ordinal or timestamp
    df['OpenDate'] = pd.to_datetime(df['OpenDate'])
    df['OpenDate'] = df['OpenDate'].map(dt.datetime.toordinal)

    #Select the features and the target variable (y value)
    # X is a numpy array with your features
    # y is the label array
    
    X = df.drop(columns=['OpenDate','CloseDate'])
    y = df['OpenDate']

    #We pass a one hot encoding to convert string and object columns into numbers
    
    label_encoder = LabelEncoder()

    #Divide the test between train and test

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    #Pasamos el encoding a la parte de test por todas las columnas 
    
    for i in X_train.columns :
        X_train[i] = label_encoder.fit_transform(X_train[i])
    for i in X_test.columns :
        X_test[i] = label_encoder.fit_transform(X_test[i])


    #We train the model

    model = LinearRegression()
    model.fit(X_train,y_train)

    #Evaluate the model
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"Mean Squared Error: {mse}, R2 Score: {r2}")

    # Print the confusion matrix in a graphic 
    plt.figure(figsize=(5,5))
    sns.scatterplot(y_test, y_pred)
    plt.xlabel('Valores reales')
    plt.ylabel('Valores predichos')
    plt.show()

    # Export the model 
    with open('store_closing_model.pkl', 'wb') as f:
        pickle.dump(model, f)

    return model


### --------------- VALIDATING THE MODEL 





    



