import pandas as pd
from PANDAS.importation_donnees_panda import importdonneepanda
from PYTHON_pur.importation_donnees_pypur import importdonneespur
import time
import os
import matplotlib.pyplot as plt
from PANDAS.plot_correlation_athletes_vs_medals import (
    plot_correlation_athletes_vs_medals,
)
from PYTHON_pur.nb_médailles_athlete import nbr_medailles
from PANDAS.nb_medailles_athlete_pd import nbr_medailles_pd

from PANDAS.corr_taille_poids_performances import (
    corr_taille_poids_performances_pd
)
from PANDAS.Profil_moyen import profil_moyen
from PANDAS.performance_host import analyser_gain_pays_hote
from PYTHON_pur.Nbr_medaille_pays import moyenne_medailles_pur
from PANDAS.nbr_med_pays_co_vs_ind import graphique_medailles_par_type
from PYTHON_pur.agemoyentemps_pur import agemoyenathlètes
from PANDAS.prediction import (
    predict_medal_chance)
from PANDAS.borne_inf_sup_pd import analyser_jo_2016_df
from PANDAS.plot_medals_by_region_and_season import (
    plot_medals_by_region_and_season)


# creation du fichier rapport
os.makedirs("resultats", exist_ok=True)
# Écraser le contenu précédent du fichier rapport.txt
with open("resultats/rapport.txt", "w", encoding="utf-8") as f:
    f.write("RAPPORT D'ANALYSE DES DONNÉES OLYMPIQUES\n")
    f.write("=" * 50 + "\n\n")

# importation des données

df_panda = importdonneepanda(
    "PROJET_INFO/analysis/donnees_jeux_olympiques/athlete_events.csv"
)
df_pur = importdonneespur(
    "PROJET_INFO/analysis/donnees_jeux_olympiques/athlete_events.csv"
)


# ---------------------------------------------------------------------------------------------
# Question 1 : Déterminer le nombre de médaille gagné par Micheal Phelps

# Resultat Avec Python pur:
start_time = time.time()


with open("resultats/rapport.txt", "a", encoding="utf-8") as f:
    f.write(
        "Question 1 : Déterminer le nombre de médaille gagné par un athlète"
        ":l'exemple de Micheal Phelps:\n \n"
    )
    f.write("- Version 1 = Avec Pyhton pur:\n")


# Calcul du tps d'exectution

athlete = "Michael Fred Phelps, II"
medailles = nbr_medailles(df_pur, athlete)


total_medals = nbr_medailles(df_pur, athlete)

gold = total_medals.get("Gold", 0)
silver = total_medals.get("Silver", 0)
bronze = total_medals.get("Bronze", 0)
total = gold + silver + bronze


# Affichage dans le terminal
print(f"Nombre de médailles de {athlete} :")
for type_medaille, nb in medailles.items():
    print(f"  {type_medaille} : {nb}")
print("Nombre total de médailles gagnées :", total)

end_time = time.time()
execution_time = end_time - start_time

# tps d'execution du code python pur
print(f" Temps d'exécution : {execution_time:.2f} secondes")

# Rajout au rapport
with open("resultats/rapport.txt", "a", encoding="utf-8") as f:
    f.write(f" Nombre de médailles de {athlete} (Python pur) :\n")
    for type_medaille, nb in medailles.items():
        f.write(f"  {type_medaille} : {nb}\n")
    f.write(f" Nombre total de médailles gagnées : {total} \n")
    f.write(" Temps d'exécution (python pur)"
            f": {execution_time:.2f} secondes \n \n")


# --------------
# Resultat Avec Pandas:
start_time = time.time()


athlete_name = "Michael Fred Phelps, II"
total_medals = nbr_medailles_pd(df_panda, athlete_name)

gold = total_medals.get("Gold", 0)
silver = total_medals.get("Silver", 0)
bronze = total_medals.get("Bronze", 0)
total = gold + silver + bronze

print("OR :", gold, "ARGENT :", silver, "BRONZE :", bronze)
print("Nombre total de médailles gagnées :", total)


with open("resultats/rapport.txt", "a", encoding="utf-8") as f:
    f.write("- Version 2 = Avec Pandas:\n")

# Affichage dans le terminal
print(f"Nombre de médailles de {athlete} :")
for type_medaille, nb in medailles.items():
    print(f"  {type_medaille} : {nb}")
print("Nombre total de médailles gagnées :", total)

