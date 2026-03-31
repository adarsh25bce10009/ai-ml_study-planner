from sentiment import detect_mood
from planner import generate_sch

def display_sch(sch, t_hours, mood, intensity):  #to displ
    print("\n" + "="*50)
    print("       YOUR PERSONALIZED STUDY PLAN")
    print("="*50)
    print(f"Mood detected : {mood.capitalize()}")
    print(f"Study intensity : {intensity.capitalize()}")
    print(f"Total study hours allocated : {t_hours} hrs")
    print("-"*50)

    for i, item in enumerate(sch, start=1):
        print(f"{i}. {item['subject']}")
        print(f"   Priority Score  : {item['priority_score']}")
        print(f"   Hours Allocated : {item['alloh']} hr(s)")
        print(f"   Days Until Exam : {item['leftTime']}")
        print()

    print("="*50)
    print("Good luck with your studies!")
    print("="*50)

def main():
    print("="*50)
    print("   STUDY PLANNER WITH SMART SUGGESTIONS")
    print("="*50)

    while True:  #check
        try:
            hours = int(input("\nHow many hours can you study today? "))
            if hours <= 0:
                print("Please enter a number greater than 0.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    print("\nHow are you feeling right now?")   #mood
    print("(e.g. I am feeling tired and stressed / I am feeling good and motivated)")
    moodInput = input("> ")

    mood, intensity = detect_mood(moodInput)

    sch, t_hours = generate_sch(hours, intensity)
    display_sch(sch, t_hours, mood, intensity)

if __name__ == "__main__":
    main()
