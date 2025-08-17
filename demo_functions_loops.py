#!/usr/bin/env python3
"""
Demo script showcasing Functions & Loops in the Music Player
This demonstrates the core programming concepts used in the system
"""

def demonstrate_functions():
    """Demonstrate various function types and patterns."""
    print("=" * 60)
    print("FUNCTIONS DEMONSTRATION")
    print("=" * 60)
    
    # Simple function
    def greet_user(name):
        return f"Hello, {name}! Welcome to the Music Player!"
    
    # Function with default parameters
    def create_playlist(name, description="", is_public=True):
        return {
            'name': name,
            'description': description,
            'is_public': is_public,
            'songs': []
        }
    
    # Function that returns multiple values
    def analyze_song(song_info):
        title = song_info.get('title', 'Unknown')
        artist = song_info.get('artist', 'Unknown')
        duration = song_info.get('duration', 0)
        
        # Calculate rating based on duration
        if duration > 300:  # 5 minutes
            rating = "Long"
        elif duration > 180:  # 3 minutes
            rating = "Medium"
        else:
            rating = "Short"
            
        return title, artist, rating
    
    # Demonstrate function calls
    print("1. Simple function:")
    print(f"   {greet_user('Music Lover')}")
    
    print("\n2. Function with default parameters:")
    playlist1 = create_playlist("My Favorites")
    playlist2 = create_playlist("Rock Classics", "Best rock songs ever", False)
    print(f"   Playlist 1: {playlist1}")
    print(f"   Playlist 2: {playlist2}")
    
    print("\n3. Function returning multiple values:")
    song_data = {'title': 'Highway Star', 'artist': 'Deep Purple', 'duration': 420}
    title, artist, rating = analyze_song(song_data)
    print(f"   Song: {title} by {artist} - Rating: {rating}")

def demonstrate_loops():
    """Demonstrate various loop types and patterns."""
    print("\n" + "=" * 60)
    print("LOOPS DEMONSTRATION")
    print("=" * 60)
    
    # Sample music data
    artists = ['Deep Purple', 'Ozzy Osbourne', 'Pantera', 'Ramones']
    songs = [
        {'title': 'Highway Star', 'artist': 'Deep Purple', 'genre': 'Rock'},
        {'title': 'Crazy Train', 'artist': 'Ozzy Osbourne', 'genre': 'Heavy Metal'},
        {'title': 'Cemetary Gates', 'artist': 'Pantera', 'genre': 'Groove Metal'},
        {'title': 'Zero Zero UFO', 'artist': 'Ramones', 'genre': 'Punk Rock'}
    ]
    
    print("1. For loop with range:")
    for i in range(5):
        print(f"   Song number {i + 1}")
    
    print("\n2. For loop with list:")
    for artist in artists:
        print(f"   Artist: {artist}")
    
    print("\n3. For loop with enumerate:")
    for index, artist in enumerate(artists, 1):
        print(f"   {index}. {artist}")
    
    print("\n4. For loop with dictionary items:")
    for song in songs:
        print(f"   {song['title']} by {song['artist']} ({song['genre']})")
    
    print("\n5. List comprehension:")
    rock_songs = [song['title'] for song in songs if song['genre'] == 'Rock']
    print(f"   Rock songs: {rock_songs}")
    
    print("\n6. While loop:")
    count = 0
    while count < 3:
        print(f"   Processing song {count + 1}...")
        count += 1

def demonstrate_nested_structures():
    """Demonstrate nested loops and complex data structures."""
    print("\n" + "=" * 60)
    print("NESTED STRUCTURES DEMONSTRATION")
    print("=" * 60)
    
    # Simulate music library structure
    music_library = {
        'Deep Purple': {
            'genre': 'Rock',
            'albums': ['Machine Head', 'Fireball', 'In Rock'],
            'songs': ['Highway Star', 'Fireball', 'Speed King', 'When A Blind Man Cries']
        },
        'Ozzy Osbourne': {
            'genre': 'Heavy Metal',
            'albums': ['Blizzard of Ozz', 'Diary of a Madman'],
            'songs': ['I Don\'t Know', 'Crazy Train', 'Goodbye to Romance', 'Dee', 'Suicide Solution']
        },
        'Pantera': {
            'genre': 'Groove Metal',
            'albums': ['Cowboys from Hell', 'Vulgar Display of Power'],
            'songs': ['Cemetary Gates', 'Domination', 'Shattered', 'Clash With Reality']
        }
    }
    
    print("1. Nested loops to display library structure:")
    for artist, info in music_library.items():
        print(f"\n   Artist: {artist}")
        print(f"   Genre: {info['genre']}")
        print(f"   Albums: {', '.join(info['albums'])}")
        print(f"   Songs:")
        for i, song in enumerate(info['songs'], 1):
            print(f"     {i}. {song}")
    
    print("\n2. Complex filtering with nested loops:")
    # Find all songs longer than 4 characters
    long_songs = []
    for artist, info in music_library.items():
        for song in info['songs']:
            if len(song) > 4:
                long_songs.append(f"{song} by {artist}")
    
    print(f"   Songs with names longer than 4 characters: {len(long_songs)}")
    for song in long_songs[:3]:  # Show first 3
        print(f"     • {song}")

