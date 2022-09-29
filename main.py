"""
Fait par Alexis Cottier-Guilly
Groupe 402
Ce programme demande un nombre à l'utilisateur (celui-ci peut choisir le nombre minimum et maximum)
et lui dit si le nombre choisis est plus petit, plus grand ou égual au nombre choisis
aléatoirement. L'utilisateur a le choix de rejouer.
"""

import random

jouer = True

while jouer:
    nombre_trouve = False
    essais = 0

    nombre_min_string = input('Nombre minimum (0 par défaut) :\t')
    if nombre_min_string == '':
        nombre_min = 0
    else:
        nombre_min = int(nombre_min_string)

    nombre_max_string = input('Nombre maximum (100 par défaut) :\t')
    if nombre_max_string == '':
        nombre_max = 100
    else:
        nombre_max = int(nombre_max_string)

    nombre = random.randint(nombre_min, nombre_max)

    while not nombre_trouve:
        essais += 1
        nombre_utilisateur = int(input(f"Nombre entre {nombre_min} et {nombre_max} :\t"))

        if nombre > nombre_utilisateur:
            print("Le nombre est plus grand.")
        elif nombre < nombre_utilisateur:
            print("Le nombre est plus petit.")
        else:
            print("Bravo ! vous avez trouvé le nombre !")
            print(f"Vous avez trouvé en {essais} essais")
            nombre_trouve = True
    quitter = input("Voulez vous quitter ? (o/n)\t")
    if quitter == "o":
        jouer = False

print("Merci d'avoir joué et bonne journée !")
