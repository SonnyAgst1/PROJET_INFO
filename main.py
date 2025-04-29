import pandas as pd
import matplotlib.pyplot as plt
from import_donnee_panda import importdonneepanda
import csv
from collections import defaultdict
from import_donnee_pur import importdonneespur
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

from Q1 import nbr_medailles

df_panda = importdonneepanda("donnees_jeux_olympiques/athlete_events.csv")
# Question 1 : Déterminer le nombre de médaille gagné par Micheal Phelps

print("nombre de medaille gagné par Michael Phelps : ", nbr_medailles(df_panda, "Michael Fred Phelps, II"))
total_medals = nbr_medailles(df_panda,athlete_name)
tot=sum(total_medals)
print("OR :", total_medals[0] , "ARGENT :", total_medals[1], "Bronze :", total_medals[2] )
print("Nombre de médailles gagnées au total par cet athlète est", tot)

# Question 2 : Quels sont les sports où la taille et le poids influencent le plus les performances ?
from Q2 import sport_medal_correlation

print(sport_medal_correlation(df_panda))
###

# Question 3 : Quel est le profil type d'un médaillé selon la discipline ?

from Q3panda import profil_moyen

profil_moyen(df_panda)

# Question 4 : Y a t-il une relation entre la taille d'un pays (nombre d'athlète) et son nombre de médaille


from Q4panda import plot_correlation_athletes_vs_medals

plot_correlation_athletes_vs_medals(df_panda)
