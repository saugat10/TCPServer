import socket
import json

# create socket
s = socket.socket()
print('Socket Created')

# bind socket with port number by passing ip address and port number
s.bind(("localhost", 43214))

s.listen(3)
print('waiting for connection')

movies = [
    {"Id": 1, "MovieName": "Dune", "LengthInMinutes": 155, "CountryOfOrigin": "USA"},
    {"Id": 2, "MovieName": "The Fifth Element", "LengthInMinutes": 126, "CountryOfOrigin": "USA"},
    {"Id": 3, "MovieName": "Martyrs", "LengthInMinutes": 99, "CountryOfOrigin": "France"}
]


def getAll():
    return movies


def getByCountry(country):
    movieList = []
    for index in range(len(movies)):
        if movies[index]["CountryOfOrigin"].upper().strip() == country.strip():
            movieList.append(movies[index])
    return movieList


while True:
    c, addr = s.accept()
    ListMovies = []
    name = c.recv(1024).decode()
    print('client connected', addr, name)
    print(name.strip().upper().split(" ")[0])
    print(name)
    if name.strip().upper() == "GETALL":
        getMovies = getAll()
        ListMovies.append(getMovies)
    elif name.strip().upper().split(" ")[0] == "GETBYCOUNTRY":
        values = ""
        if len(name.split(" ")) > 1:
            values = name.split(" ")[1]
        getMovies = getByCountry(values.upper())
        ListMovies.append(getMovies)
    sendMovies = json.dumps(ListMovies)
    c.send(sendMovies.encode())
    c.close()
