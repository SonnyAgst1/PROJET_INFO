import pandas as pd
import matplotlib.pyplot as plt

# Charger la base de données
df = pd.read_csv("donnees_jeux_olympiques/athlete_events.csv")
print(df.head())

age_moyen = df["Age"].mean()
print("age moyen : " ,age_moyen)
taille_moyen = df["Height"].mean()
print("taille moyenne : ", taille_moyen)
poids_moyen = df["Weight"].mean()
print("poids moyen : ", poids_moyen)

profil_moyen_sport = df.groupby("Sport")[["Age", "Height", "Weight"]].mean()
print("profil moyen par sport : ", profil_moyen_sport)

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
