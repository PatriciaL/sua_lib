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


# ---------------------------FEATURE ENGINEERING

#Function to Replace NaN with mean

def test_replace_nan_with_mean(df,columns):
    """
    This funcion allow us to fill the NaN values for a value we prefer
    Parameters
        df: the dataframe
        column_name: the column we want to operate with
        replacement_value: is the value we want to add to replace NaN Values
    Returns:
        df: the dataframe with the replacement value added
    """

    for col in columns:
        mean = df[col].mean()
        df[col].fillna(mean, inplace = True)
    return df

#Function to Replace NaN with mean based on column type passing object columns

def test_replace_nan_with_mean_num_cols(df, columns):
    """This function replaces NaN values into a dataframe, iterating by type of column.
       In case of integer or float64 add the mean value.
       With the "class" clausule we pass the object columns.append

       Parameters: 
       df: the dataframe we want to operate with
       columns: the columns where we registered NaN values 

       Returns: 
       df: modified dataframe
    """
    for col in columns:
        if df[col].dtype in ['int64', 'float64']:
            mean = df[col].mean()
            df[col].fillna(mean, inplace=True)
        elif df[col].dtype == 'object':
            pass
    return df

#Function to Replace with predeterminated values just in onject types

def test_replace_nan_with_predetermined_value(df, columns, value='unknown'):
    """
        This function replace NaN values with a value determined. In this case "unknown" across object columns
    and passing integer or float column formats.Iterates with a loop over all the columns into the dataframe
    Parameters:
        df: the dataframe
        columns: which columns we want to iterate
        value: includes the value we want to introduce to replace the NaN values
    Returns:
        df: the modified dataframe
    """
    for col in columns:
        if df[col].dtype == 'object':
            df[col].fillna(value, inplace=True)
        elif df[col].dtype in ['int64', 'float64']:
            pass
    return df

#Convert the date column to datetime

def test_create_date_columns(df, date_col):
    """
        This function uses two parameters converting a date column into date time format and after that
    obtaining columns with year, month, month_name, day, day_name and week.
    Parameters:
        df: the dataframe we want to use
        date_col: the column we want to use to extract the rest of fields
    Returns:
        df: the modified dataframe with the rest of date columns
    """
    df[date_col] = pd.to_datetime(df[date_col])
    df['year'] = df[date_col].dt.year
    df['month'] = df[date_col].dt.month
    df['month_name'] = df[date_col].dt.month_name()
    df['day'] = df[date_col].dt.day
    df['day_name'] = pd.to_datetime(df[date_col]).dt.day_name()
    df['week'] = pd.to_datetime(df[date_col]).dt.week
    return df
