def cargar_canciones(filePath:str)->list:
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
