class Playlist:
    def __init__(self, name, genre):
        self.name = name
        self.songs = []
        self.genre = genre
        print(f"Playlist '{self.name}' of genre '{self.genre}' created.")

    def add_song(self, song):
        self.songs.append(song)
        print(f"Song '{song}' added to playlist '{self.name}'.")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Song '{song}' removed from playlist '{self.name}'.")
        else:
            print(f"Song '{song}' not found in playlist '{self.name}'.")
    def display_songs(self):
        if self.songs:
            print(f"Songs in playlist '{self.name}':")
            for song in self.songs:
                print(f"- {song}")
        else:
            print(f"No songs in playlist '{self.name}'.")

    def __del__(self):
        print(f"Playlist '{self.name}' deleted.")

my_playlist = Playlist("My Favorite Songs", "Pop")

while True:
    print("\n1. Add song" )
    print("2. Remove song")
    print("3. Display songs")
    print("4. Exit")
    choice = input("Enter your choice: " )

    if choice == '1':
        song = input("Enter song name: " )
        my_playlist.add_song(song)
    elif choice == '2':
        song = input("Enter song name: " )
        my_playlist.remove_song(song)   
    elif choice == '3':
        my_playlist.display_songs()
    elif choice == '4':
        del my_playlist
        break
    else:
        print("Invalid choice. Please try again.")