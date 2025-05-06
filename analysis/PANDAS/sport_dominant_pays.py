import pandas as pd

def sport_dominant_par_noc(df):
    """
    Calcule, pour chaque pays (NOC) ayant gagné au moins 10 médailles
    dans au moins 3 sports différents, le sport dominant et la proportion.

    Paramètre :
    - df : DataFrame Pandas contenant les colonnes 'NOC', 'Sport', 'Medal'

    Retourne :
    - DataFrame trié avec les 10 pays les plus spécialisés parmi les pays "pluridisciplinaires"
    """

    # 1. Ne garder que les lignes avec médaille
    df_medals = df.dropna(subset=["Medal"])

    # 2. Total des médailles par NOC
    total_medailles = df_medals.groupby("NOC").size().reset_index(name="Total_medailles")

    # 3. Compter le nombre de sports différents par NOC
    sports_par_noc = df_medals.groupby("NOC")["Sport"].nunique().reset_index(name="Nb_sports")

    # 4. Fusionner les deux
    stats_pays = pd.merge(total_medailles, sports_par_noc, on="NOC")

    # ❗ Filtrer : au moins 10 médailles ET au moins 3 sports différents
    pays_valides = stats_pays[(stats_pays["Total_medailles"] >= 10) & (stats_pays["Nb_sports"] >= 3)]

    # 5. Médailles par NOC et sport
    medals_by_noc_sport = df_medals.groupby(["NOC", "Sport"]).size().reset_index(name="Nb_Medals")

    # 6. Ne garder que les NOC valides
    medals_by_noc_sport = medals_by_noc_sport[medals_by_noc_sport["NOC"].isin(pays_valides["NOC"])]

    # 7. Sport dominant pour chaque NOC
    sport_dominant = medals_by_noc_sport.sort_values("Nb_Medals", ascending=False).drop_duplicates("NOC")

    # 8. Fusion pour calcul du pourcentage
    merged = pd.merge(sport_dominant, pays_valides, on="NOC")
    merged["Proportion"] = merged["Nb_Medals"] / merged["Total_medailles"]

    # 9. Renommer pour clarté
    merged = merged.rename(columns={
        "NOC": "Pays",
        "Sport": "Sport_dominant",
        "Nb_Medals": "Nb_medailles_dans_sport"
    })

    # 10. Trier et retourner
    merged = merged.sort_values("Proportion", ascending=False)

    return merged[["Pays", "Sport_dominant", "Nb_medailles_dans_sport", "Total_medailles", "Proportion"]].head(10)


from import_donnee_panda import importdonneepanda
df_panda = importdonneepanda("analysis/donnees_jeux_olympiques/athlete_events.csv")

result = sport_dominant_par_noc(df_panda)
print(" 10 pays les plus spécialisés (au moins 10 médailles) :")
print(result)
