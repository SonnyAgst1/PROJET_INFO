import matplotlib.pyplot as plt
import csv
from collections import defaultdict

def moyenne_medailles_par_pays_par_annee_pur(data):
    """
    Version Python pur.
    Calcule la moyenne de médailles par pays sur l'ensemble des années olympiques.

    Paramètre :
    - data : liste de dictionnaires (issue de csv.DictReader)

    Retourne :
    - Une liste de tuples (pays, moyenne), triée par moyenne décroissante
    """

    # 1. Lister toutes les années des JO
    toutes_les_annees = set()
    for ligne in data:
        toutes_les_annees.add(ligne["Year"])
    nb_annees_totales = len(toutes_les_annees)

    # 2. Compter le nombre total de médailles par pays
    medailles_par_pays = defaultdict(int)
    for ligne in data:
        if ligne["Medal"] and ligne["Medal"] != "NA":
            pays = ligne["Team"]
            medailles_par_pays[pays] += 1

    # 3. Calcul de la moyenne par pays
    moyennes = []
    for pays, total in medailles_par_pays.items():
        moyenne = total / nb_annees_totales
        moyennes.append((pays, moyenne))

    # 4. Tri par moyenne décroissante
    moyennes_triees = sorted(moyennes, key=lambda x: x[1], reverse=True)

    return moyennes_triees


from import_donnee_pur import importdonneespur

data = importdonneespur("analysis/donnees_jeux_olympiques/athlete_events.csv")
resultats = moyenne_medailles_par_pays_par_annee_pur(data)

# Affichage des 10 premiers pays
for team, moyenne in resultats[:10]:
    print(f"{team} : {moyenne:.2f} médailles/an")
