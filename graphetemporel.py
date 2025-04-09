import pandas as pd
import matplotlib.pyplot as plt

# Charger la base de données
df = pd.read_csv("donnees_jeux_olympiques/athlete_events.csv")
import matplotlib.pyplot as plt

athletes_per_year = df.groupby("Year")["ID"].nunique()
df_ete = df[df["Season"] == "Summer"]
df_hiver = df[df["Season"] == "Winter"]

plt.figure(figsize=(10, 5))
plt.plot(..., label="Été")
plt.plot(..., label="Hiver")
plt.legend()
plt.plot(athletes_per_year.index, athletes_per_year.values, marker="o")
plt.title("Nombre total d'athlètes par édition des JO")
plt.xlabel("Année")
plt.ylabel("Nombre d'athlètes uniques")
plt.grid(True)
plt.tight_layout()
plt.show()
