import pandas as pd
from import_donnee_panda import importdonneepanda
# Charger la base de données
df_panda = importdonneepanda("donnees_jeux_olympiques/athlete_events.csv")

def sport_medal_correlation(df):
    """
    Analyse la corrélation entre taille/poids et nombre de médailles par sport.

    Paramètre :
    - df : DataFrame contenant les données des athlètes

    Retourne :
    - correlations : DataFrame trié des sports où taille et poids sont les plus liés aux médailles
    """

    # 1. Filtrer les lignes avec Height et Weight valides
    df_filtered = df.dropna(subset=['Height', 'Weight'])

    # 2. Calculer le nombre de médailles par athlète
    medals_per_athlete = (
        df_filtered[df_filtered['Medal'].notna()]
        .groupby('Name')['Medal']
        .count()
        .reset_index()
    )
    medals_per_athlete.rename(columns={'Medal': 'Num_Medals'}, inplace=True)

    # 3. Fusionner pour associer le nombre de médailles à chaque ligne
    df_filtered = df_filtered.merge(medals_per_athlete, on='Name', how='left')
    df_filtered['Num_Medals'] = df_filtered['Num_Medals'].fillna(0)

    # 4. Calcul des corrélations
    results = []

    for sport, group in df_filtered.groupby("Sport"):
        if group['Num_Medals'].nunique() < 2:
            continue  # On ne garde que les sports avec au moins 2 valeurs différentes

        corr_height = group['Height'].corr(group['Num_Medals'])
        corr_weight = group['Weight'].corr(group['Num_Medals'])
        combined = abs(corr_height) + abs(corr_weight)

        results.append({
            'Sport': sport,
            'Corr_Height': abs(corr_height),
            'Corr_Weight': abs(corr_weight),
            'Combined': combined
        })

    correlations = pd.DataFrame(results).sort_values(by='Combined', ascending=False)

    # 5. Affichage et retour
    print("Sports où la taille et le poids sont les plus liés au nombre de médailles :")
    print(correlations.head(10))

    return correlations

print(sport_medal_correlation(df_panda))
