import requests

# Base URL of the microservice
BASE_URL = "http://localhost:5000"

def test_record_workout():
    """Test recording a workout."""
    print("Test 1: Record a workout")
    record_data = {
        "exercise_name": "Push-up",
        "sets": 3,
        "reps": 10
    }
    try:
        response = requests.post(f"{BASE_URL}/record-workout", json=record_data)
        print("Request Data:", record_data)
        print("Response:", response.json())
    except Exception as e:
        print("Error during Test 1:", str(e))


def test_view_workouts():
    """Test viewing past workouts."""
    print("\nTest 2: View past workouts")
    try:
        response = requests.get(f"{BASE_URL}/view-workouts")
        print("Response:", response.json())
    except Exception as e:
        print("Error during Test 2:", str(e))


def test_retrieve_progress():
    """Test retrieving progress over a date range."""
    print("\nTest 3: Retrieve progress over a date range")
    params = {
        "start_date": "2024-01-01",
        "end_date": "2024-12-31"
    }
    try:
        response = requests.get(f"{BASE_URL}/retrieve-progress", params=params)
        print("Request Parameters:", params)
        print("Response:", response.json())
    except Exception as e:
        print("Error during Test 3:", str(e))


if __name__ == "__main__":
    print("Starting test program...")
    test_record_workout()
    test_view_workouts()
    test_retrieve_progress()
    print("\nTest program finished.")