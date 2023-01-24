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




#-------------------WORKING WITH GEOMETRIES --------------------

def test_create_geometry_column(df,lon_col,lat_col):
    """
        This function allow us create a basic geometry column based on points
    We need some columns
        x: represents longitude column
        y: represents latitude column
        After join those columns we passed the info to obtain a dataframe
    Parameters:
        df: the dataframe we want to convert into a geopandas dataframe
        lon_col: the column that contains longitude values
        lat_col: the column that contains the latitude values
    Returns: 
        gdf: a geodataframe
    """
    # Create a list of Point objects
    geometry = gpd.points_from_xy(lon_col,lat_col)
    # Create a GeoDataFrame
    gdf = gpd.GeoDataFrame(df, geometry=geometry)
    gdf.crs = {'init': 'epsg:4326'}
    return gdf


#Detect the latitude and longitude index

def test_detect_latitude_column(df, column_name):
    """
        This function detect the index column that contains "latitude" values or derivates
    into the column name
    Parameters:
        df: the dataframe 
        column_name: the column that contains the name
    Returns:
        lat_col: the index of the column or the text "The longitude doesn't exist" or that the column doesn't exits     
    """

    #Obtaining the name of the dataframe columns
    column_names = df.columns.tolist()
    
    #Compilate the regex expresion
    regex_lat = re.compile(r"(latitud|lat|.*ati.*"+column_name+")", re.IGNORECASE)
    
    # Search the column name that contains "latitude" or the name specific in column_name
    lat_col = next((i for i, x in enumerate(column_names) if regex_lat.search(x) != None), None)
    
    # If the column exits, we show the index number of column
    if lat_col != None:
        return lat_col
    else:

        return "The latitude column doesn't exist"


def test_detect_longitude_column(df, column_name):
    """
        This function detect the index column that contains "longitude" values or derivates
    into the column name
    Parameters:
        df: the dataframe 
        column_name: the column that contains the name
    Returns:
        lon_col: the index of the column or the text "The longitude doesn't exist"
    """
    
    #Obtaining the name of the dataframe columns
    column_names = df.columns.tolist()
    
    #Compilate the regex expresion
    regex_lon = re.compile(r"(longitude|lon|.*ongi.*"+column_name+")", re.IGNORECASE)
    
    # Search the column name that contains "latitude" or the name specific in column_name
    lon_col = next((i for i, x in enumerate(column_names) if regex_lon.search(x) != None), None)
    
    # If the column exits, we show the index number of column
    if lon_col != None:
        return lon_col
    else:

        return "The longitude column doesn't exist"


#Export the geodataframe in different options

def test_export_gdf(gdf,filename,format):
    """
        This function obtains export a file in the format we choose ("shape","geojson", "xlsx",
    "csv", "kml"). Important if the dataframe contains dates 
    shp format will not work. Currently this format is commented just
    discomment it to use. 
    Parameters
        gdf: the geodataframe we want to export
        filename: the filename we want to define the geodataframe in the export
        format: the format we prefer. By default, we define it into a list with the following values
    Raises:
        Indicates a ValueError to define that the file is in invalid format
    """
    formats = ["shp", "geojson", "csv", "xlsx", "kml"]
    if format not in formats:
        raise ValueError(f"Invalid format, options are {formats}")
    
    #if format == 'shp':
        #gdf.to_file(f"{filename}.shp")
    elif format == 'geojson':
        gdf.to_file(f"{filename}.json", driver = 'GeoJSON')
    elif format == 'csv':
        gdf.to_csv(f"{filename}.csv")
    elif format == 'xlsx':
        gdf.to_excel(f"{filename}.xlsx")
    elif format == 'kml':
        gdf.to_file(f"{filename}.kml", driver='KML')
    print(f"File exported successfully as {filename}.{format}")











    



