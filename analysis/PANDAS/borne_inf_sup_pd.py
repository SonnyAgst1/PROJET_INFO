
def borne_inf_sup_pd(df):
    # Filtrer sur l'année 2016 et les lignes avec médaille réelle
    df_2016 = df[(df["Year"] == 2016) & (df["Medal"] != "NA")]

    # Supprimer les doublons
    df_2016_unique = df_2016.drop_duplicates(
        subset=["Games", "Sport", "Event", "Medal", "NOC"]
    )

    # Compter les médailles par pays
    medal_counts = df_2016_unique["NOC"].value_counts()

    min_medals = medal_counts.min()
    max_medals = medal_counts.max()

    pays_min = medal_counts[medal_counts == min_medals].index.tolist()
    pays_max = medal_counts[medal_counts == max_medals].index.tolist()

    noc_to_team = (
        df_2016.drop_duplicates(subset=["NOC"])[["NOC", "Team"]]
        .set_index("NOC")["Team"]
        .to_dict()
    )
    pays_min_names = [noc_to_team.get(noc, noc) for noc in pays_min]
    pays_max_names = [noc_to_team.get(noc, noc) for noc in pays_max]

    # Construire le texte
    lignes = []
    lignes.append("Question 10 : Analyse des médailles aux JO 2016\n")
    lignes.append(f"Borne inférieure : {min_medals} médailles — {', '.join(pays_min_names)}")
    lignes.append(f"Borne supérieure : {max_medals} médailles — {', '.join(pays_max_names)}\n")
    lignes.append("Top 5 des pays les plus médaillés :")
    for i, (noc, count) in enumerate(medal_counts.head(5).items(), 1):
        nom_pays = noc_to_team.get(noc, noc)
        lignes.append(f"{i}. {nom_pays} : {count} médailles")

    return "\n".join(lignes)
