import random
from datetime import datetime

def filter_by_genre(songs):
    """Filter songs by genre"""
    print("\n🎸 SELECT GENRE:")
    print("1. All Genres")
    print("2. Pop")
    print("3. Rock")
    print("4. Hip-Hop")
    print("5. Electronic")
    print("6. Indie")
    print("7. Jazz")
    print("8. Classical")
    
    genre_map = {
        '1': 'all',
        '2': 'Pop',
        '3': 'Rock',
        '4': 'Hip-Hop',
        '5': 'Electronic',
        '6': 'Indie',
        '7': 'Jazz',
        '8': 'Classical'
    }
    
    while True:
        choice = input("\nEnter genre choice (1-8): ").strip()
        if choice in genre_map:
            selected_genre = genre_map[choice]
            break
        print("❌ Invalid choice! Please try again.")
    
    if selected_genre == 'all':
        return songs
    
    return [song for song in songs if song['genre'] == selected_genre]


def filter_by_year(songs):
    """Filter songs by release year"""
    print("\n📅 SELECT YEAR RANGE:")
    print("1. All Years")
    print("2. 2024 (Latest)")
    print("3. 2023")
    print("4. 2020s")
    print("5. 2010s")
    print("6. Classic Hits (Before 2010)")
    
    while True:
        choice = input("\nEnter year choice (1-6): ").strip()
        if choice in ['1', '2', '3', '4', '5', '6']:
            break
        print("❌ Invalid choice! Please try again.")
    
    if choice == '1':
        return songs
    elif choice == '2':
        return [song for song in songs if song['year'] >= 2024 or song['year'] == 2023]
    elif choice == '3':
        return [song for song in songs if song['year'] == 2023]
    elif choice == '4':
        return [song for song in songs if 2020 <= song['year'] < 2030]
    elif choice == '5':
        return [song for song in songs if 2010 <= song['year'] < 2020]
    elif choice == '6':
        return [song for song in songs if song['year'] < 2010]

