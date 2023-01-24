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
import numpy as np

#3//Machine Learning Libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score
import pickle


#Function to drop columns 

def drop_columns(df,columns):
     """
        This function drops some columns in a pandas dataframe
    Parameters:
        df: the dataframe where we want to delete the columns
        columns: list of column names you want to drop
    Returns:
        df: Dataframe
        The modified dataframe
    """
     df = df.drop(labels=columns, axis=1)
     return df

#Define merge two dataframes

def merge_dataframe(df1,df2,key1,key2):
    """
        This function drops some columns in a pandas dataframe
    Parameters:
        df1: first dataframe
        df2: second dataframe
        key1:  key column from first dataframe
        key2: second column from second dataframe
    Returns:
        df_unified: Dataframe
        The modified dataframe
    """
    df_unified = pd.merge(df1,df2,left_on=key1,right_on=key2)
    return df_unified 


