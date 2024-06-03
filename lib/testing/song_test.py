#!/usr/bin/env python3

import pytest
from song import Song

class TestSong:
    '''Test class for the Song class.'''

    def setup_method(self, method):
        Song.count = 0
        Song.genre_count = {}
        Song.artist_count = {}

    def test_instantiates_with_name_artist_genre(self):
        '''Instantiates a Song object with a title, artist, and genre.'''
        out_of_touch = Song("Out of Touch", "Hall and Oates", "Pop")
        assert out_of_touch.title == "Out of Touch"
        assert out_of_touch.artist == "Hall and Oates"
        assert out_of_touch.genre == "Pop"

    def test_counts_total_song_objects(self):
        '''Counts the total number of Song objects created.'''
        Song("99 Problems", "Jay Z", "Rap")
        Song("Halo", "Beyonce", "Pop")
        Song("Smells Like Teen Spirit", "Nirvana", "Rock")
        assert Song.count == 3
        Song("Sara Smile", "Hall and Oates", "Pop")
        assert Song.count == 4

    def test_tracks_all_song_genres(self):
        '''Tracks all the different Song genres.'''
        Song("99 Problems", "Jay Z", "Rap")
        Song("Halo", "Beyonce", "Pop")
        Song("Smells Like Teen Spirit", "Nirvana", "Rock")
        assert "Rap" in Song.genre_count
        assert "Pop" in Song.genre_count
        assert "Rock" in Song.genre_count

    def test_tracks_all_song_artists(self):
        '''Tracks all the different Song artists.'''
        Song("99 Problems", "Jay Z", "Rap")
        Song("Halo", "Beyonce", "Pop")
        Song("Smells Like Teen Spirit", "Nirvana", "Rock")
        assert "Jay Z" in Song.artist_count
        assert "Beyonce" in Song.artist_count
        assert "Nirvana" in Song.artist_count
        Song("Sara Smile", "Hall and Oates", "Pop")
        assert "Hall and Oates" in Song.artist_count

    def test_tracks_song_count_for_each_genre(self):
        '''Tracks the count of songs for each genre.'''
        Song("99 Problems", "Jay Z", "Rap")
        Song("Halo", "Beyonce", "Pop")
        Song("Smells Like Teen Spirit", "Nirvana", "Rock")
        Song("Sara Smile", "Hall and Oates", "Pop")
        assert Song.genre_count["Rap"] == 1
        assert Song.genre_count["Pop"] == 2
        assert Song.genre_count["Rock"] == 1

    def test_tracks_song_count_for_each_artist(self):
        '''Tracks the count of songs for each artist.'''
        Song("99 Problems", "Jay Z", "Rap")
        Song("Halo", "Beyonce", "Pop")
        Song("Smells Like Teen Spirit", "Nirvana", "Rock")
        Song("Sara Smile", "Hall and Oates", "Pop")
        assert Song.artist_count["Jay Z"] == 1
        assert Song.artist_count["Beyonce"] == 1
        assert Song.artist_count["Nirvana"] == 1
        assert Song.artist_count["Hall and Oates"] == 1

if __name__ == "__main__":
    pytest.main()
