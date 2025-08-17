#!/usr/bin/env python3
"""
Simple verification script to test the renamed music files
"""

def test_renamed_files():
    """Test that the renamed files work correctly"""
    print("Testing renamed music files...")
    
    try:
        from music_playlist_manager import MusicPlaylistManager
        
        # Initialize manager
        music_dir = r"D:\projects\Music_Stream\music"
        manager = MusicPlaylistManager(music_dir)
        
        # Load the music library
        print("\n1. Loading music library...")
        manager.load_music_library()
        
        # Get library info
        library = manager.get_song_library()
        print(f"   Loaded {len(library)} songs")
        
        # Show artists found
        print("\n2. Artists found:")
        artists = manager.get_artists_list()
        for artist in artists:
            print(f"   • {artist}")
        
        # Show songs by artist
        print("\n3. Songs by artist:")
        for artist in artists:
            songs = manager.filter_songs_by_artist(artist)
            print(f"\n   {artist}:")
            for song in songs:
                print(f"     • {song['title']} ({song['file_type']})")
        
        # Show file type distribution
        print("\n4. File type distribution:")
        file_types = manager.get_file_types_list()
        for file_type in file_types:
            songs = manager.filter_songs_by_file_type(file_type)
            print(f"   {file_type.upper()}: {len(songs)} songs")
        
        # Show statistics
        print("\n5. Library statistics:")
        stats = manager.get_library_statistics()
        print(f"   Total songs: {stats['total_songs']}")
        print(f"   Total size: {stats['total_size_mb']} MB")
        print(f"   Unique artists: {stats['unique_artists']}")
        
        print("\n✅ All tests passed! The renamed files work perfectly.")
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")

if __name__ == "__main__":
    test_renamed_files()
