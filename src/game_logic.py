import json
import os

# Directory to store scores for different group chats
SCORES_DIR = "scores"

def get_group_scores_file(group_id):
    """Generate the file path for the given group chat's scores."""
    if not os.path.exists(SCORES_DIR):
        os.makedirs(SCORES_DIR)  # Ensure the directory exists
    return os.path.join(SCORES_DIR, f"{group_id}_scores.json")

def load_scores(group_id):
    """Load scores for a specific group chat from its JSON file."""
    scores_file = get_group_scores_file(group_id)
    if not os.path.exists(scores_file):
        save_scores({}, group_id)  # Create a new file with an empty dictionary

    try:
        with open(scores_file, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, ValueError):
        # Handle cases where the file is invalid or empty
        save_scores({}, group_id)  # Reset to an empty dictionary
        return {}

def save_scores(scores, group_id):
    """Save scores for a specific group chat to its JSON file."""
    scores_file = get_group_scores_file(group_id)
    with open(scores_file, 'w') as f:
        json.dump(scores, f, indent=4)

def update_score(group_id, user_id, username, loudness):
    """Update the user's score only if it's their highest attempt."""
    new_best = False
    scores = load_scores(group_id)

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
    save_scores(scores, group_id)

    return new_best

def get_all_scores(group_id):
    """Retrieve and format all scores for a specific group chat."""
    scores = load_scores(group_id)
    if not scores:
        return "No scores have been recorded yet."

    # Format the scores as a list of "username: loudness pts"
    formatted_scores = [
        f"{details['username']}: {details['loudness']} pts"
        for user_id, details in scores.items()
    ]
    return "\n".join(formatted_scores)

def get_current_rankings(group_id):
    """Retrieve and format the current top 3 rankings for a specific group chat."""
    scores = load_scores(group_id)

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

def clear_scores(group_id):
    """Clear all scores for a specific group chat."""
    save_scores({}, group_id)  # Reset to an empty dictionary

def is_first_time(group_id, user_id) -> bool:
    """Check if this user is playing for the first time in the group."""
    scores = load_scores(group_id)
    user_id_str = str(user_id)
    return user_id_str not in scores
