import json
from logging import raiseExceptions
import requests
import random

def get_albums(id): 
  a_url = "https://api.deezer.com/artist/{}".format(id)
  response = requests.get(a_url).json()
  a_album = response["nb_album"]
  return int(a_album)

#open the file containing the available artists
with open("lezione6/data/artists.json", "r") as file:
    artists = json.load(file)

valid_aswers = ('1','2')

random_artists = random.sample(list(artists.keys()),2)
#artist_id_1 = random.choice(list(artists.keys())) 
#artist_id_2 = random.choice(list(artists.keys()))
questions = 0
correct = 0
command = 'y'

print("--- Benvenuto nel Deezer Trivia Quiz ---")
while command.capitalize() == 'Y' :
    questions += 1
    print("Domanda {}: Chi ha pubblicato più album tra '{}'(1) e '{}'(2)?".format(questions, random_artists[0], random_artists[1]))
    
    answer = input(">> ")
    notValid = True
    while notValid:
        try:
            if answer not in valid_aswers:
                raise Exception("Input non valido, rispondere con '1' o '2'")
            else: notValid = False
        except Exception as ex:
            print(ex)
            answer = input(">> ")
    if answer == '1':
        print("La tua risposta è: {}".format(random_artists[0]))
    else:
        print("La tua risposta è: {}".format(random_artists[1]))

    #verification part
    NbAlbum1 = get_albums(artists[random_artists[0]])
    NbAlbum2 = get_albums(artists[random_artists[1]])

    if answer == '1' and NbAlbum1 > NbAlbum2:
        print("La tua risposta è corretta!")
        print("{} ha pubblicato {} albums, {} ne ha pubblicati {}". format(random_artists[0], NbAlbum1, random_artists[1], NbAlbum2))
        correct += 1
    elif answer == '2' and NbAlbum1 < NbAlbum2:
        print("La tua risposta è corretta!")
        print("{} ha pubblicato {} albums, {} ne ha pubblicati {}". format(random_artists[0], NbAlbum1, random_artists[1], NbAlbum2))
        correct += 1
    else: 
        print("La tua rispost è errata!")
        print("{} ha pubblicato {} albums, {} ne ha pubblicati {}". format(random_artists[0], NbAlbum1, random_artists[1], NbAlbum2))

    #loop management
    command = input("Vuoi proseguire? (premi Y per continuare) ")
    #artist_id_1 = random.choice(list(artists.keys()))
    #artist_id_2 = random.choice(list(artists.keys()))
    random_artists = random.sample(list(artists.keys()),2)

print("Il tuo punteggio è {} su {}".format(correct, questions))