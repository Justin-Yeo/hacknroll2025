# Store scores for each group chat separately
group_scores = {}

def update_score(chat_id, user_id, username, loudness):
    """Update the score for a user in a specific group."""
    if chat_id not in group_scores:
        group_scores[chat_id] = {}
    group_scores[chat_id][user_id] = {"username": username, "loudness": loudness}

def get_current_rankings(chat_id):
    """Get the current rankings for a specific group."""
    if chat_id not in group_scores or not group_scores[chat_id]:
        return "No scores yet. Send a voice message to participate!"
    
    sorted_scores = sorted(
        group_scores[chat_id].items(), key=lambda x: x[1]['loudness'], reverse=True
    )
    rankings = "\n".join(
        [f"{score[1]['username']}: {score[1]['loudness']} pts" for score in sorted_scores]
    )
    return rankings

def clear_scores(chat_id):
    """Clear scores for a specific group."""
    if chat_id in group_scores:
        group_scores.pop(chat_id)

def clear_all_scores():
    """Clear scores for all groups (optional admin use)."""
    group_scores.clear()