import csv

data = []

with open("donnees_jeux_olympiques/athlete_events.csv", newline='', encoding="utf-8") as f:
    lecteur = csv.DictReader(f)
    for ligne in lecteur:
        data.append(ligne)
#data est une liste de dictionnaire où chaque dictionnaire correspond à une ligne
#on veut reproduire le graphe de l'évolution de l'age moyen des athlètes mais en python pur
