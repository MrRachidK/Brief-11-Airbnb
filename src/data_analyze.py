# Import of all the libraries we need

import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
from functions import namestr, separator

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# 1. Import of the datas we need to analyze

calendar_data = pd.read_csv("/home/apprenant/Documents/Brief-12-Airbnb/data/01_raw/calendar.csv")
listings_data = pd.read_csv("/home/apprenant/Documents/Brief-12-Airbnb/data/01_raw/listings.csv")
reviews_data = pd.read_csv("/home/apprenant/Documents/Brief-12-Airbnb/data/01_raw/reviews.csv")

print(calendar_data.head())
print("Il y a {} lignes et {} colonnes dans la base de données {}".format(calendar_data.shape[0], calendar_data.shape[1], namestr(calendar_data, globals())))

separator()

print(listings_data.head())
print("Il y a {} lignes et {} colonnes dans la base de données {}".format(listings_data.shape[0], listings_data.shape[1], namestr(listings_data, globals())))

separator()

print(reviews_data.head())
print("Il y a {} lignes et {} colonnes dans la base de données {}".format(reviews_data.shape[0], reviews_data.shape[1], namestr(reviews_data, globals())))

separator()

# 2. Checking of the duplicated values

# a. calendar_data

key_cols_calendar_data = ['listing_id', 'date', 'available', 'price', 'minimum_nights', 'maximum_nights']
calendar_data = calendar_data[key_cols_calendar_data]

# b. listings_data

key_cols_listings_data = ['id', 'host_id', 'host_name', 'host_response_time', 'host_response_rate', 'host_is_superhost', 'host_listings_count', 'neighbourhood_cleansed', 'latitude', 'longitude', 'property_type', 'room_type', 'accommodates', 'bathrooms_text', 'bedrooms', 'beds', 'price', 'minimum_nights', 'maximum_nights', 'has_availability', 'availability_365', 'number_of_reviews', 'review_scores_rating', 'review_scores_accuracy', 'review_scores_cleanliness', 'review_scores_checkin', 'review_scores_communication', 'review_scores_location', 'review_scores_value', 'reviews_per_month']
listings_data = listings_data[key_cols_listings_data]

# c. reviews_data

key_cols_reviews_data = ['listing_id', 'id', 'date', 'reviewer_id', 'reviewer_name']
reviews_data = reviews_data[key_cols_reviews_data]

# 3. Checking of the duplicated values

print(calendar_data.duplicated().value_counts())
print(listings_data.duplicated().value_counts())
print(reviews_data.duplicated().value_counts())
separator()

# 4. Checking of the value types

print(calendar_data.dtypes)
separator()
print(listings_data.dtypes)
separator()
print(reviews_data.dtypes)
separator()

# 5. Checking of the missing values

print(calendar_data.isnull().sum()) 
separator()
print(listings_data.isnull().sum()) 
separator()
print(reviews_data.isnull().sum()) 
separator()

# 6. Processing of the missing values

# a. calendar_data

calendar_data['price'] = calendar_data['price'].str.replace('$', '')
calendar_data['price'] = calendar_data['price'].str.replace(',', '')
calendar_data['price'] = calendar_data['price'].astype(float)
calendar_data['price'] = calendar_data['price'].fillna(calendar_data.price.mean())

calendar_data['minimum_nights'] = calendar_data['minimum_nights'].fillna(calendar_data.minimum_nights.mean())
calendar_data['maximum_nights'] = calendar_data['maximum_nights'].fillna(calendar_data.maximum_nights.mean())

# b. listings_data

listings_data['host_name'] = listings_data['host_name'].fillna('Not specified')
listings_data['host_is_superhost'] = listings_data['host_is_superhost'].fillna('Not specified')
listings_data['host_listings_count'] = listings_data['host_listings_count'].fillna(1)
listings_data['bathrooms_text'] = listings_data['bathrooms_text'].fillna('Not specified')
listings_data['bedrooms'] = listings_data['bedrooms'].fillna(method='bfill')
listings_data['beds'] = listings_data['beds'].fillna(method='bfill')
# listings_data['review_scores_rating'] = listings_data['review_scores_rating'].fillna(listings_data['review_scores_rating'].mean())
# listings_data['review_scores_accuracy'] = listings_data['review_scores_accuracy'].fillna(listings_data['review_scores_accuracy'].mean())
# listings_data['review_scores_cleanliness'] = listings_data['review_scores_cleanliness'].fillna(listings_data['review_scores_cleanliness'].mean())
# listings_data['review_scores_checkin'] = listings_data['review_scores_checkin'].fillna(listings_data['review_scores_checkin'].mean())
# listings_data['review_scores_communication'] = listings_data['review_scores_communication'].fillna(listings_data['review_scores_communication'].mean())
# listings_data['review_scores_location'] = listings_data['review_scores_location'].fillna(listings_data['review_scores_location'].mean())
# listings_data['review_scores_value'] = listings_data['review_scores_value'].fillna(listings_data['review_scores_value'].mean())
# listings_data['reviews_per_month'] = listings_data['reviews_per_month'].fillna(listings_data['reviews_per_month'].mean())

# 7. Handle the types of our variables

# a. calendar_data

calendar_data['date'] = pd.to_datetime(calendar_data['date'])
print(calendar_data.dtypes)
separator()

# b. listings_data

listings_data['host_response_rate'] = pd.to_numeric(listings_data['host_response_rate'].str.strip('%'))
listings_data['price'] = listings_data['price'].str.replace('$', '')
listings_data['price'] = listings_data['price'].str.replace(',', '')
listings_data['price'] = listings_data['price'].astype(float)
print(listings_data.dtypes)
separator()

# c. reviews_data

reviews_data['date'] = pd.to_datetime(reviews_data['date'])
print(reviews_data.dtypes)
separator()

# 8. Recording of the cleaned data

cleaned_calendar_data = calendar_data.to_csv("/home/apprenant/Documents/Brief-12-Airbnb/data/02_intermediate/cleaned_calendar.csv")
cleaned_listings_data = listings_data.to_csv("/home/apprenant/Documents/Brief-12-Airbnb/data/02_intermediate/cleaned_listings.csv")
cleaned_reviews_data = reviews_data.to_csv("/home/apprenant/Documents/Brief-12-Airbnb/data/02_intermediate/cleaned_reviews.csv")