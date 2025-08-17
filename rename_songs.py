#!/usr/bin/env python3
"""
Script to rename music files to a consistent format for the Music Playlist Manager
Format: "Artist - Song Title"
"""

import os
from pathlib import Path

def rename_music_files():
    """Rename all music files to follow the format 'Artist - Song Title'"""
    
    # Define the music directory
    music_dir = Path("music")
    
    if not music_dir.exists():
        print(f"Error: Music directory '{music_dir}' does not exist.")
        return
    
    # Define the mapping of current filenames to new artist-title format
    # Based on the original filenames and common knowledge of these songs
    filename_mapping = {
        # Deep Purple songs (from original filenames like "01 - Highway Star")
        "Highway Star - Copy.mp3": "Deep Purple - Highway Star.mp3",
        "Highway Star.mp3": "Deep Purple - Highway Star.mp3",
        "Fireball - Copy.mp3": "Deep Purple - Fireball.mp3", 
        "Fireball.mp3": "Deep Purple - Fireball.mp3",
        "Speed_King.mp3": "Deep Purple - Speed King.mp3",
        "Speed_King - Copy.mp3": "Deep Purple - Speed King.mp3",
        "When A Blind Man Cries - Copy.mp3": "Deep Purple - When A Blind Man Cries.mp3",
        "When A Blind Man Cries.mp3": "Deep Purple - When A Blind Man Cries.mp3",
        
        # Ozzy Osbourne songs (from original filenames like "01. I Don't Know")
        "I Don't Know.mp3": "Ozzy Osbourne - I Don't Know.mp3",
        "Crazy Train.mp3": "Ozzy Osbourne - Crazy Train.mp3",
        "Goodbye to Romance.mp3": "Ozzy Osbourne - Goodbye to Romance.mp3",
        "Dee.mp3": "Ozzy Osbourne - Dee.mp3",
        "Suicide Solution.mp3": "Ozzy Osbourne - Suicide Solution.mp3",
        
        # Pantera songs (from original filenames like "05 Pantera, Cemetary Gates")
        "Cemetary Gates.flac": "Pantera - Cemetary Gates.flac",
        "Domination.flac": "Pantera - Domination.flac",
        "Shattered.flac": "Pantera - Shattered.flac",
        "Clash With Reality.flac": "Pantera - Clash With Reality.flac",
        
        # Ramones songs (from original filenames like "02-ramones-zero_zero_ufo-end")
        "zero zero ufo-end.mp3": "Ramones - Zero Zero UFO.mp3",
        "dont bust my chops-end.mp3": "Ramones - Don't Bust My Chops.mp3",
        "punishment fits the crime end.mp3": "Ramones - Punishment Fits The Crime.mp3"
    }
    
    print("Renaming music files to follow 'Artist - Song Title' format...")
    print("=" * 60)
    
    renamed_count = 0
    skipped_count = 0
    
    for file_path in music_dir.iterdir():
        if file_path.is_file():
            current_name = file_path.name
            
            # Check if we have a mapping for this file
            if current_name in filename_mapping:
                new_name = filename_mapping[current_name]
                new_path = file_path.parent / new_name
                
                # Check if target filename already exists
                if new_path.exists():
                    print(f"SKIP: {current_name} -> {new_name} (target already exists)")
                    skipped_count += 1
                    continue
                
                try:
                    # Rename the file
                    file_path.rename(new_path)
                    print(f"RENAMED: {current_name} -> {new_name}")
                    renamed_count += 1
                except Exception as e:
                    print(f"ERROR renaming {current_name}: {e}")
                    skipped_count += 1
            else:
                print(f"SKIP: {current_name} (no mapping defined)")
                skipped_count += 1
    
    print("=" * 60)
    print(f"Renaming complete!")
    print(f"Files renamed: {renamed_count}")
    print(f"Files skipped: {skipped_count}")
    
    # Display the new directory structure
    print("\nNew directory structure:")
    print("-" * 40)
    for file_path in sorted(music_dir.iterdir()):
        if file_path.is_file():
            print(f"  {file_path.name}")

def verify_renaming():
    """Verify that the renaming worked correctly"""
    print("\n" + "=" * 60)
    print("VERIFICATION - Testing with Music Playlist Manager")
    print("=" * 60)
    
    try:
        from music_playlist_manager import MusicPlaylistManager
        
        # Initialize manager
        music_dir = r"D:\projects\Music_Stream\music"
        manager = MusicPlaylistManager(music_dir)
        
        # Load the music library
        manager.load_music_library()
        
        # Display results
        print(f"\nTotal songs loaded: {len(manager.get_song_library())}")
        
        # Show artists found
        artists = manager.get_artists_list()
        print(f"\nArtists found: {artists}")
        
        # Show sample songs for each artist
        for artist in artists:
            songs = manager.filter_songs_by_artist(artist)
            print(f"\n{artist}:")
            for song in songs:
                print(f"  • {song['title']} ({song['file_type']})")
                
    except ImportError:
        print("Could not import MusicPlaylistManager - run the main program separately")
    except Exception as e:
        print(f"Error during verification: {e}")

if __name__ == "__main__":
    # First rename the files
    rename_music_files()
    
    # Then verify the renaming worked
    verify_renaming()
