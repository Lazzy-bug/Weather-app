from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'e1b292964b3c86ad361260f80c9496e0'  # Replace with your OpenWeatherMap API key

def get_real_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()
    print(data)  # Debugging: Print the API response
    if response.status_code == 200:
        weather_data = {
            'city': data['name'],
            'temperature': f"{data['main']['temp']}°C",
            'condition': data['weather'][0]['description'].capitalize()
        }
    else:
        weather_data = {
            'city': city,
            'temperature': 'N/A',
            'condition': 'N/A'
        }
    return weather_data

@app.route('/')
def index():
    city = request.args.get('city', 'San Francisco')
    weather_data = get_real_weather(city)
    return render_template('index.html', weather_data=weather_data)

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city', 'San Francisco')
    weather_data = get_real_weather(city)
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
