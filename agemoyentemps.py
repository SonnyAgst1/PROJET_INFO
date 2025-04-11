import pandas as pd
import matplotlib.pyplot as plt


# Charger la base de données
df = pd.read_csv("donnees_jeux_olympiques/athlete_events.csv")
#on enlève les athlètes en double pour une année
df_unique = df.drop_duplicates(subset=["ID", "Year"])

age_moyen_par_annee = df_unique.groupby("Year")["Age"].mean()

plt.figure(figsize=(10, 5))
plt.plot(age_moyen_par_annee.index, age_moyen_par_annee.values, marker="o")
plt.title("Age moyen des athlètes par années")
plt.xlabel("Année")
plt.ylabel("Age moyen des athlètes")
plt.grid(True)
plt.tight_layout()
plt.show()
