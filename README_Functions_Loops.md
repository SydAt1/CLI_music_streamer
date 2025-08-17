# Music Player - Functions & Loops Implementation

## 🎵 Overview

This document explains the **Functions & Loops** implementation in the Music Player system, which demonstrates core programming concepts through a comprehensive music management application.

## 🏗️ Architecture

The Music Player is built using two main classes:

### 1. `MusicPlayer` Class
- **Core functionality** for music library management
- **Playlist operations** (create, add, remove, delete)
- **Playback control** (play, pause, next, previous, stop)
- **Library statistics** and reporting

### 2. `MusicPlayerMenu` Class
- **User interface** with interactive menus
- **Input handling** and validation
- **Menu navigation** and flow control

## 🔧 Functions Implementation

### Core Music Functions

#### Library Management
```python
def load_music_library(self) -> None:
    """Load all music files from the music directory into the library."""
    # Uses for loop to iterate through directory
    for file_path in self.music_directory.iterdir():
        if file_path.is_file() and file_path.suffix.lower() in audio_extensions:
            song_info = self._extract_song_info(file_path)
            if song_info:
                self.song_library.append(song_info)
```

#### Song Information Extraction
```python
def _extract_song_info(self, file_path: Path) -> Dict:
    """Extract song information from filename."""
    filename = file_path.stem
    file_type = file_path.suffix.lower()
    
    # Conditional logic to parse different filename formats
    if ' - ' in filename:
        parts = filename.split(' - ', 1)
        if len(parts) == 2:
            artist = parts[0].strip()
            title = parts[1].strip()
        else:
            artist = "Unknown Artist"
            title = filename
    else:
        artist = "Unknown Artist"
        title = filename
        
    return {
        'filename': filename,
        'title': title,
        'artist': artist,
        'file_type': file_type,
        'file_path': str(file_path),
        'file_size': file_path.stat().st_size
    }
```

#### Search and Filtering
```python
def search_songs(self, query: str) -> List[Dict]:
    """Search for songs by title or artist."""
    query = query.lower()
    results = []
    
    # For loop with conditional filtering
    for song in self.song_library:
        if (query in song['title'].lower() or 
            query in song['artist'].lower()):
            results.append(song)
            
    return results
```

### Playlist Functions

#### Playlist Creation and Management
```python
def create_playlist(self, playlist_name: str) -> bool:
    """Create a new playlist."""
    if playlist_name in self.playlists:
        print(f"Playlist '{playlist_name}' already exists.")
        return False
        
    self.playlists[playlist_name] = []
    print(f"Playlist '{playlist_name}' created successfully!")
    return True

def add_song_to_playlist(self, playlist_name: str, song_index: int) -> bool:
    """Add a song to a playlist by its index in the library."""
    # Input validation
    if playlist_name not in self.playlists:
        print(f"Playlist '{playlist_name}' does not exist.")
        return False
        
    if song_index < 1 or song_index > len(self.song_library):
        print(f"Invalid song index. Please choose 1-{len(self.song_library)}")
        return False
        
    song = self.song_library[song_index - 1]
    self.playlists[playlist_name].append(song)
    print(f"Added '{song['title']}' to playlist '{playlist_name}'")
    return True
```

### Playback Functions

#### Playback Control
```python
def next_song(self) -> bool:
    """Play the next song."""
    if not self.is_playing:
        print("Nothing is currently playing.")
        return False
        
    if self.current_playlist:
        # Playing from playlist
        playlist = self.playlists[self.current_playlist]
        if self.current_song_index < len(playlist) - 1:
            self.current_song_index += 1
            self._show_current_song()
            return True
        else:
            print("End of playlist reached.")
            self.stop_playback()
            return False
    else:
        # Playing single song
        if self.current_song_index < len(self.song_library) - 1:
            self.current_song_index += 1
            self._show_current_song()
            return True
        else:
            print("End of library reached.")
            self.stop_playback()
            return False
```

### Statistics Functions

#### Library Analysis
```python
def show_library_statistics(self) -> None:
    """Display comprehensive library statistics."""
    if not self.song_library:
        print("No songs in library.")
        return
        
    total_songs = len(self.song_library)
    total_size = sum(song['file_size'] for song in self.song_library)
    
    # Count by artist using loops
    artist_counts = {}
    for song in self.song_library:
        artist = song['artist']
        artist_counts[artist] = artist_counts.get(artist, 0) + 1
        
    # Count by file type using loops
    file_type_counts = {}
    for song in self.song_library:
        file_type = song['file_type']
        file_type_counts[file_type] = file_type_counts.get(file_type, 0) + 1
        
    # Display results
    print(f"Total Songs: {total_songs}")
    print(f"Total Size: {total_size / (1024 * 1024):.2f} MB")
    print(f"Unique Artists: {len(artist_counts)}")
    
    print(f"\nSongs by Artist:")
    for artist, count in sorted(artist_counts.items()):
        print(f"  {artist}: {count} songs")
```

