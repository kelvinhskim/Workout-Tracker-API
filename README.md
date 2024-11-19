# **Workout Progress Microservice**

## **Overview**

This microservice allows users to record workout progress, view workout history, and analyze workout statistics. It is designed to be accessed programmatically using HTTP POST and GET requests, providing structured JSON responses for all interactions.


#
## **Communication Contract**

**How to Programmatically Request Data**

To interact with the microservice, use the following endpoints:

**1. Record a workout**

**Endpoint**
```
POST http://localhost:5000/record-workout
```
**2. View Workout History**

**Endpoint**
```
GET http://localhost:5000/view-workouts
```

**3. Retrieve Workout Progress**

**Endpoint**
```
GET http://localhost:5000/retrieve-progress
```
#
## **Request Format**

**1. Record a Workout**
- The request payload must be in JSON format and include:
  - exercise_name (string): Name of the exercise performed.
  - sets (integer): Number of sets completed.
  - reps (integer): Number of reps per set.

**json Example Request Payload**
```
{
    "exercise_name": "Push-up",
    "sets": 3,
    "reps": 10
}
```
**Python Example for Sending Request**
```
import requests

# Microservice endpoint
url = "http://localhost:5000/record-workout"

# Request payload
data = {
    "exercise_name": "Push-up",
    "sets": 3,
    "reps": 10
}

# Send POST request
response = requests.post(url, json=data)

# Print the response
print(response.json())
```
#
**2. View Workout History**

No additional payload is required.

**Python Example for Sending Request**
```
import requests

# Microservice endpoint
url = "http://localhost:5000/view-workouts"

# Send GET request
response = requests.get(url)

# Print the response
print(response.json())
```
#
**3. Retrieve Workout Progress**
- Requires query parameters:
  - start_date (string): Start date in YYYY-MM-DD format.
  - end_date (string): End date in YYYY-MM-DD format.

**Example Query Parameters:**
```
?start_date=2024-01-01&end_date=2024-12-31
```

**Python Example for Sending Request:**
```
import requests

# Microservice endpoint
url = "http://localhost:5000/retrieve-progress"

# Query parameters
params = {
    "start_date": "2024-01-01",
    "end_date": "2024-12-31"
}

# Send GET request
response = requests.get(url, params=params)

# Print the response
print(response.json())
```
#
**How to Programmatically Receive Data**

The microservice will respond with structured JSON data. Below are examples of success and error responses.

**Successful Response**

For a valid request, the microservice will return:

- status: "success".
- message: A descriptive success message.
- Relevant data (e.g., recorded workout details, workout history, or progress statistics).

**Example Success Response (Record Workout):**
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
**Error Response**

For an invalid request, the microservice will return:

- status: "error".
- message: A description of the error.

**Example Error Response:**
```
{
    "status": "error",
    "message": "Invalid input data"
}
```
#
**Example Response Handling in Python**

The following Python code demonstrates how to handle the response:
```
response = requests.post(url, json=data)

# Check response status
if response.status_code == 200:
    # Success
    print("Success Response:", response.json())
else:
    # Error
    print("Error Response:", response.json())
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
