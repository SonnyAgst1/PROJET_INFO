import csv
import matplotlib.pyplot as plt


data = []
with open("donnees_jeux_olympiques/athlete_events.csv", newline='', encoding='utf-8') as f:
    lecteur = csv.DictReader(f)

    compteur = 0
    for ligne in lecteur:
        data.append(ligne)
#Data est maintenant une liste de dictionnaire, chaque élément de la liste représente une ligne
#s'assimile à un dataframe

correlations = []
years = []
for i in data:
    if i["Year"] not in years:
        years.append(i["Year"])
years = sorted(years)
print(years)

athletes_par_pays = {ligne["NOC"]:0 for ligne in data}
medaille_par_pays = {ligne["NOC"]:0 for ligne in data}
ID = []
for ligne in data:
    if ligne["ID"] not in ID:
        pays = ligne["NOC"]
        athletes_par_pays[pays] += 1
        ID.append(ligne["ID"])
    if ligne["Medal"] != 'NA':
        medaille_par_pays[pays] =+ 1


print(athletes_par_pays)
