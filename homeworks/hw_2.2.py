# I dati dell'utente sono:
# - `Nickname`
# - `Eta`
# - `Gender` (per semplicità solo `M` o `F`)

from distutils.log import error


print("\nBenvenuti al portale di registrazione del Gamble Casino")
n=int(input("Quanti utenti vuoi registrare? "))

utenti = 0
nicks = []  #lista con i nomi utente
error = False
users = []  #lista di dizionari con tutte le informazioni utente

### REGISTRAZIONE ###
while utenti < n and not(error):
    name = input("\nInserisci nome utente: ")
    age = int(input("Inserisci età: "))
    gender = input("Inserisci gender: ")
    games = input("Inserisci i giochi preferiti: ").split(",")

    #Controllo se l'utente è maggiorenne
    while age < 18:
        print("L'utente è minorenne, per tanto non può essere registrato. Inserire nuovo utente. \n")
        name = input("Inserisci nome utente: ")
        age = int(input("Inserisci età: "))
        gender = input("Inserisci gender: ")
        games = input("Inserisci i giochi preferiti: ").split(",")

    while len(name) <= 2:
        print("\nNome utente non valido (min. 3 lettere)")
        name = input("Inserisci nuovo nome utente: ")

    #Controllo se l'utente è già stato registrato
    if name in nicks:
        print("Utente già inserito, processo di registrazione terminato")
        error = True
    else:
        nicks.append(name)

    for i in range(len(games)):
        games[i] = games[i].strip()

    #Registrazione dell'utente nel database
    if not(error):
        user = {"nickname": name, "age": age, "gender": gender, "games": games}
        users.append(user)
        print("Registrazione dell'utente {} completata" .format(utenti+1))

    #Aggiornamento del counter
    utenti += 1

#Comunicazione di corretta esecuzione del programma
if not(error):
    print("\nProcesso di registrazione completata: N = {} utenti sono stati correttamente registrati \n" .format(n))
else:
    print("\nProcesso di registrazione NON completato!")

### ANALISI: calcolare età media e numero di utenti per genere ###
ages_sum = 0
females = 0
games_frequency = []
games_names = []

for user in users:
    ages_sum += user["age"]
    if user["gender"] == 'F': females += 1
    for each_game in user["games"]:
        if each_game in games_names:
           games_frequency[games_names.index(each_game)] += 1
        else:
            games_names.append(each_game)
            games_frequency.append(1)

print("L'età media degli utenti registrati è {}." .format(ages_sum/n))
print("Sono stati registrati {} utenti di genere maschile e {} utenti di genere femminile." .format(n-females, females))

max = 0
pos = 0
for i in (0,len(games_frequency)-1):
    if games_frequency[i] > max:
        max = games_frequency[i]
        pos = i
print("Il gioco preferito degli utenti è {}. \n" .format(games_names[pos]))