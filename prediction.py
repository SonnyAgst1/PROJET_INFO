import pandas as pd
import numpy as np
import os
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

def train_and_save_model(df, model_path="modele_medaille.pkl", cols_path="colonnes.pkl"):
    """
    Entraîne le modèle et sauvegarde le modèle + colonnes encodées.
    """
    df = df.copy()
    df["Medal_binary"] = df["Medal"].notna().astype(int)
    X = df[["Age", "Height", "Weight", "Sex", "Sport", "NOC"]]
    y = df["Medal_binary"]

    X = X.dropna()
    y = y.loc[X.index]
    X_encoded = pd.get_dummies(X, columns=["Sex", "Sport", "NOC"])

    model = LogisticRegression(max_iter=1000)
    model.fit(X_encoded, y)

    joblib.dump(model, model_path)
    joblib.dump(X_encoded.columns, cols_path)
    print("✅ Modèle et colonnes enregistrés.")


def predict_medal_chance(df, age, height, weight, sex, sport, noc,
                         model_path="modele_medaille.pkl", cols_path="colonnes.pkl"):
    """
    Prédit la probabilité qu'un athlète remporte une médaille à partir de ses caractéristiques.
    Charge le modèle entraîné si disponible, sinon l'entraîne et l'enregistre.
    """

    # Vérifier si le modèle existe déjà
    if not (os.path.exists(model_path) and os.path.exists(cols_path)):
        print("⚠️ Modèle non trouvé. Entraînement en cours...")
        train_and_save_model(df, model_path, cols_path)

    # Charger le modèle et les colonnes
    model = joblib.load(model_path)
    colonnes = joblib.load(cols_path)

    # Construire le vecteur de l’athlète
    athlete = {
        "Age": age,
        "Height": height,
        "Weight": weight,
        f"Sex_{sex}": 1,
        f"Sport_{sport}": 1,
        f"NOC_{noc}": 1
    }

    # Créer une ligne vide avec les bonnes colonnes
    athlete_row = pd.DataFrame(np.zeros((1, len(colonnes))), columns=colonnes)

    # Remplir les colonnes connues
    for col in athlete:
        if col in athlete_row.columns:
            athlete_row[col] = athlete[col]

    # Prédiction
    prob = model.predict_proba(athlete_row)[0][1]
    return prob

# Chargement de ta base
df = pd.read_csv("donnees_jeux_olympiques/athlete_events.csv")

# Prédiction directe (le modèle s'entraîne une seule fois puis est réutilisé)
proba = predict_medal_chance(df, 25, 195, 95, "M", "Basketball", "USA")
print(f"Probabilité de médaille : {proba:.2%}")
