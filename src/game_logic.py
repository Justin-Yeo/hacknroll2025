scores = {}

def update_score(user_id, username, loudness):
    scores[user_id] = {"username": username, "loudness": loudness}

def get_current_rankings():
    sorted_scores = sorted(scores.items(), key=lambda x: x[1]['loudness'], reverse=True)
    rankings = "\n".join([f"{score[1]['username']}: {score[1]['loudness']} dB" for score in sorted_scores])
    return rankings

def clear_scores():
    scores.clear()