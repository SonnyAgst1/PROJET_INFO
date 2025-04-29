def nbr_medailles(athlete_name):
    athlete_df = df[df["Name"] == athlete_name]
    medaille_count = athlete_df["Medal"].value_counts()
    return medaille_count


# le nom de l'athlète
athlete_name = "Michael Fred Phelps, II"

total_medals = nbr_medailles(athlete_name)
tot=sum(total_medals)
print("OR :", total_medals[0] , "ARGENT :", total_medals[1], "Bronze :", total_medals[2] )
print("Nombre de médailles gagnées au total par cet athlète est", tot)