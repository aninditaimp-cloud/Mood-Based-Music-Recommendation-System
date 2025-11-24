import random
from datetime import datetime

def get_mood_choice():
    """Get and validate user's mood selection"""
    mood_map = {
        '1': 'happy',
        '2': 'sad',
        '3': 'energetic',
        '4': 'calm',
        '5': 'romantic',
        '6': 'angry'
    }
    
    while True:
        choice = input("\nEnter your choice (0-6): ").strip()
        
        if choice == '0':
            return None
        
        if choice in mood_map:
            return mood_map[choice]
        
        print("❌ Invalid choice! Please enter a number between 0 and 6.")
