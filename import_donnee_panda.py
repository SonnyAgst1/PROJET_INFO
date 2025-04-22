import pandas as pd
import matplotlib.pyplot as plt

# Charger la base de données
def importdonneepanda(chemin):
    df = pd.read_csv(chemin)
    return df
