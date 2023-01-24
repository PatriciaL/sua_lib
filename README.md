# Sua_lib - Simple Exploratory data analysis and linear regression for predict store openings based in geodataframes

## What is it / what does it do?

This is a python package that processes dataframes obtaining a geodataframe based on POINT geometries to predict store openings from a retailer.

Using different functions we could create datasets, cleaning data, exploring it and create a simple linear regression model to predict store openings. 

Each part of functions was divided in different modules, in case user prefers to use it spliting it in different use cases.

## How do I install it?
Just use 'pip install sua_lib' if you have pip installed (as most systems do). Or download the zip distribution from this site, unzip it and then:

* Mac: `cd` into it, and enter `sudo python setup.py install` along with your system password.
* Windows: Same thing but without `sudo`.

## How does it work?
Let's look at some sample code. To get point geometry column based on latitude and longitude:

    >>> from sua_lib.working_geo import create_geometry_column
    >>> df = df_unified
    >>> lat_col = df_unified['latitude']
    >>> lon_col = df_unified['longitude']
    >>> gdf = create_geometry_column(df,lat_col,lon_col)
