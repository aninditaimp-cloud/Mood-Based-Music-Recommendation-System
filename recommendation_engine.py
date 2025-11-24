
from song_database import song_database
from filter_engine import filter_by_genre, filter_by_year
def get_song_count():
    """Get number of songs to display"""
    while True:
        try:
            count = int(input("\n🔢 How many songs do you want? (1-50): ").strip())
            if 1 <= count <= 50:
                return count
            print("❌ Please enter a number between 1 and 50.")
        except ValueError:
            print("❌ Please enter a valid number.")

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


def get_recommendations(mood):
    """Main function to get song recommendations"""
    songs = song_database[mood].copy()
    
    # Apply filters
    songs = filter_by_genre(songs)
    
    if not songs:
        print("\n❌ No songs found for this genre. Try another option!")
        return
    
    songs = filter_by_year(songs)
    
    if not songs:
        print("\n❌ No songs found for this year range. Try another option!")
        return
    
    # Sort by trending and popularity
    songs.sort(key=lambda x: (x['trending'], x['popularity']), reverse=True)
    
    # Get number of songs
    count = get_song_count()
    
    # Limit to requested count
    songs = songs[:count]

    display_songs(songs, mood)
    
    