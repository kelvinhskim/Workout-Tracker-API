from flask import Flask, request, jsonify
import os
import json
from datetime import datetime

app = Flask(__name__)

# File to store workout data
WORKOUT_FILE = "workout_data.json"

# Ensure the file exists
if not os.path.exists(WORKOUT_FILE):
    with open(WORKOUT_FILE, 'w') as f:
        json.dump([], f)


def load_workouts():
    """Load workouts from the file."""
    with open(WORKOUT_FILE, 'r') as f:
        return json.load(f)


def save_workouts(data):
    """Save workouts to the file."""
    with open(WORKOUT_FILE, 'w') as f:
        json.dump(data, f)


@app.route('/record-workout', methods=['POST'])
def record_workout():
    """Endpoint to record a workout."""
    try:
        data = request.get_json()
        exercise_name = data.get("exercise_name")
        sets = data.get("sets")
        reps = data.get("reps")

        # Validate input
        if not exercise_name or not isinstance(sets, int) or not isinstance(reps, int):
            return jsonify({"status": "error", "message": "Invalid input data"}), 400

        # Load existing data
        workouts = load_workouts()

        # Append new workout
        workout = {
            "exercise_name": exercise_name,
            "sets": sets,
            "reps": reps,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        workouts.append(workout)
        save_workouts(workouts)

        return jsonify({
            "status": "success",
            "message": "Workout recorded successfully",
            "workout_details": workout
        }), 200
    except Exception as e:
        return jsonify({"status": "error", "message": f"An error occurred: {str(e)}"}), 500


@app.route('/view-workouts', methods=['GET'])
def view_workouts():
    """Endpoint to view past workouts."""
    try:
        workouts = load_workouts()
        return jsonify({
            "status": "success",
            "workout_history": workouts
        }), 200
    except Exception as e:
        return jsonify({"status": "error", "message": f"An error occurred: {str(e)}"}), 500


@app.route('/retrieve-progress', methods=['GET'])
def retrieve_progress():
    """Endpoint to retrieve workout progress over a specified period."""
    try:
        start_date = request.args.get("start_date")
        end_date = request.args.get("end_date")

        if not start_date or not end_date:
            return jsonify({"status": "error", "message": "Start and end dates are required"}), 400

        # Load and filter workouts
        workouts = load_workouts()
        filtered_workouts = [
            w for w in workouts
            if start_date <= w["date"][:10] <= end_date
        ]

        # Calculate stats
        total_sets = sum(w["sets"] for w in filtered_workouts)
        total_reps = sum(w["reps"] for w in filtered_workouts)
        average_reps_per_set = total_reps / total_sets if total_sets > 0 else 0

        return jsonify({
            "status": "success",
            "progress_stats": {
                "total_sets": total_sets,
                "total_reps": total_reps,
                "average_reps_per_set": average_reps_per_set
            }
        }), 200
    except Exception as e:
        return jsonify({"status": "error", "message": f"An error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True)