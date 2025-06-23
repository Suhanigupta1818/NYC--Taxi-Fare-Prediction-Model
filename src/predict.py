import pickle
import pandas as pd
from .preprocess import preprocess_data, input_cols
import requests
import os

def download_model(url, local_path='model.pkl'):
    if not os.path.exists(local_path):
        response = requests.get(url)
        if response.status_code == 200:
            with open(local_path, 'wb') as f:
                f.write(response.content)
        else:
            raise Exception(f"Failed to download model from {url}. Status code: {response.status_code}")
    return local_path

def load_model():
    model_url = "https://drive.google.com/uc?export=download&id=1I5mJ9cpfyhuHLRrF0jNhs2M7mlSnVvSm"
    model_path = download_model(model_url)
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model

def predict_fare(pickup_lon, pickup_lat, dropoff_lon, dropoff_lat, passenger_count, pickup_datetime):
    model = load_model()
    input_data = {
        'pickup_longitude': pickup_lon,
        'pickup_latitude': pickup_lat,
        'dropoff_longitude': dropoff_lon,
        'dropoff_latitude': dropoff_lat,
        'passenger_count': passenger_count,
        'pickup_datetime': pd.to_datetime(pickup_datetime)
    }
    input_df = pd.DataFrame([input_data])
    input_df = preprocess_data(input_df, is_training=False)
    input_df = input_df[input_cols]
    fare = model.predict(input_df)[0]
    return max(fare, 2.5)  # Minimum fare