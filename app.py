# app.py
from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
from model_training import CropRecommendationModel
from weather_service import WeatherService
from crop_info import CropInformation
from config import WEATHER_API_KEY

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Initialize services
print("Loading crop recommendation model...")
crop_model = CropRecommendationModel()

# Check if model exists, if not train it
if os.path.exists('models/crop_model.pkl'):
    crop_model.load_model()
    print("✓ Model loaded successfully!")
else:
    print("⚠️  Model not found! Please run model_training.py first")

# Initialize weather service
weather_service = WeatherService(WEATHER_API_KEY)

# Initialize crop information
crop_info_service = CropInformation()


# Routes
@app.route('/')
def index():
    """Home page"""
    return render_template('index.html',
                           crops=crop_info_service.get_all_crops())


@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    """Crop recommendation page with manual input"""
    if request.method == 'POST':
        try:
            # Get form data
            print("\n" + "=" * 80)
            print("🔍 DEBUG: FORM DATA RECEIVED")
            print("=" * 80)
            print("RAW FORM DATA:")
            for key, value in request.form.items():
                print(f"  {key}: {value} (type: {type(value)})")

            input_data = {
                'N': float(request.form['nitrogen']),
                'P': float(request.form['phosphorus']),
                'K': float(request.form['potassium']),
                'temperature': float(request.form['temperature']),
                'humidity': float(request.form['humidity']),
                'ph': float(request.form['ph']),
                'rainfall': float(request.form['rainfall'])
            }

            print("\nPROCESSED INPUT DATA:")
            for key, value in input_data.items():
                print(f"  {key}: {value} (type: {type(value)})")

            # Validate inputs
            if any(v < 0 for v in input_data.values()):
                return render_template('recommend.html',
                                       error="All values must be positive numbers")

            # Get prediction
            print("\nCALLING MODEL.PREDICT()...")
            prediction, probabilities = crop_model.predict(input_data)

            print(f"\n✓ PREDICTION: {prediction}")
            print("TOP 5 PROBABILITIES:")
            for i, (crop, prob) in enumerate(probabilities[:5], 1):
                print(f"  {i}. {crop}: {prob * 100:.2f}%")
            print("=" * 80 + "\n")

            # Get crop information
            crop_details = crop_info_service.get_crop_info(prediction)

            # Get top 3 recommendations
            top_recommendations = []
            for crop, prob in probabilities[:3]:
                crop_detail = crop_info_service.get_crop_info(crop)
                top_recommendations.append({
                    'crop': crop,
                    'probability': round(prob * 100, 2),
                    'details': crop_detail
                })

            return render_template('result.html',
                                   prediction=prediction,
                                   crop_details=crop_details,
                                   recommendations=top_recommendations,
                                   input_data=input_data)

        except ValueError as e:
            print(f"\n❌ ERROR: {e}\n")
            return render_template('recommend.html',
                                   error="Please enter valid numeric values")
        except Exception as e:
            print(f"\n❌ EXCEPTION: {e}\n")
            import traceback
            traceback.print_exc()
            return render_template('recommend.html',
                                   error=f"An error occurred: {str(e)}")

    return render_template('recommend.html')


@app.route('/weather-recommend', methods=['GET', 'POST'])
def weather_recommend():
    """Weather-based crop recommendation"""
    if request.method == 'POST':
        try:
            print("\n" + "=" * 80)
            print("🔍 DEBUG: WEATHER-BASED RECOMMENDATION")
            print("=" * 80)

            city = request.form['city']
            print(f"City: {city}")

            N = float(request.form['nitrogen'])
            P = float(request.form['phosphorus'])
            K = float(request.form['potassium'])
            ph = float(request.form['ph'])

            print(f"User inputs - N: {N}, P: {P}, K: {K}, pH: {ph}")

            # Get weather data
            print(f"\nFetching weather for {city}...")
            weather_data = weather_service.get_weather_by_city(city)

            if not weather_data:
                return render_template('weather_recommend.html',
                                       error=f"Could not fetch weather data for '{city}'. Please check city name.")

            print(f"Weather data received:")
            print(f"  Temperature: {weather_data['temperature']}°C")
            print(f"  Humidity: {weather_data['humidity']}%")
            print(f"  Rainfall: {weather_data['rainfall']} mm")

            # Prepare input with weather data
            input_data = {
                'N': N,
                'P': P,
                'K': K,
                'temperature': weather_data['temperature'],
                'humidity': weather_data['humidity'],
                'ph': ph,
                'rainfall': weather_data['rainfall']
            }

            print(f"\nFINAL INPUT TO MODEL:")
            for key, value in input_data.items():
                print(f"  {key}: {value}")

            # Get prediction
            print("\nCALLING MODEL.PREDICT()...")
            prediction, probabilities = crop_model.predict(input_data)

            print(f"\n✓ PREDICTION: {prediction}")
            print("TOP 5 PROBABILITIES:")
            for i, (crop, prob) in enumerate(probabilities[:5], 1):
                print(f"  {i}. {crop}: {prob * 100:.2f}%")
            print("=" * 80 + "\n")

            crop_details = crop_info_service.get_crop_info(prediction)

            # Top recommendations
            top_recommendations = []
            for crop, prob in probabilities[:3]:
                crop_detail = crop_info_service.get_crop_info(crop)
                top_recommendations.append({
                    'crop': crop,
                    'probability': round(prob * 100, 2),
                    'details': crop_detail
                })

            return render_template('weather_result.html',
                                   prediction=prediction,
                                   crop_details=crop_details,
                                   recommendations=top_recommendations,
                                   weather=weather_data,
                                   input_data=input_data)

        except ValueError:
            return render_template('weather_recommend.html',
                                   error="Please enter valid numeric values")
        except Exception as e:
            print(f"\n❌ EXCEPTION: {e}\n")
            import traceback
            traceback.print_exc()
            return render_template('weather_recommend.html',
                                   error=f"An error occurred: {str(e)}")

    return render_template('weather_recommend.html')


@app.route('/crop-info/<crop_name>')
def crop_information(crop_name):
    """Detailed crop information page"""
    crop_details = crop_info_service.get_crop_info(crop_name)

    if crop_details:
        return render_template('crop_detail.html',
                               crop_name=crop_name,
                               details=crop_details)
    else:
        return "Crop information not found", 404


@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')


@app.route('/all-crops')
def all_crops():
    """Display all crops information"""
    all_crops_data = []
    for crop_name in crop_info_service.get_all_crops():
        details = crop_info_service.get_crop_info(crop_name)
        all_crops_data.append({
            'name': crop_name,
            'details': details
        })

    return render_template('all_crops.html', crops=all_crops_data)


# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


# Run the application
if __name__ == '__main__':
    print("\n" + "=" * 60)
    print("SMART CROP ADVISORY SYSTEM")
    print("=" * 60)
    print("Starting Flask application...")
    print("Open your browser and go to: http://127.0.0.1:5000")
    print("Press CTRL+C to stop the server")
    print("=" * 60 + "\n")

    app.run(debug=True, port=5000)