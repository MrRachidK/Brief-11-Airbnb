# Import of all the libraries we need

import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
from functions import namestr, separator

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# 1. Import of the datas we need to analyze

calendar_data = pd.read_csv("/home/apprenant/Documents/Brief-12-Airbnb/data/01_raw/calendar.csv").sample(10000)
listings_data = pd.read_csv("/home/apprenant/Documents/Brief-12-Airbnb/data/01_raw/listings.csv").sample(10000)
neighbourhoods_data = pd.read_csv("/home/apprenant/Documents/Brief-12-Airbnb/data/01_raw/neighbourhoods.csv")

print(calendar_data.head())
print("Il y a {} lignes et {} colonnes dans la base de données {}".format(calendar_data.shape[0], calendar_data.shape[1], namestr(calendar_data, globals())))

separator()

print(listings_data.head())
print("Il y a {} lignes et {} colonnes dans la base de données {}".format(listings_data.shape[0], listings_data.shape[1], namestr(listings_data, globals())))

separator()

print(neighbourhoods_data.head())
print("Il y a {} lignes et {} colonnes dans la base de données {}".format(neighbourhoods_data.shape[0], neighbourhoods_data.shape[1], namestr(neighbourhoods_data, globals())))

separator()

# 2. Checking of the duplicated values

# a. calendar_data

key_cols_calendar_data = ['date', 'price', 'adjusted_price', 'minimum_nights', 'maximum_nights']
calendar_data = calendar_data[key_cols_calendar_data].sample(10000)

# b. listings_data

key_cols_listings_data = ['id', 'host_location', 'latitude', 'longitude', 'property_type', 'room_type', 'accommodates', 'bathrooms_text', 'bedrooms', 'beds', 'price', 'minimum_nights', 'maximum_nights', 'review_scores_rating', 'reviews_per_month']
listings_data = listings_data[key_cols_listings_data].sample(10000)

# c. neighbourhoods_data

neighbourhoods_data = neighbourhoods_data['neighbourhood']

# 3. Checking of the duplicated values

print(calendar_data.duplicated().value_counts())
print(listings_data.duplicated().value_counts())
print(neighbourhoods_data.duplicated().value_counts())

separator()

# 4. Checking of the value types

print(calendar_data.dtypes)
separator()
print(listings_data.dtypes)
separator()
print(neighbourhoods_data.dtypes)
separator()

# 5. Checking of the missing values

print(calendar_data.isnull().sum()) 
separator()
print(listings_data.isnull().sum()) 
separator()
print(neighbourhoods_data.isnull().sum()) 
separator()

# 6. Processing of the missing values

# a. calendar_data

calendar_data['price'] = calendar_data['price'].str.replace('$', '')
calendar_data['price'] = calendar_data['price'].str.replace(',', '')
calendar_data['price'] = calendar_data['price'].astype(float)
calendar_data['price'] = calendar_data['price'].fillna(calendar_data.price.mean())

calendar_data['adjusted_price'] = calendar_data['adjusted_price'].str.replace('$', '')
calendar_data['adjusted_price'] = calendar_data['adjusted_price'].str.replace(',', '')
calendar_data['adjusted_price'] = calendar_data['adjusted_price'].astype(float)
calendar_data['adjusted_price'] = calendar_data['adjusted_price'].fillna(calendar_data.adjusted_price.mean())

calendar_data['minimum_nights'] = calendar_data['minimum_nights'].fillna(calendar_data.minimum_nights.mean())
calendar_data['maximum_nights'] = calendar_data['maximum_nights'].fillna(calendar_data.maximum_nights.mean())

# b. listings_data

listings_data['host_location'] = listings_data['host_location'].fillna('Not specified')
listings_data['bathrooms_text'] = listings_data['bathrooms_text'].fillna('Not specified')
listings_data['bedrooms'] = listings_data['bedrooms'].fillna(method='bfill')
listings_data['beds'] = listings_data['beds'].fillna(method='bfill')
listings_data['review_scores_rating'] = listings_data['review_scores_rating'].fillna(listings_data['review_scores_rating'].mean())
listings_data['reviews_per_month'] = listings_data['reviews_per_month'].fillna(listings_data['reviews_per_month'].mean())

# 7. Handle the types of our variables

# a. calendar_data

calendar_data['date'] = pd.to_datetime(calendar_data['date'])
print(calendar_data.dtypes)
separator()

# b. listings_data

listings_data['price'] = listings_data['price'].str.replace('$', '')
listings_data['price'] = listings_data['price'].str.replace(',', '')
listings_data['price'] = listings_data['price'].astype(float)
print(listings_data.dtypes)
separator()