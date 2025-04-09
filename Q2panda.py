import pandas as pd
import matplotlib.pyplot as plt

# Charger la base de données
df = pd.read_csv("donnees_jeux_olympiques/athlete_events.csv")

# Initialiser une liste pour stocker les corrélations par année
correlations = []

# Boucle sur chaque année unique
for year in sorted(df["Year"].unique()):
    df_year = df[df["Year"] == year]

    # Nombre d'athlètes uniques par pays
    athletes_per_country = df_year.groupby("NOC")["ID"].nunique().reset_index()
    athletes_per_country.columns = ["NOC", "Nb_Athletes"]

    # Nombre de médailles par pays
    medals_per_country = df_year[df_year["Medal"].notna()].groupby("NOC")["Medal"].count().reset_index()
    medals_per_country.columns = ["NOC", "Nb_Medals"]

    # Fusion
    merged = pd.merge(athletes_per_country, medals_per_country, on="NOC", how="left")
    merged["Nb_Medals"] = merged["Nb_Medals"].fillna(0)

    # Calcul de la corrélation (seulement si au moins 2 pays ont des données)
    if len(merged) >= 2:
        corr = merged["Nb_Athletes"].corr(merged["Nb_Medals"])
        correlations.append((year, corr))

# Convertir en DataFrame
df_corr = pd.DataFrame(correlations, columns=["Year", "Correlation"])

# Afficher l’évolution de la corrélation au fil des années
plt.figure(figsize=(12, 6))
plt.plot(df_corr["Year"], df_corr["Correlation"], marker="o")
plt.title("Corrélation entre nombre d'athlètes et nombre de médailles par pays (toutes années)")
plt.xlabel("Année")
plt.ylabel("Corrélation (athlètes vs médailles)")
plt.grid(True)
plt.tight_layout()
plt.show()
