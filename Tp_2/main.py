import pandas as pd
import matplotlib.pyplot as plt

# 1. Chargement des données depuis le fichier CSV
df = pd.read_csv('Tp_2/incidents_securite.csv')

# 2. Exploration des données
print("=== Aperçu des premières lignes ===")
print(df.head())
print("\n=== Informations sur les colonnes ===")
print(df.info())
print("\n=== Statistiques descriptives ===")
print(df.describe())

# 3. Nettoyage des données (exemple : remplir les valeurs manquantes)
print("\n=== Vérification des valeurs manquantes ===")
print(df.isnull().sum())
df.fillna('Inconnu', inplace=True)  # Remplir les valeurs manquantes

# 4. Analyses
# ---------------------

# a) Nombre d'incidents par type

incidents_par_type = df['Type_Incident'].value_counts()
print("\n=== Nombre d'incidents par type ===")
print(incidents_par_type)

# b) Distribution par date

# Convertir la colonne Date en type datetime (format AAAA-MM-JJ)
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d', errors='coerce')
# Créer un regroupement par année-mois
df['AnneeMois'] = df['Date'].dt.to_period('M')
incidents_par_mois = df.groupby('AnneeMois')['Type_Incident'].count()
print("\n=== Nombre d'incidents par mois ===")
print(incidents_par_mois)

# c) Fréquence par lieu

incidents_par_lieu = df['Lieu'].value_counts()
print("\n=== Nombre d'incidents par lieu ===")
print(incidents_par_lieu)

# 5. Visualisations
# -----------------

# A. Diagramme en barres pour les types d'incidents
incidents_par_type.plot(kind='bar', title="Nombre d'incidents par type")
plt.xlabel("Type d'incident")
plt.ylabel("Nombre d'incidents")
plt.show()

# B. Évolution des incidents dans le temps (incidents par mois)
incidents_par_mois.plot(title="Évolution des incidents dans le temps")
plt.xlabel("Temps (Année-Mois)")
plt.ylabel("Nombre d'incidents")
plt.show()

