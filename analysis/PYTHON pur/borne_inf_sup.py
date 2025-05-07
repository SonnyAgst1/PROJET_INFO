import csv
from collections import defaultdict


def analyser_jo_par_annee(fichier_csv, annee):
    medal_counts = defaultdict(int)
    seen_keys = set()
    noc_to_team = {}  # Pour convertir NOC à un nom lisible

    with open(fichier_csv, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Year"] and row["Medal"] != "NA" and int(
                        row["Year"]) == annee:
                key = (
                    row["Games"],
                    row["Sport"],
                    row["Event"],
                    row["Medal"],
                    row["NOC"],
                )
                if key not in seen_keys:
                    seen_keys.add(key)
                    noc = row["NOC"]
                    medal_counts[noc] += 1
                    if noc not in noc_to_team:
                        noc_to_team[noc] = row["Team"]

    if not medal_counts:
        print(f"\n Aucune médaille trouvée pour l'année {annee}.")
        return

    min_medals = min(medal_counts.values())
    max_medals = max(medal_counts.values())

    pays_min = [
        noc_to_team[noc] for noc, count in medal_counts.items(

        ) if count == min_medals
    ]
    pays_max = [
        noc_to_team[noc] for noc, count in medal_counts.items(
            
        ) if count == max_medals
    ]

    print(f"\n Résultats pour les JO de {annee} :")
    print(f"  ▪ Borne inférieure : {min_medals} médailles — {pays_min}")
    print(f"  ▪ Borne supérieure : {max_medals} médailles — {pays_max}")

    print(f"\n Top 5 des pays les plus médaillés en {annee} :")
    top5 = sorted(medal_counts.items(), key=lambda x: x[1], reverse=True)[:5]
    for i, (noc, count) in enumerate(top5, start=1):
        print(f"  {i}. {noc_to_team[noc]} : {count} médailles")


def menu(fichier):
    print(" Analyse des Jeux Olympiques par année\n")
    while True:
        try:
            annee = int(input("Entre une année (ou 0 pour quitter) : "))
            if annee == 0:
                print("Fin du programme.")
                break
            analyser_jo_par_annee(fichier, annee)
        except ValueError:
            print("Merci d'entrer une année valide.\n")


fichier = "PROJET_INFO/analysis/donnees_jeux_olympiques/athlete_events.csv"
menu(fichier)
