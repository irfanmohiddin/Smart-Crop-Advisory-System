# config.py
import os


class Config:
    """Application configuration"""

    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'

    # Weather API settings
    WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY') or 'YOUR_API_KEY_HERE'

    # Model paths
    MODEL_PATH = 'models/crop_model.pkl'
    SCALER_PATH = 'models/scaler.pkl'
    DATA_PATH = 'data/Crop_recommendation.csv'

    # Application settings
    DEBUG = True
    CROPS_SUPPORTED = ['Rice', 'Wheat', 'Maize', 'Cotton', 'Chickpea']


# For easy access
WEATHER_API_KEY = 'REPLACE THIS WITH YOUR ACTUAL API KEY'  # ← REPLACE THIS WITH YOUR ACTUAL API KEY
