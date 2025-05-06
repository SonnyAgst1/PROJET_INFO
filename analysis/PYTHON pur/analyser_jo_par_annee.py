
import csv
from collections import defaultdict

def analyser_jo_par_annee(fichier_csv, annee):
    medal_counts = defaultdict(int)
    seen_keys = set()

    with open(fichier_csv, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['Year'] and row['Medal'] and int(row['Year']) == annee:
                # Clé unique : 1 médaille décernée à un pays pour une épreuve précise
                key = (int(row['Year']), row['Event'].strip().lower(), row['NOC'], row['Medal'])
                if key not in seen_keys:
                    medal_counts[row['Team']] += 1
                    seen_keys.add(key)

    if not medal_counts:
        print(f"\n Aucune médaille trouvée pour l'année {annee}.")
        return

    # Bornes inférieure et supérieure
    min_medals = min(medal_counts.values())
    max_medals = max(medal_counts.values())

    pays_min = [team for team, count in medal_counts.items() if count == min_medals]
    pays_max = [team for team, count in medal_counts.items() if count == max_medals]

    print(f"\n Résultats pour les JO de {annee} :")
    print(f"  ▪ Borne inférieure : {min_medals} médailles — {pays_min}")
    print(f"  ▪ Borne supérieure : {max_medals} médailles — {pays_max}")


def menu():
    fichier = "athlete_events1.csv"  # nom du fichier que tu as fourni
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

# Lancer le menu
menu()
