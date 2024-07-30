# This program tracks the exercises a user performs and logs them into a Google Sheet using the Sheety API.
# It takes user input for the exercises performed, sends this data to the Nutritionix API to get details about the exercises,
# and then logs the exercise details such as date, time, exercise name, duration, and calories burned into a Google Sheet.

import requests
from datetime import datetime

# User details and API credentials
GENDER = "Male"        # gender
WEIGHT_KG = "64"       # weight in kg
HEIGHT_CM = "174"      # height in cm
AGE = "19"             # age

API_KEY = ""
APP_ID = "0be6e594"
sheet_endpoint = "https://api.sheety.co/**************/myWorkoutsReal/workouts"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Get exercise details from user input
exercise_text = input("Tell me which exercises you did: ")

# Set up headers for the Nutritionix API request
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

# Set up parameters for the Nutritionix API request
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# Send the request to the Nutritionix API and get the response
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

# Get the current date and time
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Loop through the exercises and log each one into the Google Sheet using the Sheety API
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # Send the request to the Sheety API to log the exercise
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    # Print the response from the Sheety API
    print(sheet_response.text)
