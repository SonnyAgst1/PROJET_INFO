def importdonneespur(chemin):
    data = []

    with open(chemin, newline='', encoding="utf-8") as f:
        lecteur = csv.DictReader(f)
        for ligne in lecteur:
            data.append(ligne)
    return data
