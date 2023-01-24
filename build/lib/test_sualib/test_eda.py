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
import numpy as np
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


#### --------------EXPLORATORY DATA ANALYSIS ----------------------------------

#Define non null percentage and show in a graphic

def test_non_null_percentage_by_column(df):
    """
        This function provides a total count of values in a dataframe
    and divide it number by the len of the dataframe in order to obtain a percentage
    to check how much non-null values are in the dataframe
        The columns where the values are below 100% are the ones where we need to apply methods in order to
    correct it.
    Parameters:
        df: the dataframe
    Returns: 
        a graphic with the non-null values
    
    """
    non_null_counts = df.count()
    total_counts = len(df)
    percentages = (non_null_counts / total_counts) * 100
    print(percentages)
    
    # Show the percentage in a bar chart
    percentages.plot(kind='bar')
    plt.xlabel('Columns')
    plt.ylabel('Percentage')
    plt.title('% of non-null values by column')
    plt.show()


#Create visualization for object columns 

def test_plot_columns_object_distribution_color(gdf, columns, kind='bar'):
    """
        This function represents the columnns sumatory values distributed by values in a bar grpah.
    Iterates over the columns into a dataframe by a for loop and plot its into a purple count plot
    It just work with type object values
    Parameters:
        df or gdf: the geodataframe or the dataframe
        columns: all the columns into de dataframe
        Kind: the kind of graphic type
    """
    color = 'purple'
    for col in columns:
        if col in gdf.columns:
            if gdf[col].dtype == 'object':
                plt.figure(figsize=(20,10))
                sns.countplot(x=col, data=gdf, color=color)
                plt.xticks(rotation=45)
                plt.title(f'Distribution of {col}')
                plt.show()
            else:
                print(f'{col} is not an object type column.')
        else:
            print(f'{col} not in the Dataframe')


#Create a visualization for numerical columns

def test_plot_columns_numerical_distribution_color(gdf, columns, kind='bar'):
    """
        This function represents the columnns sumatory values distributed by values in a bar grpah.
    Iterates over the columns into a dataframe by a for loop and plot its into a purple count plot
    It just work with type integer  values
    Parameters:
        df or gdf: the geodataframe or the dataframe
        columns: all the columns into de dataframe
        Kind: the kind of graphic type
    """
    color = 'purple'
    for col in columns:
        if col in gdf.columns:
            if gdf[col].dtype == 'int64':
                plt.figure(figsize=(20,10))
                sns.countplot(x=col, data=gdf, color=color)
                plt.xticks(rotation=45)
                plt.title(f'Distribution of {col}')
                plt.show()
            else:
                print(f'{col} is not an object type column.')
        else:
            print(f'{col} not in the Dataframe')


