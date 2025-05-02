import pandas as pd
import matplotlib.pyplot as plt
from import_donnee_panda import importdonneepanda

def profil_moyen(df):

    profil_moyen_sport = df.groupby("Sport")[["Age", "Height", "Weight"]].mean()
    print("profil moyen par sport : ", profil_moyen_sport)
