import pandas as pd
def analyser_jo_2016_df(df):
    """
    Analyse les résultats des Jeux Olympiques de 2016 à partir d'un DataFrame.

    Cette fonction extrait les médailles obtenues en 2016, filtre les doublons
     pour ne compter 
    qu'une seule fois chaque médaille attribuée à un pays dans une épreuve 
    donnée, et affiche :
        - le nombre minimum et maximum de médailles obtenues par un pays,
        - la liste des pays concernés par ces bornes,
        - le top 5 des pays les plus médaillés.

    Paramètres
    ----------
    df : pandas.DataFrame
        Le DataFrame contenant les données des Jeux Olympiques, avec au
         minimum les colonnes
        'Year', 'Medal', 'Games', 'Sport', 'Event', 'NOC', et 'Team'.

    Retourne
    --------
    str
        Une chaîne de caractères résumant les résultats de l'analyse pour les 
        JO de 2016.
    """
    df_2016 = df[(df["Year"] == 2016) & (df["Medal"].notna())]
    # Suppression des doublons (même médaille dans une même épreuve)
    df_unique = df_2016.drop_duplicates(
        subset=["Games", "Sport", "Event", "Medal", "NOC"])

    # Comptage des médailles par pays
    medal_counts = df_unique["NOC"].value_counts()

    # Conversion des codes NOC en noms de pays
    noc_to_team = df_unique.drop_duplicates(
        "NOC").set_index("NOC")["Team"].to_dict()

    min_medals = medal_counts.min()
    max_medals = medal_counts.max()

    pays_min = [noc_to_team[noc] for noc in medal_counts[
        medal_counts == min_medals].index]
    pays_max = [noc_to_team[noc] for noc in medal_counts[
        medal_counts == max_medals].index]

    result = "Résultats pour les JO de 2016 :\n"
    result += f"  ▪ Borne inférieure : {min_medals} médailles — {pays_min}\n"
    result += f"  ▪ Borne supérieure : {max_medals} médailles — {pays_max}\n"
    result += "\nTop 5 des pays les plus médaillés en 2016 :\n"

    top5 = medal_counts.head(5)
    for i, (noc, count) in enumerate(top5.items(), start=1):
        result += f"  {i}. {noc_to_team[noc]} : {count} médailles\n"

    return result
