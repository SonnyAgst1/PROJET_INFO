import pandas as pd

# Charger la base de données
def importdonneepanda(chemin):
    df = pd.read_csv(chemin)
    return df
