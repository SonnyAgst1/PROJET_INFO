from collections import defaultdict

# fonction d'Amira mais avec en entré data pour que ça corresponde avec la fonction importdonneepur pour le fichier main

def analyser_jo_par_annee(data, annee):
    """
    Analyse les résultats des JO pour une année donnée à partir d'une liste de dictionnaires (data).

    Paramètres :
    - data : liste de dictionnaires représentant les lignes du fichier CSV
    - annee : année à analyser (int)
    """

    medal_counts = defaultdict(int)
    seen_keys = set()

    for row in data:
        if row['Year'] and row['Medal'] and int(row['Year']) == annee:
            key = (row['Games'], row['Sport'], row['Event'], row['Medal'], row['Team'])
            if key not in seen_keys:
                medal_counts[row['Team']] += 1
                seen_keys.add(key)

    if not medal_counts:
        print(f"\nAucune médaille trouvée pour l'année {annee}.")
        return

    # Bornes inférieure et supérieure
    min_medals = min(medal_counts.values())
    max_medals = max(medal_counts.values())

    pays_min = [team for team, count in medal_counts.items() if count == min_medals]
    pays_max = [team for team, count in medal_counts.items() if count == max_medals]

    print(f"\nRésultats pour les JO de {annee} :")
    print(f"  ▪ Borne inférieure : {min_medals} médailles — {pays_min}")
    print(f"  ▪ Borne supérieure : {max_medals} médailles — {pays_max}")

    print(f"\nTop 5 des pays les plus médaillés en {annee} :")
    top5 = sorted(medal_counts.items(), key=lambda x: x[1], reverse=True)[:5]
    for i, (country, count) in enumerate(top5, start=1):
        print(f"  {i}. {country} : {count} médailles")

import csv

def importdonneespur(chemin):
    data = []
    with open(chemin, newline='', encoding="utf-8") as f:
        lecteur = csv.DictReader(f)
        for ligne in lecteur:
            data.append(ligne)
    return data

def menu():
    chemin = "donnees_jeux_olympiques/donnees_jeux_olympiques/athlete_events.csv"
    data = importdonneespur(chemin)

    print(" Analyse des Jeux Olympiques par année\n")
    while True:
        try:
            annee = int(input("Entre une année (ou 0 pour quitter) : "))
            if annee == 0:
                print("Fin du programme.")
                break
            analyser_jo_par_annee(data, annee)
        except ValueError:
            print("Merci d'entrer une année valide.\n")

menu()
