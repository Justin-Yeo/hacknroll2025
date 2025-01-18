scores = {}

def update_score(user_id, username, loudness):
    scores[user_id] = {"username": username, "loudness": loudness}

def get_current_rankings():
    sorted_scores = sorted(scores.items(), key=lambda x: x[1]['loudness'], reverse=True)
    rankings = [
        f"{i+1}️⃣ {score[1]['username']}: {score[1]['loudness']} pts"
        for i, score in enumerate(sorted_scores[:3])
    ]
    rankings_message = "\n".join(rankings)
    response = f"""
🎉 Loudness Game Results 🎉
🏆 Current Rankings:
{rankings_message}

Keep it loud! 🎤
"""
    return response

def clear_scores():
    scores.clear()