def demonstrate_error_handling():
    """Demonstrate error handling with functions and loops."""
    print("\n" + "=" * 60)
    print("ERROR HANDLING DEMONSTRATION")
    print("=" * 60)
    
    def safe_divide(a, b):
        """Safely divide two numbers with error handling."""
        try:
            result = a / b
            return result
        except ZeroDivisionError:
            print(f"   Error: Cannot divide {a} by zero!")
            return None
        except TypeError:
            print(f"   Error: Invalid types for division!")
            return None
    
    def process_song_data(song_list):
        """Process song data with error handling."""
        processed_songs = []
        
        for i, song in enumerate(song_list):
            try:
                # Simulate some processing that might fail
                if not isinstance(song, dict):
                    raise ValueError(f"Song at index {i} is not a dictionary")
                
                if 'title' not in song:
                    raise KeyError(f"Song at index {i} missing 'title' key")
                
                processed_songs.append(song['title'])
                print(f"   Successfully processed: {song['title']}")
                
            except (ValueError, KeyError) as e:
                print(f"   Error processing song at index {i}: {e}")
            except Exception as e:
                print(f"   Unexpected error processing song at index {i}: {e}")
        
        return processed_songs
    
    print("1. Error handling in functions:")
    print(f"   Safe division: 10 / 2 = {safe_divide(10, 2)}")
    print(f"   Safe division: 10 / 0 = {safe_divide(10, 0)}")
    
    print("\n2. Error handling in loops:")
    test_songs = [
        {'title': 'Highway Star'},
        {'title': 'Crazy Train'},
        'Invalid song data',  # This will cause an error
        {'title': 'Cemetary Gates'},
        {}  # This will cause an error
    ]
    
    processed = process_song_data(test_songs)
    print(f"   Successfully processed {len(processed)} songs")

def demonstrate_recursion():
    """Demonstrate recursive functions."""
    print("\n" + "=" * 60)
    print("RECURSION DEMONSTRATION")
    print("=" * 60)
    
    def factorial(n):
        """Calculate factorial using recursion."""
        if n <= 1:
            return 1
        return n * factorial(n - 1)
    
    def fibonacci(n):
        """Calculate Fibonacci number using recursion."""
        if n <= 1:
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)
    
    def count_songs_in_playlist(playlist, depth=0):
        """Recursively count songs in nested playlist structure."""
        indent = "  " * depth
        if isinstance(playlist, list):
            total = 0
            for item in playlist:
                total += count_songs_in_playlist(item, depth + 1)
            return total
        elif isinstance(playlist, dict):
            if 'songs' in playlist:
                return len(playlist['songs'])
            else:
                return 0
        else:
            return 0
    
    print("1. Factorial calculation:")
    for i in range(6):
        print(f"   {i}! = {factorial(i)}")
    
    print("\n2. Fibonacci sequence:")
    for i in range(8):
        print(f"   F({i}) = {fibonacci(i)}")
    
    print("\n3. Recursive playlist processing:")
    nested_playlist = {
        'name': 'My Music',
        'playlists': [
            {
                'name': 'Rock',
                'songs': ['Song 1', 'Song 2', 'Song 3']
            },
            {
                'name': 'Metal',
                'songs': ['Song 4', 'Song 5']
            }
        ]
    }
    
    total_songs = count_songs_in_playlist(nested_playlist)
    print(f"   Total songs in nested playlist: {total_songs}")

def main():
    """Main function to run all demonstrations."""
    print("🎵 MUSIC PLAYER - FUNCTIONS & LOOPS DEMONSTRATION 🎵")
    
    # Run all demonstrations
    demonstrate_functions()
    demonstrate_loops()
    demonstrate_nested_structures()
    demonstrate_error_handling()
    demonstrate_recursion()
    
    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE!")
    print("=" * 60)
    print("This showcases the core programming concepts used in the Music Player:")
    print("• Functions with various parameter types and return values")
    print("• Different types of loops (for, while, list comprehensions)")
    print("• Nested data structures and loops")
    print("• Error handling in functions and loops")
    print("• Recursive functions")
    print("\nRun 'python music_player_menu.py' to use the full Music Player!")

if __name__ == "__main__":
    main()
