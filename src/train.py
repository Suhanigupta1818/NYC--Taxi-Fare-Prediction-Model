from preprocess import load_data, preprocess_data
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error
import pickle
import numpy as np

input_cols = ['pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude', 'passenger_count',
              'pickup_datetime_year', 'pickup_datetime_month', 'pickup_datetime_day', 'pickup_datetime_weekday',
              'pickup_datetime_hour', 'trip_distance', 'jfk_drop_distance', 'lga_drop_distance', 'ewr_drop_distance',
              'met_drop_distance', 'wtc_drop_distance']
target_col = 'fare_amount'

def train_model(train_data_path):
    df = load_data(train_data_path)
    df = preprocess_data(df)
    
    train_df, val_df = train_test_split(df, test_size=0.2, random_state=42)
    train_df = train_df.dropna()
    val_df = val_df.dropna()
    
    models = {
        'Ridge': Ridge(random_state=42),
        'XGBoost': XGBRegressor(random_state=42, n_jobs=-1, objective='reg:squarederror',
                                n_estimators=500, max_depth=5, learning_rate=0.1,
                                subsample=0.8, colsample_bytree=0.8)
    }
    
    best_model = None
    best_rmse = float('inf')
    for name, model in models.items():
        model.fit(train_df[input_cols], train_df[target_col])
        train_preds = model.predict(train_df[input_cols])
        val_preds = model.predict(val_df[input_cols])
        train_rmse = np.sqrt(mean_squared_error(train_df[target_col], train_preds))
        val_rmse = np.sqrt(mean_squared_error(val_df[target_col], val_preds))
        print(f"{name} Train RMSE: {train_rmse:.2f}, Val RMSE: {val_rmse:.2f}")
        if val_rmse < best_rmse:
            best_rmse = val_rmse
            best_model = model
    
    with open('src/model.pkl', 'wb') as f:
        pickle.dump(best_model, f)

if __name__ == "__main__":
    train_model('data/train.csv')