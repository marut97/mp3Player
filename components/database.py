import os
import eyed3


class Database:
    def __init__(self):
        self.path = os.getcwd() + "\\database"
        self.songs = self.__read_songs()

    def __read_songs(self):
        songs = []
        for file in os.listdir(self.path):
            if file.endswith(".mp3"):
                self.__load_song(os.path.join(self.path, file),  songs)
        return songs

    def __load_song(self, path, songs):
        song = eyed3.load(path)
        songs.append([path, song.tag.title, song.info.time_secs, song.tag.album,
                      song.tag.artist, song.tag.getBestDate(), song.tag.genre])

    def get_songs(self):
        return self.songs

    def get_song(self, index):
        if index >= 0 and index < len(self.songs):
            return self.songs[index]

    def get_next_song(self, current_index):
        if current_index + 1 < len(self.songs):
            return self.songs[current_index + 1]
        else:
            return self.songs[0]

    def get_previous_song(self, current_index):
        if current_index - 1 >= 0:
            return self.songs[current_index - 1]
        else:
            return self.songs[len(self.songs) - 1]
