import pandas as pd
import matplotlib.pyplot as plt
from import_donnee_panda import importdonneepanda
import csv
from collections import defaultdict
from import_donnee_pur import importdonneespur
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

from Nbr_medaille_ath import nbr_medailles

df_panda = importdonneepanda("analysis/donnees_jeux_olympiques/athlete_events.csv")
df_pur = importdonneespur("analysis/donnees_jeux_olympiques/athlete_events.csv")
# Question 1 : Déterminer le nombre de médaille gagné par Micheal Phelps

print("Déterminer le nombre de médaille gagné par Micheal Phelps")
print("nombre de medaille gagné par Michael Phelps : ", nbr_medailles(df_panda,"Michael Fred Phelps, II"))
medailles = nbr_medailles(df_panda,"Michael Fred Phelps, II")
with open("resultats/rapport.txt", "a", encoding="utf-8") as f:
    f.write(f"Nombre de médailles de {athlete} :\n")
    f.write(medailles.to_string())
    f.write("\n\n")


# Question 2 : Quels sont les sports où la taille et le poids influencent le plus les performances ?
from sportmedal_correlation import sport_medal_correlation

print("Quels sont les sports où la taille et le poids influencent le plus les performances ?",sport_medal_correlation(df_panda))
correlations = sport_medal_correlation(df_panda)

# Ajoute une colonne d'identification de l'analyse
correlations["Analyse"] = "Corrélation taille/poids vs médailles"

# Réorganiser les colonnes (optionnel)
cols = ["Analyse", "Sport", "Corr_Height", "Corr_Weight", "Combined"]
correlations = correlations[cols]

# Ajouter au fichier CSV global
correlations.to_csv("resultats/tableaux.csv", mode="a", index=False)


# Question 3 : Quel est le profil type d'un médaillé selon la discipline ?

from Profil_moyen import profil_moyen

print("Quel est le profil type d'un médaillé selon la discipline ?")
profil_moyen(df_panda)
result = profil_moyen(df_panda)

# Sauvegarde du résultat
result.reset_index().assign(Analyse="Profil moyen par sport").to_csv("resultats/tableaux.csv", mode="a", index=False)

# Question 4 : Y a t-il une relation entre la taille d'un pays (nombre d'athlète) et son nombre de médaille


from Cor_ath_med import plot_correlation_athletes_vs_medals

print(" Y a t-il une relation entre la taille d'un pays (nombre d'athlète) et son nombre de médaille ?")
plot_correlation_athletes_vs_medals(df_panda)
plt_obj = plot_correlation_athletes_vs_medals(df_panda)

# Enregistrer dans un fichier PNG
plt_obj.savefig("resultats/correlation_athletes_vs_medailles.png")


# Question 5 : Trouver les bornes inférieur et supérieur du nombre de médaille par nation en 2016
from borne_inf_sup import analyser_jo_par_annee
chemin = "donnees_jeux_olympiques/donnees_jeux_olympiques/athlete_events.csv"
print("Trouver les bornes inférieur et supérieur du nombre de médaille par nation en 2016 :")
analyser_jo_par_annee( chemin , 2016 )
with open("resultats/rapport.txt", "a", encoding="utf-8") as f:
    f.write(f"Résultats pour les JO de {annee} :\n")
    f.write(buffer.getvalue())
    f.write("\n")



# Question 6 :



# Question 7 : Moyenne du nombre de medaille gagné par pays sur toutes les éditions

from Nbr_medaille_pays import moyenne_medailles_par_pays_par_annee
resultats = moyenne_medailles_par_pays_par_annee(df_pur)

# Afficher les 10 premiers
print("Top 10 des pays ayant remporté le plus de médailles en moyenne par an :")
for team, moyenne in resultats[:10]:
    print(f"{team} : {moyenne:.2f} médailles/an")

# Sauvegarder dans rapport.txt
with open("resultats/rapport.txt", "a", encoding="utf-8") as f:
    f.write("Question : Quelle est la moyenne de médailles par pays sur toutes les éditions ?\n")
    for team, moyenne in resultats[:10]:
        f.write(f"{team} : {moyenne:.2f} médailles/an\n")
    f.write("\n")


# Question 8 : Quel est le nombre de médailles remportées par chaque pays, en distinguant celles gagnées dans des sports collectifs de celles gagnées dans des sports individuels ?

from nbr_med_pays_co_vs_ind import graphique_medailles_par_type

print("Quel est le nombre de médailles remportées par chaque pays, en distinguant celles gagnées dans des sports collectifs de celles gagnées dans des sports individuels ?")
graphique_medailles_par_type(df_panda, top_n=10)
plt_obje = graphique_medailles_par_type(df_panda, top_n=10)
plt_obje.savefig("resultats/correlation_athletes_vs_medailles.png")




# Question 9 : Evolution de l'age moyen des athlètes au cours du temps ( graphique )

from agemoyentemps_pur import agemoyenathlètes

print("Comment a évolué l'age moyen des athlètes au cours du temps ? ", agemoyenathlètes(df_pur))


# Question 10 :



# Question de prédiction : Est-il possible de prédire si un athlète gagnera une médaille en fonction de caractéristique ?

from prediction import (train_and_save_model, predict_medal_chance )

# Prédiction
age = 25
height = 195
weight = 95
sex = "M"
sport = "Basketball"
noc = "USA"

proba = predict_medal_chance(df, age, height, weight, sex, sport, noc)

# Affichage à l'écran
print(f"✅ Probabilité qu’un athlète de {noc} en {sport} remporte une médaille : {proba:.2%}")

# Sauvegarde dans le rapport
with open("resultats/rapport.txt", "a", encoding="utf-8") as f:
    f.write("Question : Peut-on prédire si un athlète va remporter une médaille ?\n")
    f.write(f"→ Pour un athlète {sex}, {age} ans, {height} cm, {weight} kg, "
            f"sport : {sport}, pays : {noc} → Probabilité de médaille : {proba:.2%}\n\n")
