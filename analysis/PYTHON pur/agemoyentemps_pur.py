import csv
from collections import defaultdict
import matplotlib.pyplot as plt
from import_donnee_pur import importdonneespur

data = importdonneespur("donnees_jeux_olympiques/athlete_events.csv")


#data est une liste de dictionnaire où chaque dictionnaire correspond à une ligne
#on veut reproduire le graphe de l'évolution de l'age moyen des athlètes mais en python pur

def agemoyenathlètes(df):
    data_unique = []
    vu = set()
    for ligne in data:
        couple = (ligne["ID"], ligne["Year"])
        if couple not in vu:
            vu.add(couple)
            data_unique.append(ligne)
    #data_unique est le dataframe sans doublons pour pas fausser la moyenne d'age

    D = defaultdict(list)

    for ligne in data_unique:
        annee = ligne["Year"]
        age = ligne["Age"]
        if age != "NA" and age != "":
            D[annee].append(float(age))
    #chaque année est une clé, chaque valeur est une liste contenant les ages des athlètes pour cet année

    agemoyen_par_annee = {}

    for annee, liste_ages in D.items():
        if liste_ages:  # éviter division par zéro
            moyenne = sum(liste_ages) / len(liste_ages)
            agemoyen_par_annee[int(annee)] = moyenne

    annees = sorted(agemoyen_par_annee.keys())
    moyennes = [agemoyen_par_annee[annee] for annee in annees]

    plt.figure(figsize=(10, 5))
    plt.plot(annees, moyennes, marker="o")
    plt.title("Âge moyen des athlètes par année ")
    plt.xlabel("Année")
    plt.ylabel("Âge moyen")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

agemoyenathlètes(data)
