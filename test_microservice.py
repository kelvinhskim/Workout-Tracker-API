import requests
import json

# Base URL for the microservice
BASE_URL = "http://localhost:5000"

def test_record_workout():
    """
    Test the POST /record-workout endpoint to record a workout.
    """
    print("\n--- Testing Record Workout ---")
    url = f"{BASE_URL}/record-workout"
    data = {
        "exercise_name": "bench press",
        "sets": 3,
        "reps": 12
    }
    try:
        response = requests.post(url, json=data)
        print("Request Payload:")
        print(json.dumps(data, indent=4))  # Pretty-print the request payload
        print("\nResponse Status Code:", response.status_code)
        print("\nResponse JSON:")
        print(json.dumps(response.json(), indent=4))  # Pretty-print the response JSON
    except Exception as e:
        print("Error:", str(e))


def test_view_workouts():
    """
    Test the GET /view-workouts endpoint to view all recorded workouts.
    """
    print("\n--- Testing View Workouts ---")
    url = f"{BASE_URL}/view-workouts"
    try:
        response = requests.get(url)
        print("\nResponse Status Code:", response.status_code)
        print("\nResponse JSON:")
        print(json.dumps(response.json(), indent=4))  # Pretty-print the response JSON
    except Exception as e:
        print("Error:", str(e))


def test_retrieve_progress():
    """
    Test the GET /retrieve-progress endpoint to retrieve progress over a date range.
    """
    print("\n--- Testing Retrieve Progress ---")
    url = f"{BASE_URL}/retrieve-progress"
    params = {
        "start_date": "2024-01-01",
        "end_date": "2024-12-31"
    }
    try:
        response = requests.get(url, params=params)
        print("Request Parameters:")
        print(json.dumps(params, indent=4))  # Pretty-print the request parameters
        print("\nResponse Status Code:", response.status_code)
        print("\nResponse JSON:")
        print(json.dumps(response.json(), indent=4))  # Pretty-print the response JSON
    except Exception as e:
        print("Error:", str(e))


def test_invalid_record_workout():
    """
    Test the POST /record-workout endpoint with invalid data to validate error handling.
    """
    print("\n--- Testing Invalid Record Workout ---")
    url = f"{BASE_URL}/record-workout"
    invalid_data = {
        "exercise_name": "",  # Invalid: empty string
        "sets": "three",      # Invalid: should be integer
        "reps": -10           # Invalid: should be a positive integer
    }
    try:
        response = requests.post(url, json=invalid_data)
        print("Request Payload:")
        print(json.dumps(invalid_data, indent=4))  # Pretty-print the invalid payload
        print("\nResponse Status Code:", response.status_code)

        # Handle JSON response or errors gracefully
        try:
            print("\nResponse JSON:")
            print(json.dumps(response.json(), indent=4))  # Pretty-print JSON response
        except ValueError:
            print("\nResponse is not in JSON format:")
            print(response.text)
    except Exception as e:
        print("Error:", str(e))


def test_invalid_retrieve_progress():
    """
    Test the GET /retrieve-progress endpoint with invalid date range to validate error handling.
    """
    print("\n--- Testing Invalid Retrieve Progress ---")
    url = f"{BASE_URL}/retrieve-progress"
    invalid_params = {
        "start_date": "2024-31-01",  # Invalid: wrong format
        "end_date": "not-a-date"    # Invalid: not a valid date
    }
    try:
        response = requests.get(url, params=invalid_params)
        print("Request Parameters:")
        print(json.dumps(invalid_params, indent=4))  # Pretty-print the invalid parameters
        print("\nResponse Status Code:", response.status_code)

        # Handle JSON response or errors gracefully
        try:
            print("\nResponse JSON:")
            print(json.dumps(response.json(), indent=4))  # Pretty-print JSON response
        except ValueError:
            print("\nResponse is not in JSON format:")
            print(response.text)
    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    print("--- Starting Microservice Test Program ---")
    test_record_workout()         # Test recording a valid workout
    test_view_workouts()          # Test viewing all recorded workouts
    test_retrieve_progress()      # Test retrieving progress with valid dates
    test_invalid_record_workout() # Test recording an invalid workout
    test_invalid_retrieve_progress() # Test retrieving progress with invalid dates
    print("--- Test Program Finished ---")
