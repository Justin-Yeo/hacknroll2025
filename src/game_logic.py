import json
import os

# File to store scores
SCORES_FILE = "scores.json"

def load_scores():
    """Load scores from the JSON file, initializing if empty or invalid."""
    if not os.path.exists(SCORES_FILE):
        save_scores({})  # Create a new file with an empty dictionary

    try:
        with open(SCORES_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, ValueError):
        # Handle cases where the file is invalid or empty
        save_scores({})  # Reset to an empty dictionary
        return {}

def save_scores(scores):
    """Save scores to the JSON file."""
    with open(SCORES_FILE, 'w') as f:
        json.dump(scores, f, indent=4)

def update_score(user_id, username, loudness):
    """Update the user's score only if it's their highest attempt."""
    new_best = False
    scores = load_scores()

    user_id_str = str(user_id)

    if user_id_str in scores:
        current_best = scores[user_id_str]["loudness"]
        if loudness > current_best:
            scores[user_id_str]["loudness"] = loudness
            new_best = True
    else:
        scores[user_id_str] = {"username": username, "loudness": loudness}
        new_best = True

    # Always update username in case it changed
    scores[user_id_str]["username"] = username
    save_scores(scores)

    return new_best


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
    """Retrieve and format the current top 3 rankings based on loudness."""
    scores = load_scores()  # Load scores from the JSON file

    if not scores:  # Check if scores are empty or not present
        return "No scores available yet. Start playing to see rankings!"

    # Sort scores by loudness in descending order
    sorted_scores = sorted(scores.items(), key=lambda x: x[1]['loudness'], reverse=True)

    # Format the top 3 scores
    rankings = [
        f"{i + 1}️⃣ {score[1]['username']}: {score[1]['loudness']} pts"
        for i, score in enumerate(sorted_scores[:3])
    ]
    rankings_message = "\n".join(rankings)

    # Create the response message
    response = f"""
🎉 Loudness Game Results 🎉
🏆 Current Rankings:
{rankings_message}

Keep it loud! 🎤
"""
    return response

def clear_scores():
    """Clear all scores."""
    save_scores({})  # Reset to an empty dictionary

def is_first_time(user_id) -> bool:
    """Check if this user is playing for the first time based on our scores."""
    scores = load_scores()  
    user_id_str = str(user_id)
    return user_id_str not in scores