end_time = time.time()
execution_time = end_time - start_time

# tps d'execution du code python pur
print(f" Temps d'exécution : {execution_time:.2f} secondes \n \n")

# Rajout au rapport
with open("resultats/rapport.txt", "a", encoding="utf-8") as f:
    f.write(f" Nombre de médailles de {athlete} (Python pur) :\n")
    for type_medaille, nb in medailles.items():
        f.write(f"  {type_medaille} : {nb}\n")
    f.write(f" Nombre total de médailles gagnées : {total} \n")
    f.write(" Temps d'exécution (pandas) :"
            f"{execution_time:.2f} secondes \n \n")


# ---------------------------------------------------------------------------------------------------

# Question 2 : Quels sont les sports où la taille et le poids influencent
# le plus les performances ?


results = corr_taille_poids_performances_pd(df_panda)

correlations = pd.DataFrame(results).sort_values(
    by="Combined", ascending=False)
print("Sports où la taille et le poids sont les plus liés"
      "au nombre de médailles :")

print(correlations.head(10))

with open("resultats/rapport.txt", "a", encoding="utf-8") as f:
    f.write(
        "Question2: Quels sont les sports où la taille et le poids influencent"
        "le plus les performances:\n"
    )
    f.write(f"{correlations.head(10)}\n \n")

# print(correlations2.head(10))
# ----------------------------------------------------------------------------------------------------

# Question 3 : Quel est le profil type d'un médaillé selon la discipline ?


profil_type_top20_sexe = profil_moyen(df_panda)
# Affichage
print("Profil moyen des 20 athlètes les plus médaillés"
      "par sport et par sexe :")
print(profil_type_top20_sexe)
with open("resultats/rapport.txt", "a", encoding="utf-8") as f:
    f.write(
        "Question 3 : Quel est le profil type d'un médaillé"
        " selon la discipline par sexe ?: \n"
    )
    f.write(f"{profil_type_top20_sexe.head(20)}\n \n")


# -----------------------------------------------------------------------------------------------------

# Question 4 : Y a t-il une relation entre la taille d'un pays
#  (nombre d'athlète) et son nombre de médaille


print(
    " Y a t-il une relation entre la taille d'un pays (nombre d'athlète)"
    "et son nombre de médaille ?"
)
plot_correlation_athletes_vs_medals(df_panda)

with open("resultats/rapport.txt", "a", encoding="utf-8") as f:
    f.write(
        " Question 4 : Y a t-il une relation entre la taille d'un pays"
        "nombre d'athlète et son nombre de médaille \n"
    )
    f.write(
        " Le résultat est une courbe 'fichier png' présente dans "
        "le dossier 'resultats '\n \n"
    )


# ------------------------------------------------------------------------------------------------------
# Question 5 : Trouver des bornes inférieure et supérieure du nombre de
#  médailles par nation en 2016

# Resultats Avec Pandas + affichage sur results/rapport:

with open("resultats/rapport.txt", "a", encoding="utf-8") as f:
    f.write(
        "Question 5 : Trouver des bornes inférieure et supérieure du"
        "nombre de mé dailles par nation en 2016 \n \n"
    )

start_time = time.time()

with open("resultats/rapport.txt", "a", encoding="utf-8") as f:
    f.write(analyser_jo_2016_df(df_panda))
    f.write("\n\n")

end_time = time.time()
execution_time = end_time - start_time

# tps d'execution du code python pur
print(f" Temps d'exécution : {execution_time:.2f} secondes \n")




# -----------------------------------------------------------------------------------------------------
# Question 6 : Est ce que les pays hotes performent mieux que les autres ?
try:
    # Question 6 : Est ce que les pays hôtes performent mieux que les autres ?
    resultats = analyser_gain_pays_hote(df_panda)

    print("Analyse de l'impact du pays hôte sur les performances :\n")
    print(resultats)

    with open("resultats/rapport.txt", "a", encoding="utf-8") as f:
        f.write(
            "Question 6 : Influence du pays hôte sur le nombre"
            " de médailles gagnées\n"
        )
        f.write(resultats.to_string(index=False))
        f.write("\n\n")

except Exception as e:
    print("ERREUR à la question 6 :", e)
    with open("resultats/rapport.txt", "a", encoding="utf-8") as f:
        f.write("Erreur lors du traitement de la question 6 : " + str(e) + "\n\n")



# Question 7 : Moyenne du nombre de medaille gagné par pays sur
# toutes les éditions

