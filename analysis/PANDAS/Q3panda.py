import pandas as pd
import matplotlib.pyplot as plt
from import_donnee_panda import importdonneepanda
# Charger la base de données
df_panda = importdonneepanda("donnees_jeux_olympiques/athlete_events.csv")

# Charge la base de données
def profil_moyen(df):

    profil_moyen_sport = df.groupby("Sport")[["Age", "Height", "Weight"]].mean()
    return print("profil moyen par sport : ", profil_moyen_sport)

profil_moyen(df_panda)
