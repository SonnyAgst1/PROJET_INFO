import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd

import pandas as pd
import matplotlib.pyplot as plt

def comparaison_host_vs_nonhost(df):
    """
    Compare le nombre moyen de médailles gagnées par un pays lorsqu’il est hôte
    des JO par rapport aux années où il ne l’est pas et affiche le résultat sous forme de graphique.

    Paramètre :
    - df : DataFrame contenant les données des JO (avec colonnes 'NOC', 'Year', 'Medal')

    Retourne :
    - DataFrame : comparaison des pays organisateurs avec gain moyen de médailles
    """

    # 1. Garder seulement les athlètes médaillés
    df_medals = df[df["Medal"].notna()]

    # 2. Liste des pays hôtes
    host_countries = [
        {"Year": 1896, "City": "Athens", "Host_NOC": "GRE"},
        {"Year": 1900, "City": "Paris", "Host_NOC": "FRA"},
        {"Year": 1904, "City": "St. Louis", "Host_NOC": "USA"},
        {"Year": 1920, "City": "Antwerp", "Host_NOC": "BEL"},
        {"Year": 1924, "City": "Paris", "Host_NOC": "FRA"},
        {"Year": 1936, "City": "Berlin", "Host_NOC": "GER"},
        {"Year": 1948, "City": "London", "Host_NOC": "GBR"},
        {"Year": 1952, "City": "Helsinki", "Host_NOC": "FIN"},
        {"Year": 1956, "City": "Melbourne", "Host_NOC": "AUS"},
        {"Year": 1960, "City": "Rome", "Host_NOC": "ITA"},
        {"Year": 1964, "City": "Tokyo", "Host_NOC": "JPN"},
        {"Year": 1968, "City": "Mexico City", "Host_NOC": "MEX"},
        {"Year": 1972, "City": "Munich", "Host_NOC": "FRG"},
        {"Year": 1976, "City": "Montreal", "Host_NOC": "CAN"},
        {"Year": 1980, "City": "Moscow", "Host_NOC": "URS"},
        {"Year": 1984, "City": "Los Angeles", "Host_NOC": "USA"},
        {"Year": 1988, "City": "Seoul", "Host_NOC": "KOR"},
        {"Year": 1992, "City": "Barcelona", "Host_NOC": "ESP"},
        {"Year": 1996, "City": "Atlanta", "Host_NOC": "USA"},
        {"Year": 2000, "City": "Sydney", "Host_NOC": "AUS"},
        {"Year": 2004, "City": "Athens", "Host_NOC": "GRE"},
        {"Year": 2008, "City": "Beijing", "Host_NOC": "CHN"},
        {"Year": 2012, "City": "London", "Host_NOC": "GBR"},
        {"Year": 2016, "City": "Rio de Janeiro", "Host_NOC": "BRA"},
    ]
    host_df = pd.DataFrame(host_countries)

    # 3. Associer chaque ligne à un pays hôte s’il y a lieu
    df_medals = df_medals.merge(host_df[["Year", "Host_NOC"]], on="Year", how="left")
    df_medals["Is_Host"] = df_medals["NOC"] == df_medals["Host_NOC"]

    # 4. Supprimer les doublons au niveau (NOC, Year, Event, Medal)
    df_medals_unique = df_medals.drop_duplicates(subset=["NOC", "Year", "Event", "Medal"])

    # 5. Calcul des médailles par pays et année
    medals_by_country_year = df_medals_unique.groupby(["NOC", "Year"]).size().reset_index(name="Total_Medals")

    # 6. Marquer si le pays était hôte cette année-là
    host_flags = df_medals_unique[["NOC", "Year", "Is_Host"]].drop_duplicates()
    medals_by_country_year = medals_by_country_year.merge(host_flags, on=["NOC", "Year"], how="left")

    # 7. Comparaison pays par pays
    comparisons = []

    for noc in host_df["Host_NOC"].unique():
        data = medals_by_country_year[medals_by_country_year["NOC"] == noc]
        host_data = data[data["Is_Host"] == True]
        non_host_data = data[data["Is_Host"] == False]

        if not host_data.empty and not non_host_data.empty:
            comparisons.append({
                "Pays (NOC)": noc,
                "Moy. médailles années hôtes": host_data["Total_Medals"].mean(),
                "Moy. médailles autres années": non_host_data["Total_Medals"].mean()
            })

    # 8. Résultat final
    comparison_df = pd.DataFrame(comparisons).sort_values(by="Moy. médailles années hôtes", ascending=False)

    # 9. Visualisation
    plt.figure(figsize=(14, 8))
    bar_width = 0.4
    index = range(len(comparison_df))

    plt.bar(index, comparison_df["Moy. médailles années hôtes"], bar_width, label="Années hôtes", color="#3498db")
    plt.bar([i + bar_width for i in index], comparison_df["Moy. médailles autres années"], bar_width, label="Autres années", color="#95a5a6")

    plt.xlabel("Pays (NOC)")
    plt.ylabel("Nombre moyen de médailles")
    plt.title("Comparaison des médailles gagnées par les pays hôtes vs non-hôtes")
    plt.xticks([i + bar_width / 2 for i in index], comparison_df["Pays (NOC)"], rotation=45, ha="right")
    plt.legend()
    plt.tight_layout()
    plt.show()

    return comparison_df



from importation_donnees_panda import importdonneepanda
df_panda = importdonneepanda("analysis/donnees_jeux_olympiques/athlete_events.csv")

print(comparaison_host_vs_nonhost(df_panda))
