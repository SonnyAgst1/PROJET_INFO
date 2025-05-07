
def nbr_medailles_pd(df, athlete_name):
    """
    Calcule le nombre de médailles obtenues par un athlète donné.

    Cette fonction filtre les lignes du DataFrame correspondant à un 
    athlète spécifique et comptabilise les types de médailles 
    (Or, Argent, Bronze) qu'il ou elle a remportées.

    Paramètres
    ----------
    df : pandas.DataFrame
        Le DataFrame contenant les données des Jeux Olympiques,
         incluant au minimum 
        les colonnes 'Name' et 'Medal'.
    
    athlete_name : str
        Le nom complet de l'athlète à rechercher (sensible à la casse).

    Retourne
    --------
        Une série contenant le nombre de médailles par 
        type (Gold, Silver, Bronze) 
        pour l'athlète donné. Si l'athlète n'a gagné aucune
         médaille, la série est vide.
    """
    athlete_df = df[(df["Name"] == athlete_name) & (df["Medal"].notna())]
    medaille_count = athlete_df["Medal"].value_counts()
    return medaille_count
