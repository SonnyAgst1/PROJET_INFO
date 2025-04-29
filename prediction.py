import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

from import_donnee_panda import importdonneepanda
# Charger la base de données
df = importdonneepanda("donnees_jeux_olympiques/athlete_events.csv")

def predict_medal_chance(df, age, height, weight, sex, sport, noc):
    """
    Prédit la probabilité pour un athlète de remporter une médaille
    en fonction de ses caractéristiques.

    Paramètres :
    - df : base de données (DataFrame pandas)
    - age : âge de l'athlète (int)
    - height : taille (en cm) (int)
    - weight : poids (en kg) (int)
    - sex : "M" ou "F" (str)
    - sport : sport pratiqué (str)
    - noc : code pays (ex: "FRA") (str)

    Retourne :
    - probabilité de médaille (float entre 0 et 1)
    """

    # 1. Préparation des données
    df = df.copy()
    df["Medal_binary"] = df["Medal"].notna().astype(int)
    X = df[["Age", "Height", "Weight", "Sex", "Sport", "NOC"]]
    y = df["Medal_binary"]

    X = X.dropna()
    y = y.loc[X.index]

    X_encoded = pd.get_dummies(X, columns=["Sex", "Sport", "NOC"])

    # 2. Division train/test
    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.3, random_state=42)

    # 3. Entraînement du modèle
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # 4. Préparation de l'athlète
    athlete = {
        "Age": age,
        "Height": height,
        "Weight": weight,
        f"Sex_{sex}": 1,
        f"Sport_{sport}": 1,
        f"NOC_{noc}": 1
    }

    # Initialiser une ligne vide
    athlete_row = pd.DataFrame(np.zeros((1, X_encoded.shape[1])), columns=X_encoded.columns)

    # Remplir les valeurs connues
    for col in athlete:
        if col in athlete_row.columns:
            athlete_row[col] = athlete[col]

    # 5. Prédiction
    prob_medal = model.predict_proba(athlete_row)[0][1]

    return prob_medal

print(predict_medal_chance(df, 25, 195, 95, "M", "Basketball", "USA"))
