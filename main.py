import pandas as pd
import matplotlib.pyplot as plt
from import_donnee_panda import importdonneepanda
import csv
from collections import defaultdict
from import_donnee_pur import importdonneespur
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

from Nbr_medaille_ath import nbr_medailles

df_panda = importdonneepanda("donnees_jeux_olympiques/athlete_events.csv")
df_pur = importdonneespur("donnees_jeux_olympiques/athlete_events.csv")
# Question 1 : Déterminer le nombre de médaille gagné par Micheal Phelps

print("nombre de medaille gagné par Michael Phelps : ", nbr_medailles(df_panda, "Michael Fred Phelps, II"))


# Question 2 : Quels sont les sports où la taille et le poids influencent le plus les performances ?
from sportmedal_correlation import sport_medal_correlation

print(sport_medal_correlation(df_panda))

# Question 3 : Quel est le profil type d'un médaillé selon la discipline ?

from Profil_moyen import profil_moyen

profil_moyen(df_panda)

# Question 4 : Y a t-il une relation entre la taille d'un pays (nombre d'athlète) et son nombre de médaille


from Cor_ath_med import plot_correlation_athletes_vs_medals

plot_correlation_athletes_vs_medals(df_panda)

# Question 5 : Trouver les bornes inférieur et supérieur du nombre de médaille par nation en 2016




# Question 6 :



# Question 8 : Quel est le nombre de médailles remportées par chaque pays, en distinguant celles gagnées dans des sports collectifs de celles gagnées dans des sports individuels ?

from nbr_med_pays_co_vs_ind import graphique_medailles_par_type

print("Quel est le nombre de médailles remportées par chaque pays, en distinguant celles gagnées dans des sports collectifs de celles gagnées dans des sports individuels ?")
graphique_medailles_par_type(df_panda, top_n=10)