# Resultat Avec Python pur:
start_time = time.time()
resultats = moyenne_medailles_par_pays_par_annee(df_pur)
# Enregistrement dans un fichier TXT
output_txt_path = "resultats/moyenne_medailles_par_pays.txt"
with open(output_txt_path, "w", encoding="utf-8") as txtfile:
    txtfile.write("Moyenne des médailles gagnées par pays par année\n\n")
    for pays, moyenne in resultats:
        txtfile.write(f"{pays}: {moyenne:.2f} médailles/an\n")

print(f"Les résultats ont été enregistrés dans {output_txt_path}")
with open("resultats/rapport.txt", "a", encoding="utf-8") as f:
    f.write(
        "Question 7 : Moyenne du nombre de medaille gagné par type de"
        "sport sur toutes les éditions:\n \n"
    )
    f.write("- Version 1 = Avec Pyhton pur:\n")

resultats = moyenne_medailles_par_pays_par_annee(df_pur)


# Question 8 : Quel est le nombre de médailles remportées par chaque pays, en
#  distinguant celles gagnées dans des sports collectifs de celles gagnées dans
#  des sports individuels ?

print(
    "Quel est le nombre de médailles remportées par chaque pays, en"
    "distinguant celles gagnées dans des sports collectifs de celles gagnées"
    " dans des sports individuels ?"
)
graphique_medailles_par_type(df_panda, top_n=10)


with open("resultats/rapport.txt", "a", encoding="utf-8") as f:
    f.write(
        " Question 8 : Quel est le nombre de médailles remportées par "
        "chaque pays, en"
        "distinguant celles gagnées dans des sports collectifs de celles \n"
        " gagnées dans"
        "des sports individuels ? \n \n"
    )
    f.write(
        " Le résultat est un barchart 'fichier png' présent dans "
        "le dossier 'resultats ' \n \n"
    )

# Question 9 : Evolution de l'age moyen des athlètes au cours
# du temps ( graphique )


print(
    "Question 9:Comment a évolué l'age moyen des athlètes au cours du temps ?",
    agemoyenathlètes(df_pur)
)

with open("resultats/rapport.txt", "a", encoding="utf-8") as f:
    f.write("Question 9 : Comment a évolué l'âge moyen des athlètes "
            "au cours du temps ? \n \n")
    f.write(agemoyenathlètes(df_pur))
    f.write("\n\n")

# Question 10 :
df_regions = pd.read_csv(
    "analysis/PANDAS/donnees_jeux_olympiques/noc_regions_avec_grande_region.csv")
print(
    "Question 10 :Quelles regions du monde dominent dans les sports d'hiver et "
    "quelles regions" 
    "dominent sur celles d'été ?"
    "Voir figure"
)
plot_medals_by_region_and_season(df_panda, df_regions)


with open("resultats/rapport.txt", "a", encoding="utf-8") as f:
    f.write("Question 10 :Quelles regions du monde dominent dans les sports"
    " d'hiver et quelles regions" 
            "dominent sur celles d'été ? \n\n")
    f.write("Voir figure")
    f.write("\n\n")



# ----------------------------------------------------------------------------
# -------------------------
# Question de prédiction :
# ------------------------

#  Est-il possible de prédire si un athlète gagnera
#  une médaille en fonction de caractéristique ?


age = 25
height = 195
weight = 95
sex = "M"
sport = "Basketball"
noc = "USA"


# Prédiction directe (le modèle s'entraîne une seule fois puis est réutilisé)
proba = predict_medal_chance(df_panda, age, height, weight, sex, sport, noc)

print(f"Probabilité de gagner une médaille : {proba:.2%}")

print(
    f" Probabilité qu’un athlète de {noc} en {sport} "
    f"remporte une médaille : {proba:.2%}"
)

# Sauvegarde dans le rapport
with open("resultats/rapport.txt", "a", encoding="utf-8") as f:
    f.write(" PROBLEMATIQUE :\n")
    f.write("-Question de prédiction : Peut-on prédire "
            "si un athlète va remporter"
            " une médaille en fonction de ses caractéristiques "
            "(age, poids, taille, sexe, nationalité, "
            "le sport qu'il pratique )?\n")
    f.write(
        f"→ Pour un athlète {sex}, {age} ans, {height} cm, {weight} kg, "
        f"sport : {sport}, pays : {noc} → Probabilité de médaille :"
        f"{proba:.2%}\n\n"
    )
