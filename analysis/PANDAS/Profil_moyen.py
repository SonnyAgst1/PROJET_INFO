
def profil_moyen(df):
    """
    Calcule le profil moyen (âge, taille, poids) des 20 athlètes
    les plus médaillés par sport.

    Paramètre :
    - df : DataFrame Pandas contenant les colonnes
    'Sport', 'Age', 'Height', 'Weight', 'Medal'

    Retourne :
    - DataFrame : profil moyen des 20 athlètes les plus médaillés par sport

    """

    # Garder uniquement les athlètes ayant gagné au moins
    # une médaille et des infos valides

    df_medaille = df[df["Medal"].notna()]
    df_medaille = df_medaille.dropna(subset=["Age", "Height", "Weight"])

    #  Compter les médailles par athlète pour chaque sport et sexe
    medals_per_athlete_sport_sex = (
        df_medaille
        .groupby(["Sport", "Sex", "ID", "Name", "Age", "Height", "Weight"])
        .size()
        .reset_index(name="Medal_Count")
    )

    #  Garder les 20 athlètes les plus médaillés pour chaque sport et sexe
    top20_by_sport_sex = (
        medals_per_athlete_sport_sex
        .sort_values(
            ["Sport", "Sex", "Medal_Count"], ascending=[True, True, False])
        .groupby(["Sport", "Sex"])
        .head(20)
    )

    #  Calculer les moyennes (profil type) par sport et sexe
    profil_type_20par_sex = (
        top20_by_sport_sex
        .groupby(["Sport", "Sex"])[["Age", "Height", "Weight"]]
        .mean()
        .round(1)
    )
    return profil_type_20par_sex
