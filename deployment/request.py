import requests

url = 'http://localhost:5000/predict'

r = requests.post(url,json={'Hour':20, 'Dew point temperature (°C)':9, 'Temperature (°C)':3, 'Humidity (%)':37, 'Wind Speed (m/s)':2, 'Visibility (10m)':2000, 'Rainfall (mm)':0, 'Snowfall (cm)':0, 'Season':'Autumn', 'Holiday':'No Holiday', 'Functioning Day':'Yes', 'Solar Radiation (MJ/m2)':0})

print(r.json())
