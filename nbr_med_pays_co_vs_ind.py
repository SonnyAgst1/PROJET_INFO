import matplotlib.pyplot as plt
import pandas as pd

def graphique_medailles_par_type(df, top_n=10):
    """
    Affiche un graphique empilé du nombre de médailles par pays,
    en distinguant les sports individuels et collectifs.

    Paramètres :
    - df : DataFrame avec les colonnes 'Sport', 'Medal', 'Team', 'Games', 'Event'
    - top_n : nombre de pays à afficher (Top N)
    """

    sports_collectifs = [
        "Basketball", "Football", "Hockey", "Handball", "Water Polo", "Rugby Sevens",
        "Baseball", "Softball", "Volleyball", "Beach Volleyball", "Polo", "Lacrosse",
        "Tug-Of-War", "Cricket"
    ]

    # Catégoriser les sports
    df['Sport_category'] = df['Sport'].apply(
        lambda x: 'collectif' if x in sports_collectifs else 'individuel'
    )

    # Supprimer les lignes sans médaille
    df_medals = df.dropna(subset=['Medal'])

    # Supprimer les doublons (un événement par pays, jeu, sport, médaille)
    df_medals_unique = df_medals.drop_duplicates(
        subset=['Team', 'Games', 'Sport', 'Event', 'Medal']
    )

    # Groupe par pays et catégorie
    result = df_medals_unique.groupby(['Team', 'Sport_category']).size().unstack(fill_value=0)
    result['Total'] = result.sum(axis=1)
    result = result.sort_values(by='Total', ascending=False)

    # Garder les top N pays
    top_10 = result.head(top_n)

    # Tracer
    plt.figure(figsize=(14, 6))
    plt.bar(top_10.index, top_10['individuel'], label='Individuel', color='skyblue')
    plt.bar(top_10.index, top_10['collectif'], bottom=top_10['individuel'], label='Collectif', color='orange')

    plt.title(f"Médailles par pays (Top {top_n}) - Sports individuels vs collectifs")
    plt.xlabel("Pays")
    plt.ylabel("Nombre de médailles")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

df = pd.read_csv("donnees_jeux_olympiques/athlete_events.csv")
graphique_medailles_par_type(df)
