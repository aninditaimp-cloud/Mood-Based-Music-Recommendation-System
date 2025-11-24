import random
from datetime import datetime
from recommendation_engine import get_recommendations

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

def print_header():
    """Display the program header"""
    print("\n" + "="*60)
    print("🎵  MOOD-BASED MUSIC RECOMMENDATION SYSTEM  🎵".center(60))
    print("="*60)
    print("Discover songs that match your current mood!".center(60))
    print("="*60 + "\n")


def print_menu():
    """Display the mood selection menu"""
    print("\n📋 SELECT YOUR MOOD:")
    print("-" * 40)
    print("1. 😊 Happy")
    print("2. 😢 Sad")
    print("3. ⚡ Energetic")
    print("4. 😌 Calm")
    print("5. 💕 Romantic")
    print("6. 😠 Angry")
    print("0. ❌ Exit")
    print("-" * 40)

def display_songs(songs, mood):
    """Display the recommended songs"""
    if not songs:
        print("\n" + "="*60)
        print("❌ No songs found matching your criteria!")
        print("Try adjusting your filters.")
        print("="*60)
        return
    
    print("\n" + "="*60)
    print(f"🎵  YOUR PERSONALIZED {mood.upper()} PLAYLIST  🎵".center(60))
    print("="*60)
    print(f"Found {len(songs)} song(s)\n")
    
    for i, song in enumerate(songs, 1):
        print(f"\n{i}. 🎵 {song['title']}")
        print(f"   👤 Artist: {song['artist']}")
        print(f"   🎸 Genre: {song['genre']}")
        print(f"   📅 Year: {song['year']}")
        print(f"   ⭐ Popularity: {song['popularity']}/100")
        if song['trending']:
            print(f"   🔥 TRENDING!")
        print("-" * 50)
    
    print("\n" + "="*60)    


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
