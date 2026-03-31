from data import SUBJECTS

def calc_priority(subject):
    difficulty = subject["difficulty"]
    urgency = 10 - subject["leftTime"]  # fewer days mean higher urgancy
    priority_score = (difficulty * 0.6) + (urgency * 0.4)
    return round(priority_score, 2)

def adjust_hours_by_mood(hours_available, intensity):
    if intensity == "high":
        return hours_available          # full study sesion
    elif intensity == "moderate":
        return int(hours_available * 0.8)   # 80% of available hours
    else:
        return int(hours_available * 0.6)   # light session, 60%

def generate_sch(hours_available, intensity):
    scored = []
    for subject in SUBJECTS:
        score = calc_priority(subject)
        scored.append((subject, score))

    scored.sort(key=lambda x: x[1], reverse=True)

    t_hours = adjust_hours_by_mood(hours_available, intensity)

    sch = []
    hours_left = t_hours

    for subject, score in scored:
        if hours_left <= 0:
            break

        allocated = min(subject["needh"], hours_left, round(t_hours * (score / 10)))
        allocated = max(allocated, 1)  

        sch.append({
            "subject": subject["name"],
            "priority_score": score,
            "alloh": allocated,
            "leftTime": subject["leftTime"]
        })

        hours_left -= allocated

    return sch, t_hours