## 🔄 Loops Implementation

### For Loops

#### Iterating Through Collections
```python
# Iterate through song library
for i, song in enumerate(self.song_library, 1):
    print(f"{i:2d}. {song['title']:<35} | {song['artist']:<20} | {song['file_type']:<5}")

# Iterate through playlists
for playlist_name, songs in self.playlists.items():
    print(f"{playlist_name}: {len(songs)} songs")

# Iterate through search results
for i, song in enumerate(results, 1):
    print(f"{i}. {song['title']} - {song['artist']} ({song['file_type']})")
```

#### List Comprehensions
```python
# Filter songs by artist
def filter_by_artist(self, artist: str) -> List[Dict]:
    return [song for song in self.song_library 
            if song['artist'].lower() == artist.lower()]

# Filter songs by file type
def filter_by_file_type(self, file_type: str) -> List[Dict]:
    return [song for song in self.song_library 
            if song['file_type'] == file_type.lower()]
```

### While Loops

#### Menu Navigation
```python
def handle_main_menu(self) -> None:
    """Handle the main menu selection."""
    while True:  # Main program loop
        self.display_main_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            self.player.view_song_library()
        elif choice == '2':
            self._handle_search()
        elif choice == '3':
            self._handle_playlist_menu()
        elif choice == '4':
            self._handle_playback_menu()
        elif choice == '5':
            self.player.show_library_statistics()
        elif choice == '6':
            print("Goodbye! 🎵")
            self.running = False
            break
        else:
            print("Invalid choice. Please try again.")
        
        if not self.running:
            break
```

#### Submenu Loops
```python
def _handle_playlist_menu(self) -> None:
    """Handle the playlist management menu."""
    while True:  # Submenu loop
        self.display_playlist_menu()
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == '1':
            self._create_playlist()
        elif choice == '2':
            self.player.list_playlists()
        # ... more options ...
        elif choice == '7':
            break  # Exit submenu
        else:
            print("Invalid choice. Please try again.")
```

## 🎯 Key Programming Concepts Demonstrated

### 1. **Function Types**
- **Simple functions** with basic parameters
- **Functions with default parameters**
- **Functions returning multiple values**
- **Private methods** (prefixed with `_`)
- **Class methods** and instance methods

### 2. **Loop Patterns**
- **For loops** with `range()`, `enumerate()`, and collections
- **While loops** for menu navigation and program flow
- **List comprehensions** for data filtering
- **Nested loops** for complex data structures

### 3. **Data Structures**
- **Lists** for song collections and playlists
- **Dictionaries** for song information and playlist storage
- **Sets** for unique collections (artists, file types)
- **Nested structures** for complex data organization

### 4. **Control Flow**
- **Conditional statements** (`if`, `elif`, `else`)
- **Loop control** (`break`, `continue`)
- **Exception handling** with `try`/`except`
- **Input validation** and error checking

### 5. **User Interaction**
- **Input processing** with `input()` function
- **Menu systems** with hierarchical navigation
- **User feedback** and status messages
- **Error handling** for invalid inputs

## 🚀 Usage Examples

### Running the Full Music Player
```bash
python music_player_menu.py
```

### Running the Functions & Loops Demo
```bash
python demo_functions_loops.py
```

### Programmatic Usage
```python
from music_player_menu import MusicPlayer

# Create player instance
player = MusicPlayer("path/to/music")

# Use functions
player.create_playlist("My Favorites")
player.add_song_to_playlist("My Favorites", 1)
player.play_playlist("My Favorites")

# Access data through loops
for song in player.song_library:
    print(f"Song: {song['title']} by {song['artist']}")
```

## 📊 Performance Considerations

### Loop Efficiency
- **Linear time complexity** for most operations
- **Efficient filtering** using list comprehensions
- **Minimal memory overhead** for large libraries

### Function Optimization
- **Early returns** for invalid inputs
- **Cached results** for frequently accessed data
- **Efficient data structures** for lookups

## 🔍 Testing and Validation

### Input Validation
- **Range checking** for song indices
- **Type validation** for user inputs
- **Existence checking** for playlists and songs

### Error Handling
- **Graceful degradation** for missing files
- **User-friendly error messages**
- **Recovery mechanisms** for common errors

## 🎓 Learning Objectives

This implementation demonstrates:

1. **Function Design**: How to structure functions for reusability and maintainability
2. **Loop Mastery**: Different ways to iterate through data structures
3. **Data Processing**: How to transform and filter data using loops
4. **User Interface**: Building interactive menu systems with loops
5. **Error Handling**: Managing user input and system errors gracefully
6. **Code Organization**: Structuring complex applications with clear separation of concerns

## 🔮 Future Enhancements

- **Audio playback** integration
- **Database storage** for playlists
- **Web interface** using Flask/Django
- **Music metadata** extraction
- **Recommendation algorithms**
- **Social features** (sharing playlists)

---

*This implementation showcases professional-grade Python programming with emphasis on clean code, proper error handling, and user experience design.*
