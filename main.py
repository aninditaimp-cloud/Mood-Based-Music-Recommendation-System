import random
from datetime import datetime
from mood_selector import get_mood_choice
from song_database import song_database
from filter_engine import filter_by_genre, filter_by_year
from recommendation_engine import get_recommendations
from display_manager import print_header, print_menu, display_songs

def main():
    """Main program loop"""
    print_header()
    
    while True:
        print_menu()
        mood = get_mood_choice()
        
        if mood is None:
            print("\n" + "="*60)
            print("Thank you for using Mood Music Recommender! 👋".center(60))
            print("="*60 + "\n")
            break
        
        get_recommendations(mood)
        
        
        input("\n\nPress Enter to continue...")


# Run the program
if __name__ == "__main__":
    main()
