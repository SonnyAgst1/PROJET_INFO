import pandas as pd
from import_donnee_panda import importdonneepanda

df_panda = importdonneepanda("donnees_jeux_olympiques/athlete_events.csv")

def nbr_medailles(df, athlete_name):
    athlete_df = df[df["Name"] == athlete_name]
    medaille_count = athlete_df["Medal"].value_counts()
    return medaille_count

print(nbr_medailles()
