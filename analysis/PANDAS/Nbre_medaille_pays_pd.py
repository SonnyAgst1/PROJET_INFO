import pandas as pd

def moyenne_medailles_par_pays_par_annee(df):
    """
    Calcule la moyenne de médailles par pays sur l'ensemble des années olympiques.

    Paramètre :
    - df : DataFrame Pandas contenant les colonnes 'Team', 'Year', 'Medal'

    Retourne :
    - DataFrame : Moyenne des médailles par pays triée par ordre décroissant
    """

    # Filtrer uniquement les lignes où une médaille a été remportée
    df_medals = df[df["Medal"].notna()]

    # Compter le nombre total de médailles par pays et par année
    medal_counts = df_medals.groupby(["Team", "Year"]).size().reset_index(name="Nb_Medals")

    # Calculer la moyenne par pays
    moyennes = medal_counts.groupby("Team")["Nb_Medals"].mean().reset_index()

    # Renommer la colonne pour plus de clarté
    moyennes.columns = ["Team", "Moyenne_medailles_par_annee"]

    # Trier par ordre décroissant
    moyennes = moyennes.sort_values(by="Moyenne_medailles_par_annee", ascending=False)

    return moyennes
