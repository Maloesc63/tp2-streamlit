
# TP2 STREAMLIT - VISUALISATION DE DONNEES
# ESCOLLE Malo


# ETAPE 1 : IMPORTATION DES LIBRAIRIES
import streamlit as st
import numpy as np 
import pandas as pd
import seaborn as sns
import time 
import plotly.express as px


# ETAPE 2 : CONFIGURATION DE LA PAGE
st.set_page_config(
    page_title="TP2 Streamlit",
    layout="wide"
)

st.title("Application Streamlit - Visualisation de données")

st.write("""
Cette application permet :
- de charger un fichier CSV,
- de visualiser les données,
- de créer des graphiques 2D et 3D.
""")


# ETAPE 3 : DEMANDER LE NOM DE L'UTILISATEUR
nom = st.text_input("Entrez votre prénom :")

if nom:
    st.success(f"Bonjour {nom} !")


# ETAPE 4 : CHARGEMENT DU FICHIER CSV
uploaded_file = st.file_uploader(
    "Choisissez un fichier CSV",
    type=["csv"]
)

# Vérifie si un fichier est chargé
if uploaded_file is not None:

    # Lecture du fichier CSV
    df = pd.read_csv(uploaded_file)

    st.subheader("Aperçu des données")

    st.dataframe(df)


    # ETAPE 5 : RECUPERATION DES COLONNES NUMERIQUES
    numeric_columns = df.select_dtypes(include=["number"]).columns.tolist()

    st.subheader("Colonnes numériques détectées")

    st.write(numeric_columns)

 
    # ETAPE 6 : CHOIX DU TYPE DE VISUALISATION
    graph_type = st.selectbox(
        "Choisissez le type de graphique",
        ["2D", "3D"]
    )


    # GRAPHIQUE 2D
    if graph_type == "2D":

        st.subheader("Graphique 2D")

        # Sélection des colonnes
        x_col = st.selectbox(
            "Choisissez la colonne X",
            numeric_columns
        )

        y_col = st.selectbox(
            "Choisissez la colonne Y",
            numeric_columns
        )

        # Création du graphique
        st.line_chart(df[[x_col, y_col]])


    # GRAPHIQUE 3D
    elif graph_type == "3D":

        st.subheader("Nuage de points 3D")

        # Sélection des colonnes
        x_col = st.selectbox(
            "Choisissez la colonne X",
            numeric_columns
        )

        y_col = st.selectbox(
            "Choisissez la colonne Y",
            numeric_columns
        )

        z_col = st.selectbox(
            "Choisissez la colonne Z",
            numeric_columns
        )

        # Création du scatter 3D
        fig = px.scatter_3d(
            df,
            x=x_col,
            y=y_col,
            z=z_col
        )

        st.plotly_chart(fig, use_container_width=True)

else:

    st.info("Veuillez charger un fichier CSV.")
