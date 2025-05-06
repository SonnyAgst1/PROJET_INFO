from collections import defaultdict

def nbr_medailles(data, athlete_name):
    """
    Compte le nombre de médailles (or, argent, bronze) remportées par un athlète.

    Paramètres :
    - data : liste de dictionnaires (issue d’un fichier CSV)
    - athlete_name : nom complet de l’athlète (str)

    Retourne :
    - Dictionnaire : {"Gold": x, "Silver": y, "Bronze": z}
    """

    resultats = {"Gold": 0, "Silver": 0, "Bronze": 0}

    for ligne in data:
        if ligne["Name"] == athlete_name:
            medaille = ligne["Medal"]
            if medaille in resultats:
                resultats[medaille] += 1

    return resultats
