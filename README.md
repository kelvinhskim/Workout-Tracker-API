# **Workout Tracker API**

## **Overview**

A production-ready REST API that records set/rep workouts, returns history, and computes date-ranged progress metrics with validation and JSON responses. (Python + Flask)


#
## **Communication Contract**

**How to Programmatically Request Data**

To interact with the microservice, use the following endpoints:

**1. Record a workout**

 - **Method**

   POST

- **Endpoint**
```
http://localhost:5000/record-workout
```

- **Request Format:**
  -   JSON payload with the following fields:
      -  exercise_name (string): Name of the exercise performed.
      -  sets (integer): Number of sets completed.
      -  reps (integer): Number of reps per set.
 
**Example Request**
```
import requests

url = "http://localhost:5000/record-workout"
data = {
    "exercise_name": "Push-up",
    "sets": 3,
    "reps": 10
}
response = requests.post(url, json=data)
print(response.json())
```

**2. View Workout History**

 - **Method**

   GET

- **Endpoint**
```
http://localhost:5000/view-workouts
```

- **Request Format**: No additional payload is required.

**Example Request**
```
import requests

url = "http://localhost:5000/view-workouts"
response = requests.get(url)
print(response.json())
```

**3. Retrieve Workout Progress**

 - **Method**

   GET
   
- **Endpoint**
```
http://localhost:5000/retrieve-progress
```

- **Query Parameters:**
    - start_date (string): Start date in YYYY-MM-DD format.
    - end_date (string): End date in YYYY-MM-DD format.
 
**Example Request**
```
import requests

url = "http://localhost:5000/retrieve-progress"
params = {"start_date": "2024-01-01", "end_date": "2024-12-31"}
response = requests.get(url, params=params)
print(response.json())
```
#
**How to Programmatically Receive Data**

The microservice will return structured JSON responses for all requests.

**1. Record Workout Response**
  - **Successful Response**
```
{
  "status": "success",
  "message": "Workout recorded successfully",
  "workout_details": {
    "exercise_name": "Push-up",
    "sets": 3,
    "reps": 10,
    "date": "2024-12-01 10:00:00"
  }
}
```
 - **On Error**
```
{
  "status": "error",
  "message": "Invalid input data"
}
```
**2. View Workout History Response**
  - **Successful Response**
```
{
  "status": "success",
  "workout_history": [
    {
      "exercise_name": "Push-up",
      "sets": 3,
      "reps": 10,
      "date": "2024-12-01 10:00:00"
    }
  ]
}
```
**3. Retrieve Workout Progress Response**
  - **Successful Response**
```
{
  "status": "success",
  "progress_stats": {
    "total_sets": 3,
    "total_reps": 10,
    "average_reps_per_set": 3.33
  }
}
```
  - **On Error**
```
{
  "status": "error",
  "message": "Invalid date range"
}
```

**Example Response Handling:**
```
response = requests.post(url, json=data)

if response.status_code == 200:
    print("Response:", response.json())
else:
    print("Error:", response.json())
```

#
## **UML Sequence Diagram**

Below is a UML sequence diagram that explains how requesting and receiving data works between the test program and the microservice:

![alt text](https://github.com/kelvinhskim/CS-361---Assignment-8/blob/main/UML%20Sequence%20Diagram%20-%20Workout%20Tracker.png)

#
## **Notes**

**- Starting the Microservice:**
  - Ensure the microservice is running at http://localhost:5000 before making requests. Start it by running:
```
python app.py
```

**- Validation Rules:**
  - exercise_name: Must be a non-empty string.
  - sets and reps: Must be integers.
  - start_date and end_date: Must follow the YYYY-MM-DD format.

**- Error Handling:**
  - Always check for errors in the response and handle them appropriately in your code.
#
