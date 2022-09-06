def cargar_canciones(filePath: str) -> list:
    data_dictionary = []
    file = open(filePath)
    file.readline().split(",")
    line = file.readline()

    while (len(line) > 0):
        data = line.split(",")
        song = {}
        song["posicion"] = int(data[0])
        song["nombre_cancion"] = data[1]
        song["nombre_artista"] = data[2]
        song["anio"] = int(data[3])
        song["letra"] = data[4]
        data_dictionary.append(song)
        line = file.readline()
    file.close()

    return data_dictionary


def get_song_by_name_and_year(songs: list, name: str, year: int) -> dict:
    song_found = None
    for song in songs:
        if(song["nombre_cancion"].upper() == name.upper() and song["anio"] == year):
            song_found = song
            break

    return song_found


def get_songs_by_year(songs: list, year: int) -> list:
    song_list = []
    for song in songs:
        if(song["anio"] == year):
            song_found = {}
            song_found['posicion'] = song['posicion']
            song_found['nombre_cancion'] = song['nombre_cancion']
            song_found['nombre_artista'] = song['nombre_artista']
            song_found['anio'] = song['anio']
            song_list.append(song_found)

    return song_list


def get_songs_by_artist_and_years_range(songs: list, artist: str, grant_year: int, less_year: int) -> list:
    song_list = []
    for song in songs:
        if(song["nombre_artista"].upper() == artist.upper() and (song["anio"] >= grant_year and song["anio"] <= less_year)):
            song_found = {}
            song_found['posicion'] = song['posicion']
            song_found['nombre_cancion'] = song['nombre_cancion']
            song_found['nombre_artista'] = song['nombre_artista']
            song_found['anio'] = song['anio']
            song_list.append(song_found)

    return song_list


def get_songs_by_artist(songs: list, artist: str) -> list:
    song_list = []
    for song in songs:
        if(song["nombre_artista"].upper() == artist.upper()):
            song_found = {}
            song_found['posicion'] = song['posicion']
            song_found['nombre_cancion'] = song['nombre_cancion']
            song_found['nombre_artista'] = song['nombre_artista']
            song_found['anio'] = song['anio']
            song_list.append(song_found)

    return song_list


def get_artists_by_song(songs: list, search_song: str) -> list:
    artist_list = []
    for song in songs:
        if(song["nombre_cancion"].upper() == search_song.upper()):
            artist_list.append(song["nombre_artista"])

    return artist_list


def get_quantity_songs(songs: list, minimal_songs: int) -> list:
    songs_by_artists = {}
    list_artists = []
    for song in songs:
        songs_by_artists[song['nombre_artista']] = 0
    for song in songs:
        songs_by_artists[song['nombre_artista']
                         ] += 1
    for artist in songs_by_artists:
        if (songs_by_artists[artist] >= minimal_songs):
            list_artists.append(artist)

    return list_artists


def get_must_popular_artist(songs: list) -> dict:
    songs_by_artists = {}
    most_popular_artist = {}
    grant_quantity_songs = 0
    popular_artist = ''
    for song in songs:
        songs_by_artists[song['nombre_artista']] = 0
    for song in songs:
        songs_by_artists[song['nombre_artista']
                         ] += 1
    for artist in songs_by_artists:
        if (songs_by_artists[artist] > grant_quantity_songs):
            grant_quantity_songs = songs_by_artists[artist]
            popular_artist = artist

    most_popular_artist[popular_artist] = grant_quantity_songs

    return most_popular_artist


def get_songs_by_artist(songs: list) -> dict:
    songs_by_artist = {}
    for song in songs:
        songs_by_artist[song['nombre_artista']] = []
    for song in songs:
        if (not song['nombre_cancion'] in songs_by_artist[song['nombre_artista']]):
            songs_by_artist[song['nombre_artista']].append(
                song['nombre_cancion'])

    return songs_by_artist


def get_songs_average_by_artist(songs: list) -> float:
    songs_by_artist = get_songs_by_artist(songs)
    total_artist = len(list(songs_by_artist))
    total_song = 0

    for artist in songs_by_artist:
        total_song += len(songs_by_artist[artist])

    return total_song/total_artist
