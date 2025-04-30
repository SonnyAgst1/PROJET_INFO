import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd

def moyenne_medailles_par_pays_par_annee(df):
    """
    Calcule le nombre moyen de médailles par pays au cours des années.

    Paramètre :
    - df : DataFrame Pandas contenant les colonnes 'Team', 'Year', 'Medal'

    Retourne :
    - df_moyennes : DataFrame avec 'Team' et 'Moyenne_medailles_par_annee'
    """

    # 1. Garder uniquement les lignes où une médaille a été remportée
    df_medals = df.dropna(subset=["Medal"])

    # 2. Compter les médailles par pays ET par année
    medal_counts = df_medals.groupby(["Team", "Year"]).size().reset_index(name="Nb_Medals")

    # 3. Moyenne par pays
    moyennes = medal_counts.groupby("Team")["Nb_Medals"].mean().reset_index()
    moyennes.columns = ["Team", "Moyenne_medailles_par_annee"]

    # 4. Trier par ordre décroissant pour affichage
    moyennes = moyennes.sort_values(by="Moyenne_medailles_par_annee", ascending=False)

    return moyennes

df = pd.read_csv("donnees_jeux_olympiques/athlete_events.csv")
resultat = moyenne_medailles_par_pays_par_annee(df)

print("Top 10 des pays avec la meilleure moyenne de médailles par année :")
print(resultat.head(10))
