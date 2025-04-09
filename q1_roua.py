import pandas as pd

df = pd.read_csv("donnees_jeux_olympiques/donnees_jeux_olympiques/athlete_events.csv")
print(df.head())


def nbr_medailles(athlete_name):
    athlete_df = df[df["Name"] == athlete_name]
    medaille_count = athlete_df["Medal"].value_counts()
    return medaille_count


# le nom de l'athlète
athlete_name = "Michael Fred Phelps, II"

total_medals = nbr_medailles(athlete_name)
print(total_medals)
