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
    songs_found = None
    song_list = []
    for song in songs:
        if(song["anio"] == year):
            song_found = {}
            song_found['posicion'] = song['posicion']
            song_found['nombre_cancion'] = song['nombre_cancion']
            song_found['nombre_artista'] = song['nombre_artista']
            song_found['anio'] = song['anio']
            song_list.append(song_found)
    if (len(song_list) > 0):
        songs_found = song_list

    return songs_found
