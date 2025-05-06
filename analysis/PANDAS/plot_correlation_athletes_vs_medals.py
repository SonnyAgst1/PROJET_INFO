import pandas as pd
import matplotlib.pyplot as plt
from import_donnee_panda import importdonneepanda

def plot_correlation_athletes_vs_medals(df):
    correlations = []

    for year in sorted(df["Year"].unique()):
        df_year = df[df["Year"] == year]

        # Nombre d'athlètes uniques par pays
        athletes_per_country = df_year.groupby("NOC")["ID"].nunique().reset_index()
        athletes_per_country.columns = ["NOC", "Nb_Athletes"]

        # Nombre de médailles par pays
        medals_per_country = (
            df_year[df_year["Medal"].notna()]
            .groupby("NOC")["Medal"]
            .count()
            .reset_index()
        )
        medals_per_country.columns = ["NOC", "Nb_Medals"]

        # Fusion
        merged = pd.merge(athletes_per_country, medals_per_country, on="NOC", how="left")
        merged["Nb_Medals"] = merged["Nb_Medals"].fillna(0)

        # Corrélation uniquement si on a au moins 2 pays
        if len(merged) >= 2:
            corr = merged["Nb_Athletes"].corr(merged["Nb_Medals"])
            correlations.append((year, corr))

    # Résultat sous forme de DataFrame
    df_corr = pd.DataFrame(correlations, columns=["Year", "Correlation"])

    # Tracer l’évolution
    plt.figure(figsize=(12, 6))
    plt.plot(df_corr["Year"], df_corr["Correlation"], marker="o")
    plt.title("Corrélation entre nombre d'athlètes et nombre de médailles par pays (toutes années)")
    plt.xlabel("Année")
    plt.ylabel("Corrélation (athlètes vs médailles)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    return plt
