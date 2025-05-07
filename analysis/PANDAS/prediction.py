import pandas as pd
import numpy as np
import os
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib


def create_medal_binary(df):
    """
    Crée la colonne `Medal_binary` pour indiquer si un athlète a gagné au moins une médaille.

    - 1 : a gagné au moins une médaille
    - 0 : aucune médaille

    """
    # Crée un DataFrame avec 1 si au moins une médaille, 0 sinon
    medal_counts = df.groupby("ID")["Medal"].apply(lambda x: 1 if x.notna().any() else 0)

    # Associer cette information à chaque ligne
    df = df.merge(medal_counts.rename("Medal_binary"), left_on="ID", right_index=True)

    return df

def train_and_save_model(df, model_path="modele_medaille.pkl", cols_path="colonnes.pkl"):
    """
    Entraîne le modèle et sauvegarde le modèle + colonnes encodées.
    Gère les valeurs manquantes de Age, Height, Weight séparément pour les hommes et les femmes.
    Prend en compte le statut 'Medal_binary' au niveau de l'athlète.
    """
    df = df.copy()

    # Créer la colonne `Medal_binary` par athlète (ID)
    df = create_medal_binary(df)

    # Sélection des colonnes explicatives et de la cible
    X = df[["Age", "Height", "Weight", "Sex", "Sport", "NOC"]]
    y = df["Medal_binary"]

    # Gestion des valeurs manquantes par sexe (médiane)
    for sex in ["M", "F"]:
        subset = X[X["Sex"] == sex]

        # Calcul des médianes
        age_median = subset["Age"].median()
        height_median = subset["Height"].median()
        weight_median = subset["Weight"].median()

        # Imputation
        X.loc[X["Sex"] == sex, "Age"] = X.loc[X["Sex"] == sex, "Age"].fillna(age_median)
        X.loc[X["Sex"] == sex, "Height"] = X.loc[X["Sex"] == sex, "Height"].fillna(height_median)
        X.loc[X["Sex"] == sex, "Weight"] = X.loc[X["Sex"] == sex, "Weight"].fillna(weight_median)

    # Supprimer les lignes restantes avec des valeurs manquantes
    X = X.dropna()
    y = y.loc[X.index]

    # Encodage des variables catégorielles
    X_encoded = pd.get_dummies(X, columns=["Sex", "Sport", "NOC"])

    # Entraînement du modèle
    model = LogisticRegression(max_iter=1000)
    model.fit(X_encoded, y)

    # Sauvegarde du modèle et des colonnes encodées
    joblib.dump(model, model_path)
    joblib.dump(X_encoded.columns, cols_path)
    print("✅ Modèle et colonnes enregistrés avec gestion de `Medal_binary` par athlète (médiane utilisée).")



def predict_medal_chance(df, age, height, weight, sex, sport, noc,
                         model_path="modele_medaille.pkl", cols_path="colonnes.pkl"):
    """
    Prédit la probabilité qu'un athlète remporte une médaille à partir de ses caractéristiques.
    Charge le modèle entraîné si disponible, sinon l'entraîne et l'enregistre.

    Gestion des valeurs manquantes basée sur les médianes par sexe.
    """

    # Vérifier si le modèle et les colonnes existent
    if not (os.path.exists(model_path) and os.path.exists(cols_path)):
        print("⚠️ Modèle non trouvé. Entraînement en cours...")
        train_and_save_model(df, model_path, cols_path)

    # Charger le modèle et les colonnes
    model = joblib.load(model_path)
    colonnes = joblib.load(cols_path)

    # Créer le vecteur de l’athlète
    athlete = {
        "Age": age,
        "Height": height,
        "Weight": weight,
        f"Sex_{sex}": 1,
        f"Sport_{sport}": 1,
        f"NOC_{noc}": 1
    }

    # Créer un DataFrame vide avec les colonnes attendues
    athlete_row = pd.DataFrame(np.zeros((1, len(colonnes))), columns=colonnes)

    # Remplir les colonnes fournies
    for col in athlete:
        if col in athlete_row.columns:
            athlete_row[col] = athlete[col]

    # Gestion des valeurs manquantes pour l'athlète
    # Obtenir les **médianes** par sexe dans le DataFrame d'entraînement
    for sex_value in ["M", "F"]:
        subset = df[df["Sex"] == sex_value]
        age_median = subset["Age"].median()
        height_median = subset["Height"].median()
        weight_median = subset["Weight"].median()

        # Appliquer les médianes si la colonne est restée à 0 ou est NaN
        if sex == sex_value:
            if age == 0 or pd.isna(age):
                athlete_row["Age"] = age_median
            if height == 0 or pd.isna(height):
                athlete_row["Height"] = height_median
            if weight == 0 or pd.isna(weight):
                athlete_row["Weight"] = weight_median

    # Prédiction
    prob = model.predict_proba(athlete_row)[0][1]
    return prob


