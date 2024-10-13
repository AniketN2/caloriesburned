from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS

# Load the trained model
model = joblib.load('calories.pkl')

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Define the endpoint for prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json()

        # Extract input features from JSON data
        features = np.array([[
            data['Age'],
            data['Height'],
            data['Weight'],
            data['Duration'],
            data['Heart_Rate'],
            data['Body_Temp']
        ]])

        # Make prediction
        prediction = model.predict(features)

        # Return the result as JSON
        return jsonify({'Calories': prediction[0]})

    except Exception as e:
        return jsonify({'error': str(e)})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
