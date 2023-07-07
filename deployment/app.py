import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input values from the user's request
    hour = int(request.form['hour'])
    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    windspeed = float(request.form['windspeed'])
    visibility = float(request.form['visibility'])
    dew_point_temp = float(request.form['dew_point_temp'])
    solar_radiation = float(request.form['solar_radiation'])
    rainfall = float(request.form['rainfall'])
    snowfall = float(request.form['snowfall'])
    seasons = request.form['seasons']
    holiday = request.form['holiday']
    functioning_day = request.form['functioning_day']

    # Perform the necessary encoding for categorical variables
    seasons_winter = 1 if seasons == 'Winter' else 0
    seasons_spring = 1 if seasons == 'Spring' else 0
    seasons_summer = 1 if seasons == 'Summer' else 0
    seasons_autumn = 1 if seasons == 'Autumn' else 0
    holiday = 1 if holiday == '1' else 0
    functioning_day = 1 if functioning_day == '1' else 0

    # Prepare the input features as a list
    input_features = [hour, temperature, humidity, windspeed, visibility, dew_point_temp,
                      solar_radiation, rainfall, snowfall, seasons_winter, seasons_spring,
                      seasons_summer, seasons_autumn, holiday, functioning_day, 0, 0]

    # Perform the prediction using the loaded model
    prediction = model.predict([input_features])

    # Convert the prediction to an integer
    prediction = int(prediction[0])

     # Return the prediction result as JSON
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
