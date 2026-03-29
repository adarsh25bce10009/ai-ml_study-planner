POSITIVE_WORDS = ["good", "great", "fine", "ready", "motivated", "fresh", "happy", "energetic", "confident"]
NEGATIVE_WORDS = ["sick","tired", "stressed", "exhausted", "bad", "overwhelmed", "anxious", "nervous", "scared", "worried"]

def detect_mood(user_input):
    text = user_input.lower()
    words = text.split()

    positive_count = 0
    for word in words:
        if word in POSITIVE_WORDS:
            positive_count += 1

    negative_count = 0
    for word in words:
        if word in NEGATIVE_WORDS:
            negative_count += 1

    if positive_count > negative_count:
        mood = "positive"
        intensity = "high"
    elif negative_count > positive_count:
        mood = "negative"
        intensity = "light"
    else:
        mood = "neutral"
        intensity = "moderate"

    return mood, intensity