from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

# Assuming your friend's API is accessible via an endpoint
API_URL = "http://127.0.0.1:5000/predict"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_calories():
    # Fetch data from form
    weight = request.form['weight']
    height = request.form['height']
    age = request.form['age']
    duration = request.form['duration']
    heartrate = request.form['heartrate']
    btemp = request.form['btemp']

    # Prepare data for the API
    data = {
        'Age': age,
        'Height': height,
        'Weight': weight,
        'Duration': duration,
        'Heart_Rate': heartrate,
        'Body_Temp': btemp     
    }

    # Make a POST request to your friend's API
    response = requests.post(API_URL, json=data)
    result = response.json()

    # Render the result page with the API response
    return render_template('result.html', calories_burned=result['Calories'])

if __name__ == '__main__':
    app.run(debug=True)


