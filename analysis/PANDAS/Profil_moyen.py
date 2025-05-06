import pandas as pd
import matplotlib.pyplot as plt
from import_donnee_panda import importdonneepanda

def profil_moyen(df):
    """
    Calcule le profil moyen (âge, taille, poids) des athlètes médaillés par sport.

    Paramètre :
    - df : DataFrame Pandas contenant les colonnes 'Sport', 'Age', 'Height', 'Weight', 'Medal'

    Retourne :
    - DataFrame : profil moyen des athlètes médaillés par sport
    """

    # 1. Filtrer uniquement les athlètes médaillés
    df_medaille = df[df["Medal"].notna()]

    # 2. Calcul du profil moyen par sport
    profil_moyen_sport = df_medaille.groupby("Sport")[["Age", "Height", "Weight"]].mean()

    print("Profil moyen des athlètes médaillés par sport :")
    print(profil_moyen_sport)

    return profil_moyen_sport
