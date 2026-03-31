POSITIVE_WORDS = ["good", "great", "fine", "ready", "motivated", "fresh", "happy", "energetic", "confident"]
NEGATIVE_WORDS = ["sick","tired", "stressed", "exhausted", "bad", "overwhelmed", "anxious", "nervous", "scared", "worried"]

def detect_mood(user_input):
    text = user_input.lower()
    words = text.split()

    pos_count = 0
    for word in words:
        if word in POSITIVE_WORDS:
            pos_count += 1

    neg_count = 0
    for word in words:
        if word in NEGATIVE_WORDS:
            neg_count += 1

    if pos_count > neg_count:
        mood = "positive"
        intensity = "high"
    elif neg_count > pos_count:
        mood = "negative"
        intensity = "light"
    else:
        mood = "neutral"
        intensity = "moderate"

    return mood, intensity
