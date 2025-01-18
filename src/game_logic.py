# scores = {}
import json
import os

# File to store scores
SCORES_FILE = "scores.json"

# Ensure the scores file exists
if not os.path.exists(SCORES_FILE):
    with open(SCORES_FILE, 'w') as f:
        json.dump({}, f)  # Initialize with an empty dictionary

def load_scores():
    """Load scores from the JSON file."""
    with open(SCORES_FILE, 'r') as f:
        return json.load(f)

def save_scores(scores):
    """Save scores to the JSON file."""
    with open(SCORES_FILE, 'w') as f:
        json.dump(scores, f, indent=4)

def update_score(user_id, username, loudness):
    """Update the user's score in the scores dictionary."""
    scores = load_scores()
    scores[user_id] = {"username": username, "loudness": loudness}
    save_scores(scores)

def get_all_scores():
    """Retrieve and format all scores for display."""
    scores = load_scores()
    if not scores:
        return "No scores have been recorded yet."

    # Format the scores as a list of "username: loudness pts"
    formatted_scores = [
        f"{details['username']}: {details['loudness']} pts"
        for user_id, details in scores.items()
    ]
    return "\n".join(formatted_scores)


def get_current_rankings():
    """Generate a string of current rankings sorted by loudness."""
    scores = load_scores()
    sorted_scores = sorted(scores.items(), key=lambda x: x[1]['loudness'], reverse=True)
    rankings = "\n".join([f"{score[1]['username']}: {score[1]['loudness']} pts" for score in sorted_scores])
    return rankings if rankings else "No rankings yet!"

def clear_scores():
    """Clear all scores."""
    with open(SCORES_FILE, 'w') as f:
        json.dump({}, f)  # Reset to an empty dictionary