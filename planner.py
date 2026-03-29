from data import SUBJECTS

def calculate_priority(subject):
    difficulty = subject["difficulty"]
    urgency = 10 - subject["days_until_exam"]  # fewer days = higher urgency
    priority_score = (difficulty * 0.6) + (urgency * 0.4)
    return round(priority_score, 2)

def adjust_hours_by_mood(hours_available, intensity):
    if intensity == "high":
        return hours_available          # full study session
    elif intensity == "moderate":
        return int(hours_available * 0.8)   # 80% of available hours
    else:
        return int(hours_available * 0.6)   # light session, 60%

def generate_schedule(hours_available, intensity):
    # Step 1: Score every subject
    scored = []
    for subject in SUBJECTS:
        score = calculate_priority(subject)
        scored.append((subject, score))

    # Step 2: Sort by priority score, highest first
    scored.sort(key=lambda x: x[1], reverse=True)

    # Step 3: Adjust total hours based on mood
    total_hours = adjust_hours_by_mood(hours_available, intensity)

    # Step 4: Assign time slots
    schedule = []
    hours_left = total_hours

    for subject, score in scored:
        if hours_left <= 0:
            break

        # Allocate proportional time, capped at hours_needed
        allocated = min(subject["hours_needed"], hours_left, round(total_hours * (score / 10)))
        allocated = max(allocated, 1)  # at least 1 hour per subject

        schedule.append({
            "subject": subject["name"],
            "priority_score": score,
            "hours_allocated": allocated,
            "days_until_exam": subject["days_until_exam"]
        })

        hours_left -= allocated

    return schedule, total_hours