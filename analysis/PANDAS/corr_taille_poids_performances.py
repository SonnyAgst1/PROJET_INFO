import pandas as pd

def corr_taille_poids_performances_pd(df):
    """
    Analyse la corrélation entre taille/poids et nombre de médailles par sport.

    Paramètre :
    - df : DataFrame contenant les données des athlètes

    Retourne :
    - correlations : DataFrame trié des sports où taille et poids sont les 
    plus liés au nombre de médailles
    """

    df_filtered = df.dropna(subset=['Height', 'Weight']) 

    medals_per_athlete = df_filtered[df_filtered['Medal'].notna()] \
        .groupby('Name')['Medal'].count().reset_index()
    medals_per_athlete.rename(columns={'Medal': 'Num_Medals'}, inplace=True)

    df_filtered = df_filtered.merge(medals_per_athlete, on='Name', how='left')
    df_filtered['Num_Medals'] = df_filtered['Num_Medals'].fillna(0)

    def most_frequent_sport(sports):
        return sports.mode(        
        ).iloc[0] if not sports.mode().empty else sports.iloc[0]

    athlete_data = df_filtered.groupby('Name').agg({
        'Height': 'mean',
        'Weight': 'mean',
        'Num_Medals': 'max',
        'Sport': most_frequent_sport
    }).reset_index()
    results = []
    for sport, group in athlete_data.groupby('Sport'):
        if len(group) < 10 or group['Num_Medals'].nunique() < 2:
            continue

        corr_height = group['Height'].corr(group['Num_Medals'])
        corr_weight = group['Weight'].corr(group['Num_Medals'])
        combined = abs(corr_height) + abs(corr_weight)

        results.append({
            'Sport': sport,
            'Corr_Height': abs(corr_height),
            'Corr_Weight': abs(corr_weight),
            'Combined': combined
        })
    return results
