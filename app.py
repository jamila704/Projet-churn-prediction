# 🎯 DASHBOARD STREAMLIT - PRÉDICTION ATTRITION CLIENT

import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# Configuration de la page
st.set_page_config(
    page_title="Prédiction d'Attrition Client",
    page_icon="📊",
    layout="wide"
)

# Titre principal
st.title("🎯 Prédiction d'Attrition Client")
st.markdown("Déterminez si un client est susceptible de quitter l'entreprise")

# Chargement du modèle
@st.cache_resource
def load_model():
    try:
        model = joblib.load("meilleur_modele_churn.pkl")
        return model
    except:
        return None

model = load_model()

# Fonction de prédiction
def predict_churn(input_features):
    try:
        input_df = pd.DataFrame([input_features])
        
        # Encodage des variables catégorielles
        categorical_cols = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'PhoneService', 
                           'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
                           'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
                           'Contract', 'PaperlessBilling', 'PaymentMethod']
        
        for col in categorical_cols:
            if col in input_df.columns:
                le = LabelEncoder()
                input_df[col] = le.fit_transform(input_df[col].astype(str))
        
        # Prédiction
        prediction = model.predict(input_df)[0]
        prediction_proba = model.predict_proba(input_df)[0]
        
        return prediction, prediction_proba[1]
    
    except Exception as e:
        return 0, 0.5

# Formulaire de saisie
st.header("📋 Informations du Client")

with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Démographie")
        gender = st.selectbox("Genre", ["Male", "Female"])
        senior_citizen = st.selectbox("Senior Citizen", ["No", "Yes"])
        partner = st.selectbox("Partenaire", ["No", "Yes"])
        dependents = st.selectbox("Personnes à charge", ["No", "Yes"])
        
    with col2:
        st.subheader("Services")
        phone_service = st.selectbox("Service téléphonique", ["No", "Yes"])
        multiple_lines = st.selectbox("Lignes multiples", ["No", "Yes", "No phone service"])
        internet_service = st.selectbox("Service Internet", ["DSL", "Fiber optic", "No"])
        online_security = st.selectbox("Sécurité en ligne", ["No", "Yes", "No internet service"])
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("Services additionnels")
        online_backup = st.selectbox("Sauvegarde en ligne", ["No", "Yes", "No internet service"])
        device_protection = st.selectbox("Protection appareil", ["No", "Yes", "No internet service"])
        tech_support = st.selectbox("Support technique", ["No", "Yes", "No internet service"])
        streaming_tv = st.selectbox("TV en streaming", ["No", "Yes", "No internet service"])
        streaming_movies = st.selectbox("Films en streaming", ["No", "Yes", "No internet service"])
    
    with col4:
        st.subheader("Facturation et contrat")
        contract = st.selectbox("Type de contrat", ["Month-to-month", "One year", "Two year"])
        paperless_billing = st.selectbox("Facturation électronique", ["No", "Yes"])
        payment_method = st.selectbox("Méthode de paiement", 
                                    ["Electronic check", "Mailed check", "Bank transfer", "Credit card"])
        tenure = st.slider("Durée de relation (mois)", 0, 72, 12)
        monthly_charges = st.number_input("Charges mensuelles ($)", 0.0, 200.0, 65.0)
        total_charges = st.number_input("Charges totales ($)", 0.0, 10000.0, 1000.0)

    submitted = st.form_submit_button("🎯 Prédire l'Attrition")

# Résultats de la prédiction
if submitted:
    if model is None:
        st.error("❌ Le modèle n'est pas disponible")
    else:
        input_features = {
            'gender': gender, 'SeniorCitizen': senior_citizen, 'Partner': partner,
            'Dependents': dependents, 'tenure': tenure, 'PhoneService': phone_service,
            'MultipleLines': multiple_lines, 'InternetService': internet_service,
            'OnlineSecurity': online_security, 'OnlineBackup': online_backup,
            'DeviceProtection': device_protection, 'TechSupport': tech_support,
            'StreamingTV': streaming_tv, 'StreamingMovies': streaming_movies,
            'Contract': contract, 'PaperlessBilling': paperless_billing,
            'PaymentMethod': payment_method, 'MonthlyCharges': monthly_charges,
            'TotalCharges': total_charges
        }
        
        prediction, probability = predict_churn(input_features)
        
        st.header("📊 Résultat de la Prédiction")
        
        # Affichage principal
        col1, col2 = st.columns([2, 1])
        
        with col1:
            if prediction == 1:
                st.error("## 🔴 **Le client va probablement PARTIR**")
                st.metric("Prédiction", "OUI", delta="Risque élevé", delta_color="inverse")
            else:
                st.success("## 🟢 **Le client va probablement RESTER**")
                st.metric("Prédiction", "NON", delta="Risque faible", delta_color="off")
        
        with col2:
            st.metric("Probabilité de départ", f"{probability:.1%}")
            confidence = min(probability, 1-probability) * 2
            st.metric("Confiance", f"{confidence:.1%}")
        
        # Visualisation
        fig, ax = plt.subplots(figsize=(8, 3))
        
        if prediction == 1:
            colors = ['lightcoral', 'lightgreen']
            labels = ['Part (OUI)', 'Reste (NON)']
            sizes = [probability, 1-probability]
        else:
            colors = ['lightgreen', 'lightcoral']
            labels = ['Reste (NON)', 'Part (OUI)']
            sizes = [1-probability, probability]
        
        wedges, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
                                         startangle=90)
        
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
        
        ax.axis('equal')
        plt.title('Répartition de la Prédiction', fontweight='bold')
        st.pyplot(fig)
        
        # Recommandations
        st.header("💡 Recommandations")
        
        if prediction == 1:
            with st.expander("🚨 Actions recommandées pour ce client à risque"):
                st.write("""
                **Actions immédiates :**
                - 📞 Contacter le client dans les 48h
                - 💰 Proposer une offre de fidélisation personnalisée
                - 🔍 Analyser les raisons du mécontentement
                - ⏰ Planifier un suivi rapproché
                
                **Stratégies de rétention :**
                - Réduction de 15% sur 6 mois
                - Amélioration du service inclus
                - Programme de parrainage avantageux
                """)
        else:
            with st.expander("✅ Actions de fidélisation recommandées"):
                st.write("""
                **Pour renforcer la fidélité :**
                - 👍 Maintenir l'excellence du service
                - 🎁 Proposer des avantages exclusifs
                - 📢 Inviter au programme de parrainage
                - ⭐ Solliciter des témoignages
                
                **Opportunités :**
                - Proposition de services additionnels
                - Programme de récompenses fidélité
                - Enquête de satisfaction
                """)

# Footer
st.markdown("---")
st.markdown("*Système de prédiction d'attrition client - Classification binaire*")