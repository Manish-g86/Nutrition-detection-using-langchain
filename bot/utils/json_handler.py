import json

# ------------------------------ USER PROFILE HANDLERS ------------------------------

def load_profiles():
    """Load user profile data from the JSON file."""
    try:
        with open('data/user_profiles.json', 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return {}  # Return an empty dictionary if the file doesn't exist

def save_profiles(profiles):
    """Save user profile data to the JSON file."""
    with open('data/user_profiles.json', 'w') as json_file:
        json.dump(profiles, json_file, indent=4)

# ------------------------------ MEAL TRACKER HANDLERS ------------------------------

def load_meal_data():
    """Load meal tracker data from the JSON file."""
    try:
        with open('meal_tracker.json', 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return {}  # Return an empty dictionary if the file doesn't exist

def save_meal_data(meal_tracker):
    """Save meal tracker data to the JSON file."""
    with open('meal_tracker.json', 'w') as json_file:
        json.dump(meal_tracker, json_file, indent=4)

def add_meal_data(user_id, current_date, breakfast, lunch, dinner):
    """Add meal data for the user."""
    # Load the existing meal tracker data
    meal_tracker = load_meal_data()

    # Check if user_id already exists in meal_tracker
    if user_id not in meal_tracker:
        meal_tracker[user_id] = {}

    # Add the meal data for the specific date
    meal_tracker[user_id][current_date] = {
        "breakfast": breakfast if breakfast != "not eaten" else "not eaten",
        "lunch": lunch if lunch != "not eaten" else "not eaten",
        "dinner": dinner if dinner != "not eaten" else "not eaten"
    }

    # Save the updated meal_tracker
    save_meal_data(meal_tracker
