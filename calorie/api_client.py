import requests

def get_calories_prediction(data):
    API_URL = "http://127.0.0.1:5000/predict"
    
    try:
        # Make the POST request with a timeout (e.g., 10 seconds)
        response = requests.post(API_URL, json=data, timeout=10)
        
        # Check if the request was successful
        if response.status_code == 200:
            return response.json()
        else:
            # If the status code is not 200, return an error message
            return {"error": f"API call failed with status code {response.status_code}"}
    
    except requests.exceptions.Timeout:
        return {"error": "Request timed out. Please try again later."}
    
    except requests.exceptions.RequestException as e:
        # Handle general errors such as connection issues
        return {"error": f"An error occurred: {str(e)}"}
