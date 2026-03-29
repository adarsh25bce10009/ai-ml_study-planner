# Study Planner with Smart Suggestions

A Python-based command-line study planner that generates a personalized study schedule based on subject priority and the student's current mood.

## Overview

Managing multiple subjects with different difficulty levels and exam dates can be overwhelming. This tool helps students plan their study sessions smartly by ranking subjects using a priority scoring system and adjusting the schedule based on how the student is feeling, and tells the students which subjects to focus on first to maximise result.

## Features

- Prioritizes subjects based on difficulty and days until exam
- Detects student mood from natural language input
- Adjusts study intensity based on mood (high / moderate / light)
- Generates a clean, ranked study schedule

## How It Works

1. The planner scores each subject using:
   - Priority Score = (difficulty × 0.4) + (urgency × 0.6)
   - Urgency = 10 - days_until_exam (fewer days = higher urgency)
2. The sentiment module scans the student's input for positive/negative keywords
3. Available study hours are adjusted based on detected mood
4. Subjects are ranked and time is allocated proportionally

## Project Structure

study-planner/
├── main.py          # Entry point, handles user input and output
├── planner.py       # Core scheduling and priority logic
├── sentiment.py     # Keyword-based mood detection
├── data.py          # Subject dataset with difficulty and exam data
├── requirements.txt # No external dependencies
└── .gitignore       # Excludes cache and unnecessary files


## Setup and Usage

**Requirements:** Python 3.x - no external libraries needed

**Run the planner:**
```bash
python main.py
```

**Example interaction:**
```
==================================================
   STUDY PLANNER WITH SMART SUGGESTIONS
==================================================
How many hours can you study today? 5
How are you feeling right now?
> I am feeling tired and stressed

==================================================
       YOUR PERSONALIZED STUDY PLAN
==================================================
Mood detected : Negative
Study intensity : Light
Total study hours allocated : 3 hrs
--------------------------------------------------
1. Transform Techniques
   Priority Score  : 8.2
   Hours Allocated : 2 hr(s)
   Days Until Exam : 3
...
==================================================
Good luck with your studies!
==================================================
```

## Concepts Applied

- **Priority Scoring** - weighted formula combining difficulty and urgency
- **Sentiment Analysis** - keyword-based NLP mood detection
- **Data Representation** - structured subject data with multiple attributes
- **Decision Logic** - mood-based intensity adjustment

## Author

Adarsh Kumar Yadav - B.Tech CSE, VIT Bhopal University
