class Song:
    count = 0
    genre_count = {}
    artist_count = {}

    def __init__(self, title, artist, genre):
        self.title = title
        self.artist = artist
        self.genre = genre

        Song.count += 1

        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1
