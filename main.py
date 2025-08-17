#!/usr/bin/env python3
"""
Main Music Player - Interactive Interface
Combines all music player features into one simple interface
"""

import os
import sys
import pygame

# Add src directory to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.Lists_and_Tuples import MusicPlaylistManager
from src.linked_list_playlist import PlaylistManager
from src.stacks_queues_music import MusicPlayerStacksQueues, SongQueue, PrioritySongQueue, ListeningHistoryStack

class MainMusicPlayer:
    """Main music player that combines all features."""
    
    def __init__(self):
        self.music_manager = None
        self.playlist_manager = None
        self.stacks_queues_player = None
        self.current_mode = "main"
        
    def initialize_music_library(self):
        """Initialize the music library."""
        print("🎵 WELCOME TO THE MAIN MUSIC PLAYER! 🎵")
        print("=" * 50)
        
        # Get music directory
        music_dir = input("Enter music directory path (or press Enter for default): ").strip()
        if not music_dir:
            music_dir = r"D:\projects\Music_Stream\music"
        
        try:
            self.music_manager = MusicPlaylistManager(music_dir)
            song_library = self.music_manager.get_song_library()
            
            if not song_library:
                print("❌ No songs found in library.")
                return False
            
            print(f"✅ Found {len(song_library)} songs in library!")
            
            # Initialize other components
            self.playlist_manager = PlaylistManager()
            self.stacks_queues_player = MusicPlayerStacksQueues(self.music_manager)
            
            return True
            
        except Exception as e:
            print(f"❌ Error initializing music library: {e}")
            return False
    
    def show_main_menu(self):
        """Display the main menu."""
        print("\n" + "=" * 50)
        print("🎵 MAIN MUSIC PLAYER MENU 🎵")
        print("=" * 50)
        print("1. 📚 Music Library Management")
        print("2. 📋 Playlist Management")
        print("3. 🎯 Stacks & Queues (Play Next/Party Mode)")
        print("4. 📊 View All Status")
        print("5. 🎵 Quick Play")
        print("6. ❌ Exit")
        print("-" * 50)
    
    def show_library_menu(self):
        """Display the music library management menu."""
        while True:
            print("\n" + "=" * 50)
            print("📚 MUSIC LIBRARY MANAGEMENT")
            print("=" * 50)
            print("1. 📋 Display All Songs")
            print("2. 🎨 Display by Artist")
            print("3. 📁 Display by File Type")
            print("4. 🔍 Search Songs")
            print("5. 📊 Library Statistics")
            print("6. ⬅️  Back to Main Menu")
            print("-" * 50)
            
            choice = input("Enter your choice (1-6): ").strip()
            
            if choice == '1':
                self.music_manager.display_song_library()
            
            elif choice == '2':
                self.music_manager.display_artist_report()
            
            elif choice == '3':
                self.music_manager.display_file_type_report()
            
            elif choice == '4':
                query = input("Enter search term: ").strip()
                if query:
                    results = self.music_manager.search_songs(query)
                    if results:
                        print(f"\nFound {len(results)} songs:")
                        for i, song in enumerate(results, 1):
                            print(f"{i}. {song['title']} - {song['artist']}")
                    else:
                        print("No songs found.")
            
            elif choice == '5':
                self.music_manager.display_statistics()
            
            elif choice == '6':
                break
            
            else:
                print("Invalid choice. Please try again.")
    
    def show_playlist_management_menu(self):
        """Display the playlist management menu."""
        while True:
            print("\n" + "=" * 50)
            print("📋 PLAYLIST MANAGEMENT")
            print("=" * 50)
            print("1. 📋 List All Playlists")
            print("2. ➕ Create New Playlist")
            print("3. 📚 Create Playlist from Library")
            print("4. 🔄 Switch Playlist")
            print("5. 🗑️  Delete Playlist")
            print("6. 🎵 Add Song to Current Playlist")
            print("7. 📋 Display Current Playlist")
            print("8. ⏭️  Next Song")
            print("9. ⏮️  Previous Song")
            print("10. 🏠 Go to First Song")
            print("11. 🏁 Go to Last Song")
            print("12. 🔀 Insert Song After")
            print("13. 🗑️  Remove Song")
            print("14. 🔍 Search Song")
            print("15. 🔄 Shuffle Current Playlist")
            print("16. ▶️ Play Current Playlist")
            print("17. ⬅️  Back to Main Menu")
            print("-" * 50)
            
            choice = input("Enter your choice (1-17): ").strip()
            
            if choice == '1':
                self.playlist_manager.list_playlists()
            
            elif choice == '2':
                name = input("Enter playlist name: ").strip()
                description = input("Enter playlist description (optional): ").strip()
                if name:
                    self.playlist_manager.create_playlist(name, description)
            
            elif choice == '3':
                name = input("Enter playlist name: ").strip()
                description = input("Enter playlist description (optional): ").strip()
                max_songs = input("Enter max songs (default 10): ").strip()
                try:
                    max_songs_val = int(max_songs) if max_songs.isdigit() else 10
                    if name:
                        self.playlist_manager.create_playlist_from_library(name, self.music_manager, max_songs_val, description)
                except ValueError:
                    print("Please enter a valid number for max songs.")
            
            elif choice == '4':
                self.playlist_manager.list_playlists()
                name = input("Enter playlist name to switch to: ").strip()
                if name:
                    self.playlist_manager.switch_playlist(name)
            
            elif choice == '5':
                self.playlist_manager.list_playlists()
                name = input("Enter playlist name to delete: ").strip()
                if name:
                    confirm = input(f"Are you sure you want to delete '{name}'? (y/n): ").strip().lower()
                    if confirm == 'y':
                        self.playlist_manager.delete_playlist(name)
            
            elif choice == '6':
                current_playlist = self.playlist_manager.get_current_playlist()
                if not current_playlist:
                    print("No playlist selected. Please create or switch to a playlist first.")
                    continue
                
                song_library = self.music_manager.get_song_library()
                print("\nAvailable songs:")
                for i, song in enumerate(song_library[:10], 1):
                    print(f"{i}. {song['title']} - {song['artist']}")
                
                try:
                    song_idx = int(input("Enter song number: ")) - 1
                    if 0 <= song_idx < len(song_library):
                        self.playlist_manager.add_song_to_current_playlist(song_library[song_idx])
                    else:
                        print("Invalid song number.")
                except ValueError:
                    print("Please enter a valid number.")
            
            elif choice == '7':
                current_playlist = self.playlist_manager.get_current_playlist()
                if current_playlist:
                    current_playlist.display_playlist()
                else:
                    print("No playlist selected. Please create or switch to a playlist first.")
            
            elif choice == '8':
                current_playlist = self.playlist_manager.get_current_playlist()
                if current_playlist:
                    current_playlist.next_song()
                else:
                    print("No playlist selected. Please create or switch to a playlist first.")
            
            elif choice == '9':
                current_playlist = self.playlist_manager.get_current_playlist()
                if current_playlist:
                    current_playlist.previous_song()
                else:
                    print("No playlist selected. Please create or switch to a playlist first.")
            
            elif choice == '10':
                current_playlist = self.playlist_manager.get_current_playlist()
                if current_playlist:
                    current_playlist.go_to_first_song()
                else:
                    print("No playlist selected. Please create or switch to a playlist first.")
            
            elif choice == '11':
                current_playlist = self.playlist_manager.get_current_playlist()
                if current_playlist:
                    current_playlist.go_to_last_song()
                else:
                    print("No playlist selected. Please create or switch to a playlist first.")
            
            elif choice == '12':
                current_playlist = self.playlist_manager.get_current_playlist()
                if current_playlist:
                    target = input("Enter song title to insert after: ").strip()
                    title = input("Enter new song title: ").strip()
                    artist = input("Enter new artist name: ").strip()
                    if target and title and artist:
                        new_song = {
                            'title': title,
                            'artist': artist,
                            'file_type': '.mp3',
                            'file_path': 'manual/entry',
                            'file_size': 1024
                        }
                        current_playlist.insert_song_after(target, new_song)
                else:
                    print("No playlist selected. Please create or switch to a playlist first.")
            
            elif choice == '13':
                current_playlist = self.playlist_manager.get_current_playlist()
                if current_playlist:
                    title = input("Enter song title to remove: ").strip()
                    if title:
                        current_playlist.remove_song(title)
                else:
                    print("No playlist selected. Please create or switch to a playlist first.")
            
            elif choice == '14':
                current_playlist = self.playlist_manager.get_current_playlist()
                if current_playlist:
                    query = input("Enter search term: ").strip()
                    if query:
                        result = current_playlist.search_song(query)
                        if result:
                            print(f"Found: {result}")
                        else:
                            print("No songs found.")
                else:
                    print("No playlist selected. Please create or switch to a playlist first.")
            
            elif choice == '15':
                current_playlist = self.playlist_manager.get_current_playlist()
                if current_playlist:
                    current_playlist.shuffle_playlist()
                else:
                    print("No playlist selected. Please create or switch to a playlist first.")
            
            elif choice == '16':
                current_playlist = self.playlist_manager.get_current_playlist()
                if not current_playlist:
                    print("No playlist selected. Please create or switch to a playlist first.")
                    continue
                if current_playlist.is_empty():
                    print("Current playlist is empty.")
                    continue
                # Ensure we're at a valid song
                if not current_playlist.get_current_song():
                    current_playlist.go_to_first_song()
                while True:
                    song = current_playlist.get_current_song()
                    if song:
                        self.stacks_queues_player.play_song(song)
                        print(f"🎵 Playing: {song['title']} - {song['artist']}")
                        # Wait for song to finish (simulated here; pygame can handle this differently)
                        input("Press Enter to play next song, or Ctrl+C to stop...")
                        current_playlist.next_song()
                        if not current_playlist.get_current_song():
                            current_playlist.go_to_first_song()
                    else:
                        print("Reached end of playlist.")
                        break
            
            elif choice == '17':
                self.stacks_queues_player.stop_song()
                break
            
            else:
                print("Invalid choice. Please try again.")

    def show_stacks_queues_menu(self):
        """Display the stacks and queues menu."""
        while True:
            print("\n" + "=" * 50)
            print("🎯 STACKS & QUEUES FEATURES")
            print("=" * 50)
            print("1. 📊 Display All Queues & Status")
            print("2. ➡️  Add Song to Play Next Queue")
            print("3. ⏭️  Play Next Song")
            print("4. 🎉 Add Song to Party Queue")
            print("5. ⬆️  Upvote Song in Party Queue")
            print("6. 🎵 Play from Party Queue")
            print("7. 📜 View Listening History")
            print("8. 🔍 Search Listening History")
            print("9. 🗑️  Clear Play Next Queue")
            print("10. 🗑️  Clear Party Queue")
            print("11. ⬅️  Back to Main Menu")
            print("-" * 50)
            
            choice = input("Enter your choice (1-11): ").strip()
            
            if choice == '1':
                self.stacks_queues_player.display_all_queues()
            
            elif choice == '2':
                self._add_to_play_next()
            
            elif choice == '3':
                self.stacks_queues_player.play_next_song()
            
            elif choice == '4':
                self._add_to_party_queue()
            
            elif choice == '5':
                self.stacks_queues_player.party_queue.display_queue()
                song_title = input("Enter song title to upvote: ").strip()
                if song_title:
                    self.stacks_queues_player.upvote_song_in_party_queue(song_title)
            
            elif choice == '6':
                self.stacks_queues_player.play_from_party_queue()
            
            elif choice == '7':
                limit = input("How many recent songs to show (default 10): ").strip()
                try:
                    limit_val = int(limit) if limit.isdigit() else 10
                    self.stacks_queues_player.listening_history.display_history(limit_val)
                except ValueError:
                    self.stacks_queues_player.listening_history.display_history()
            
            elif choice == '8':
                query = input("Enter search term: ").strip()
                if query:
                    results = self.stacks_queues_player.listening_history.search_history(query)
                    if results:
                        print(f"\nFound {len(results)} songs in history:")
                        for i, song in enumerate(results, 1):
                            print(f"{i}. {song['title']} - {song['artist']}")
                    else:
                        print("No songs found in history.")
            
            elif choice == '9':
                self.stacks_queues_player.play_next_queue.clear_queue()
            
            elif choice == '10':
                self.stacks_queues_player.party_queue.clear_queue()
            
            elif choice == '11':
                self.stacks_queues_player.stop_song()
                break
            
            else:
                print("Invalid choice. Please try again.")
    
    def _add_to_play_next(self):
        """Helper method to add songs to play next queue."""
        song_library = self.music_manager.get_song_library()
        print("\nAvailable songs:")
        for i, song in enumerate(song_library[:10], 1):  # Show first 10
            print(f"{i}. {song['title']} - {song['artist']}")
        
        try:
            song_idx = int(input("Enter song number: ")) - 1
            if 0 <= song_idx < len(song_library):
                self.stacks_queues_player.add_to_play_next(song_library[song_idx])
            else:
                print("Invalid song number.")
        except ValueError:
            print("Please enter a valid number.")
    
    def _add_to_party_queue(self):
        """Helper method to add songs to party queue."""
        song_library = self.music_manager.get_song_library()
        print("\nAvailable songs:")
        for i, song in enumerate(song_library[:10], 1):  # Show first 10
            print(f"{i}. {song['title']} - {song['artist']}")
        
        try:
            song_idx = int(input("Enter song number: ")) - 1
            if 0 <= song_idx < len(song_library):
                priority = input("Enter priority (0=normal, 1+=high): ").strip()
                priority_val = int(priority) if priority.isdigit() else 0
                self.stacks_queues_player.add_to_party_queue(song_library[song_idx], priority_val)
            else:
                print("Invalid song number.")
        except ValueError:
            print("Please enter a valid number.")
    
    def quick_play(self):
        """Quick play functionality."""
        print("\n🎵 QUICK PLAY")
        print("=" * 30)
        
        song_library = self.music_manager.get_song_library()
        print("Available songs:")
        for i, song in enumerate(song_library[:8], 1):
            print(f"{i}. {song['title']} - {song['artist']}")
        
        try:
            song_idx = int(input("Enter song number to play: ")) - 1
            if 0 <= song_idx < len(song_library):
                song = song_library[song_idx]
                self.stacks_queues_player.play_song(song)
                print(f"🎵 Now playing: {song['title']} - {song['artist']}")
                input("Press Enter to stop playback...")
                self.stacks_queues_player.stop_song()
            else:
                print("Invalid song number.")
        except ValueError:
            print("Please enter a valid number.")
    
    def view_all_status(self):
        """Display status of all components."""
        print("\n" + "=" * 80)
        print("📊 COMPLETE MUSIC PLAYER STATUS")
        print("=" * 80)
        
        # Library status
        song_library = self.music_manager.get_song_library()
        print(f"📚 Music Library: {len(song_library)} songs")
        
        # Playlist management status
        if self.playlist_manager:
            total_playlists = len(self.playlist_manager.playlists)
            current_playlist_name = self.playlist_manager.current_playlist_name
            print(f"📋 Playlist Manager: {total_playlists} playlists")
            if current_playlist_name:
                current_playlist = self.playlist_manager.get_current_playlist()
                if current_playlist:
                    print(f"   Active: {current_playlist_name} ({current_playlist.get_size()} songs)")
                    if not current_playlist.is_empty():
                        current_song = current_playlist.get_current_song()
                        if current_song:
                            print(f"   Current: {current_song['title']} - {current_song['artist']}")
        
        # Stacks & Queues status
        if self.stacks_queues_player:
            print(f"➡️  Play Next Queue: {self.stacks_queues_player.play_next_queue.get_size()} songs")
            print(f"🎉 Party Queue: {self.stacks_queues_player.party_queue.get_size()} songs")
            print(f"📜 Listening History: {self.stacks_queues_player.listening_history.get_size()} songs")
            
            if self.stacks_queues_player.currently_playing:
                current = self.stacks_queues_player.currently_playing
                print(f"🎵 Currently Playing: {current['title']} - {current['artist']}")
        
        print("=" * 80)
    
    def run(self):
        """Main run loop."""
        if not self.initialize_music_library():
            print("❌ Failed to initialize music library. Exiting.")
            return
        
        while True:
            self.show_main_menu()
            choice = input("Enter your choice (1-6): ").strip()
            
            if choice == '1':
                self.show_library_menu()
            
            elif choice == '2':
                self.show_playlist_management_menu()
            
            elif choice == '3':
                self.show_stacks_queues_menu()
            
            elif choice == '4':
                self.view_all_status()
            
            elif choice == '5':
                self.quick_play()
            
            elif choice == '6':
                self.stacks_queues_player.stop_song()
                print("\n🎵 Thanks for using the Main Music Player! Goodbye! 🎵")
                break
            
            else:
                print("Invalid choice. Please try again.")

def main():
    """Main function."""
    try:
        player = MainMusicPlayer()
        player.run()
    except KeyboardInterrupt:
        print("\n\n🎵 Music player interrupted. Goodbye! 🎵")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()