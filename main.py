from sentiment import detect_mood
from planner import generate_schedule

def display_schedule(schedule, total_hours, mood, intensity):
    print("\n" + "="*50)
    print("       YOUR PERSONALIZED STUDY PLAN")
    print("="*50)
    print(f"Mood detected : {mood.capitalize()}")
    print(f"Study intensity : {intensity.capitalize()}")
    print(f"Total study hours allocated : {total_hours} hrs")
    print("-"*50)

    for i, item in enumerate(schedule, start=1):
        print(f"{i}. {item['subject']}")
        print(f"   Priority Score  : {item['priority_score']}")
        print(f"   Hours Allocated : {item['hours_allocated']} hr(s)")
        print(f"   Days Until Exam : {item['days_until_exam']}")
        print()

    print("="*50)
    print("Good luck with your studies!")
    print("="*50)

def main():
    print("="*50)
    print("   STUDY PLANNER WITH SMART SUGGESTIONS")
    print("="*50)

    while True:
        try:
            hours = int(input("\nHow many hours can you study today? "))
            if hours <= 0:
                print("Please enter a number greater than 0.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("\nHow are you feeling right now?")
    print("(e.g. I am feeling tired and stressed / I am feeling good and motivated)")
    mood_input = input("> ")

    mood, intensity = detect_mood(mood_input)

    schedule, total_hours = generate_schedule(hours, intensity)
    display_schedule(schedule, total_hours, mood, intensity)

if __name__ == "__main__":
    main()
