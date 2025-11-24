import random
from datetime import datetime

song_database = {
    'happy': [
        {'title': 'Blinding Lights', 'artist': 'The Weeknd', 'genre': 'Pop', 'year': 2020, 'popularity': 98, 'trending': True},
        {'title': 'Good Feeling', 'artist': 'Flo Rida', 'genre': 'Pop', 'year': 2011, 'popularity': 92, 'trending': False},
        {'title': 'Happy', 'artist': 'Pharrell Williams', 'genre': 'Pop', 'year': 2013, 'popularity': 95, 'trending': False},
        {'title': "Can't Stop the Feeling", 'artist': 'Justin Timberlake', 'genre': 'Pop', 'year': 2016, 'popularity': 94, 'trending': False},
        {'title': 'Uptown Funk', 'artist': 'Mark Ronson ft. Bruno Mars', 'genre': 'Pop', 'year': 2014, 'popularity': 96, 'trending': False},
        {'title': 'September', 'artist': 'Earth, Wind & Fire', 'genre': 'Pop', 'year': 1978, 'popularity': 93, 'trending': False},
        {'title': 'Walking on Sunshine', 'artist': 'Katrina and the Waves', 'genre': 'Rock', 'year': 1985, 'popularity': 88, 'trending': False},
        {'title': "Don't Stop Me Now", 'artist': 'Queen', 'genre': 'Rock', 'year': 1978, 'popularity': 97, 'trending': False},
        {'title': 'I Gotta Feeling', 'artist': 'Black Eyed Peas', 'genre': 'Pop', 'year': 2009, 'popularity': 91, 'trending': False},
        {'title': 'Sugar', 'artist': 'Maroon 5', 'genre': 'Pop', 'year': 2014, 'popularity': 90, 'trending': False},
        {'title': 'Flowers', 'artist': 'Miley Cyrus', 'genre': 'Pop', 'year': 2023, 'popularity': 96, 'trending': True},
        {'title': 'Levitating', 'artist': 'Dua Lipa', 'genre': 'Pop', 'year': 2020, 'popularity': 94, 'trending': True},
        {'title': 'Anti-Hero', 'artist': 'Taylor Swift', 'genre': 'Pop', 'year': 2023, 'popularity': 95, 'trending': True}
    ],
    'sad': [
        {'title': 'Someone Like You', 'artist': 'Adele', 'genre': 'Pop', 'year': 2011, 'popularity': 96, 'trending': False},
        {'title': 'Let Her Go', 'artist': 'Passenger', 'genre': 'Indie', 'year': 2012, 'popularity': 92, 'trending': False},
        {'title': 'The Night We Met', 'artist': 'Lord Huron', 'genre': 'Indie', 'year': 2015, 'popularity': 91, 'trending': False},
        {'title': 'Skinny Love', 'artist': 'Bon Iver', 'genre': 'Indie', 'year': 2007, 'popularity': 89, 'trending': False},
        {'title': 'Fix You', 'artist': 'Coldplay', 'genre': 'Rock', 'year': 2005, 'popularity': 94, 'trending': False},
        {'title': 'Hurt', 'artist': 'Johnny Cash', 'genre': 'Rock', 'year': 2002, 'popularity': 93, 'trending': False},
        {'title': 'Mad World', 'artist': 'Gary Jules', 'genre': 'Indie', 'year': 2001, 'popularity': 88, 'trending': False},
        {'title': 'Creep', 'artist': 'Radiohead', 'genre': 'Rock', 'year': 1992, 'popularity': 92, 'trending': False},
        {'title': 'All Too Well', 'artist': 'Taylor Swift', 'genre': 'Pop', 'year': 2021, 'popularity': 95, 'trending': True},
        {'title': 'drivers license', 'artist': 'Olivia Rodrigo', 'genre': 'Pop', 'year': 2021, 'popularity': 94, 'trending': True},
        {'title': 'Vampire', 'artist': 'Olivia Rodrigo', 'genre': 'Pop', 'year': 2023, 'popularity': 93, 'trending': True},
        {'title': 'Glimpse of Us', 'artist': 'Joji', 'genre': 'Pop', 'year': 2023, 'popularity': 90, 'trending': True}
    ],
    'energetic': [
        {'title': 'Till I Collapse', 'artist': 'Eminem', 'genre': 'Hip-Hop', 'year': 2002, 'popularity': 95, 'trending': False},
        {'title': 'Eye of the Tiger', 'artist': 'Survivor', 'genre': 'Rock', 'year': 1982, 'popularity': 94, 'trending': False},
        {'title': 'Thunder', 'artist': 'Imagine Dragons', 'genre': 'Rock', 'year': 2017, 'popularity': 93, 'trending': False},
        {'title': 'Titanium', 'artist': 'David Guetta ft. Sia', 'genre': 'Electronic', 'year': 2011, 'popularity': 96, 'trending': False},
        {'title': 'Pump It', 'artist': 'Black Eyed Peas', 'genre': 'Pop', 'year': 2005, 'popularity': 90, 'trending': False},
        {'title': 'Lose Yourself', 'artist': 'Eminem', 'genre': 'Hip-Hop', 'year': 2002, 'popularity': 98, 'trending': False},
        {'title': "Can't Hold Us", 'artist': 'Macklemore', 'genre': 'Hip-Hop', 'year': 2011, 'popularity': 92, 'trending': False},
        {'title': 'Stronger', 'artist': 'Kanye West', 'genre': 'Hip-Hop', 'year': 2007, 'popularity': 93, 'trending': False},
        {'title': 'SICKO MODE', 'artist': 'Travis Scott', 'genre': 'Hip-Hop', 'year': 2018, 'popularity': 94, 'trending': True},
        {'title': 'HUMBLE.', 'artist': 'Kendrick Lamar', 'genre': 'Hip-Hop', 'year': 2017, 'popularity': 95, 'trending': True},
        {'title': 'Paint The Town Red', 'artist': 'Doja Cat', 'genre': 'Hip-Hop', 'year': 2023, 'popularity': 96, 'trending': True},
        {'title': 'Last Night', 'artist': 'Morgan Wallen', 'genre': 'Pop', 'year': 2023, 'popularity': 94, 'trending': True},
        {'title': 'Cruel Summer', 'artist': 'Taylor Swift', 'genre': 'Pop', 'year': 2024, 'popularity': 97, 'trending': True}
    ],
    'calm': [
        {'title': 'Weightless', 'artist': 'Marconi Union', 'genre': 'Electronic', 'year': 2011, 'popularity': 87, 'trending': False},
        {'title': 'Clair de Lune', 'artist': 'Claude Debussy', 'genre': 'Classical', 'year': 1905, 'popularity': 91, 'trending': False},
        {'title': 'Sunset Lover', 'artist': 'Petit Biscuit', 'genre': 'Electronic', 'year': 2015, 'popularity': 89, 'trending': False},
        {'title': 'River Flows in You', 'artist': 'Yiruma', 'genre': 'Classical', 'year': 2001, 'popularity': 90, 'trending': False},
        {'title': 'Holocene', 'artist': 'Bon Iver', 'genre': 'Indie', 'year': 2011, 'popularity': 88, 'trending': False},
        {'title': 'Banana Pancakes', 'artist': 'Jack Johnson', 'genre': 'Indie', 'year': 2005, 'popularity': 86, 'trending': False},
        {'title': 'Better Together', 'artist': 'Jack Johnson', 'genre': 'Indie', 'year': 2005, 'popularity': 87, 'trending': False},
        {'title': 'Breathe Me', 'artist': 'Sia', 'genre': 'Indie', 'year': 2004, 'popularity': 88, 'trending': False},
        {'title': 'The Less I Know The Better', 'artist': 'Tame Impala', 'genre': 'Indie', 'year': 2015, 'popularity': 92, 'trending': False},
        {'title': 'Lost', 'artist': 'Frank Ocean', 'genre': 'Indie', 'year': 2012, 'popularity': 91, 'trending': False},
        {'title': 'Stick Season', 'artist': 'Noah Kahan', 'genre': 'Indie', 'year': 2023, 'popularity': 93, 'trending': True},
        {'title': 'Everything I Wanted', 'artist': 'Billie Eilish', 'genre': 'Pop', 'year': 2020, 'popularity': 90, 'trending': True}
    ],
    'romantic': [
        {'title': 'Perfect', 'artist': 'Ed Sheeran', 'genre': 'Pop', 'year': 2017, 'popularity': 97, 'trending': False},
        {'title': 'Thinking Out Loud', 'artist': 'Ed Sheeran', 'genre': 'Pop', 'year': 2014, 'popularity': 96, 'trending': False},
        {'title': 'All of Me', 'artist': 'John Legend', 'genre': 'Pop', 'year': 2013, 'popularity': 98, 'trending': False},
        {'title': 'A Thousand Years', 'artist': 'Christina Perri', 'genre': 'Pop', 'year': 2011, 'popularity': 95, 'trending': False},
        {'title': 'Make You Feel My Love', 'artist': 'Adele', 'genre': 'Pop', 'year': 2008, 'popularity': 93, 'trending': False},
        {'title': "Say You Won't Let Go", 'artist': 'James Arthur', 'genre': 'Pop', 'year': 2016, 'popularity': 94, 'trending': False},
        {'title': "I Don't Want to Miss a Thing", 'artist': 'Aerosmith', 'genre': 'Rock', 'year': 1998, 'popularity': 95, 'trending': False},
        {'title': 'Unchained Melody', 'artist': 'The Righteous Brothers', 'genre': 'Pop', 'year': 1965, 'popularity': 92, 'trending': False},
        {'title': 'At Last', 'artist': 'Etta James', 'genre': 'Jazz', 'year': 1960, 'popularity': 91, 'trending': False},
        {'title': 'Lover', 'artist': 'Taylor Swift', 'genre': 'Pop', 'year': 2019, 'popularity': 93, 'trending': True},
        {'title': 'Die For You', 'artist': 'The Weeknd', 'genre': 'Pop', 'year': 2023, 'popularity': 95, 'trending': True},
        {'title': 'Snooze', 'artist': 'SZA', 'genre': 'Pop', 'year': 2023, 'popularity': 94, 'trending': True}
    ],
    'angry': [
        {'title': 'Break Stuff', 'artist': 'Limp Bizkit', 'genre': 'Rock', 'year': 1999, 'popularity': 88, 'trending': False},
        {'title': 'Bodies', 'artist': 'Drowning Pool', 'genre': 'Rock', 'year': 2001, 'popularity': 87, 'trending': False},
        {'title': 'The Way I Am', 'artist': 'Eminem', 'genre': 'Hip-Hop', 'year': 2000, 'popularity': 91, 'trending': False},
        {'title': 'Killing in the Name', 'artist': 'Rage Against the Machine', 'genre': 'Rock', 'year': 1992, 'popularity': 93, 'trending': False},
        {'title': 'Freak on a Leash', 'artist': 'Korn', 'genre': 'Rock', 'year': 1998, 'popularity': 89, 'trending': False},
        {'title': 'Down with the Sickness', 'artist': 'Disturbed', 'genre': 'Rock', 'year': 2000, 'popularity': 90, 'trending': False},
        {'title': 'Chop Suey!', 'artist': 'System of a Down', 'genre': 'Rock', 'year': 2001, 'popularity': 92, 'trending': False},
        {'title': 'In the End', 'artist': 'Linkin Park', 'genre': 'Rock', 'year': 2000, 'popularity': 96, 'trending': False},
        {'title': 'Enter Sandman', 'artist': 'Metallica', 'genre': 'Rock', 'year': 1991, 'popularity': 94, 'trending': False},
        {'title': 'Welcome to the Jungle', 'artist': "Guns N' Roses", 'genre': 'Rock', 'year': 1987, 'popularity': 95, 'trending': False},
        {'title': 'The Grudge', 'artist': 'Tool', 'genre': 'Rock', 'year': 2001, 'popularity': 88, 'trending': False}
    ]
}