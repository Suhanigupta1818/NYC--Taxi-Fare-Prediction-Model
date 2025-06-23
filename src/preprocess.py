import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import random

# Define input_cols (list of features used for training and prediction)
input_cols = ['pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude', 'passenger_count',
              'pickup_datetime_year', 'pickup_datetime_month', 'pickup_datetime_day', 'pickup_datetime_weekday',
              'pickup_datetime_hour', 'trip_distance', 'jfk_drop_distance', 'lga_drop_distance', 'ewr_drop_distance',
              'met_drop_distance', 'wtc_drop_distance']

def load_data(file_path, sample_frac=0.01):
    selected_cols = ['fare_amount', 'pickup_datetime', 'pickup_longitude', 'pickup_latitude',
                     'dropoff_longitude', 'dropoff_latitude', 'passenger_count']
    dtypes = {
        'fare_amount': 'float32',
        'pickup_longitude': 'float32',
        'pickup_latitude': 'float32',
        'dropoff_longitude': 'float32',
        'dropoff_latitude': 'float32',
        'passenger_count': 'float32'
    }
    
    def skip_row(row_idx):
        if row_idx == 0:
            return False
        return random.random() > sample_frac
    
    random.seed(42)
    df = pd.read_csv(file_path, usecols=selected_cols, dtype=dtypes,
                     parse_dates=['pickup_datetime'], skiprows=skip_row)
    return df

def add_dateparts(df, col='pickup_datetime'):
    df[col + '_year'] = df[col].dt.year
    df[col + '_month'] = df[col].dt.month
    df[col + '_day'] = df[col].dt.day
    df[col + '_weekday'] = df[col].dt.weekday
    df[col + '_hour'] = df[col].dt.hour

def haversine_np(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat/2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2.0)**2
    c = 2 * np.arcsin(np.sqrt(a))
    km = 6367 * c
    return km

def add_trip_distance(df):
    df['trip_distance'] = haversine_np(df['pickup_longitude'], df['pickup_latitude'],
                                      df['dropoff_longitude'], df['dropoff_latitude'])

def add_landmark_dropoff_distance(df, landmark_name, landmark_lonlat):
    lon, lat = landmark_lonlat
    df[landmark_name + '_drop_distance'] = haversine_np(lon, lat, df['dropoff_longitude'], df['dropoff_latitude'])

def remove_outliers(df):
    return df[(df['fare_amount'] >= 1.) & (df['fare_amount'] <= 500.) &
              (df['pickup_longitude'] >= -75) & (df['pickup_longitude'] <= -72) &
              (df['dropoff_longitude'] >= -75) & (df['dropoff_longitude'] <= -72) &
              (df['pickup_latitude'] >= 40) & (df['pickup_latitude'] <= 42) &
              (df['dropoff_latitude'] >= 40) & (df['dropoff_latitude'] <= 42) &
              (df['passenger_count'] >= 1) & (df['passenger_count'] <= 6)]

def preprocess_data(df, is_training=True):
    add_dateparts(df)
    add_trip_distance(df)
    landmarks = {
        'jfk': (-73.7781, 40.6413),
        'lga': (-73.8740, 40.7769),
        'ewr': (-74.1745, 40.6895),
        'met': (-73.9632, 40.7794),
        'wtc': (-74.0099, 40.7126)
    }
    for name, lonlat in landmarks.items():
        add_landmark_dropoff_distance(df, name, lonlat)
    if is_training:
        df = remove_outliers(df)
    return df