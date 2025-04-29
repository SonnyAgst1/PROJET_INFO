import pandas as pd
import matplotlib.pyplot as plt
from import_donnee_panda import importdonneepanda
# Charger la base de données
df = importdonneepanda("donnees_jeux_olympiques/athlete_events.csv")

# Charge la base de données
def profil_moyen(df):

    profil_moyen_sport = df.groupby("Sport")[["Age", "Height", "Weight"]].mean()
    return print("profil moyen par sport : ", profil_moyen_sport)

profil_moyen(df)

# la suite ne sert pas au code c'est des test
#--------------------------------------------------------------
aero = df[df["Sport"] == "Aeronautics"]
print(aero)
#Il n'y a qu'une personne dans Aeronautics donc autant supprimer ce sport

alpi = df[df["Sport"] == "Alpinism"]
print(alpi)
#Pour l'alpinisme c'est différent, Il y a plusieurs athlète mais les poids et tailles ne sont pas renseigné

print("nobre na alpi:", alpi.isna().sum())
print(" nombre na profil moy : ",profil_moyen_sport.isna().sum())
