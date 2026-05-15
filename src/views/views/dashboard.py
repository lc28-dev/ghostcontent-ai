import streamlit as st
from src.ai_engine import generate_social_bundle
import json

def show():
    st.title("🚀 Générateur de Contenu")
    
    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            biz_name = st.text_input("Nom de votre Business", placeholder="Ex: Café de Paris")
            industry = st.selectbox("Secteur", ["Restauration", "Immobilier", "Beauté", "Sport", "Technologie"])
        with col2:
            tone = st.selectbox("Ton de marque", ["Professionnel", "Amical/Fun", "Luxueux", "Énergique"])
            goal = st.selectbox("Objectif", ["Plus de clients", "Plus de vues", "Vendre un produit"])

    if st.button("✨ Générer mon pack GhostContent", type="primary"):
        with st.spinner("L'IA Ghost rédige vos posts..."):
            # Appel à l'IA
            result = generate_social_bundle(biz_name, industry, tone, goal)
            data = json.loads(result)
            
            st.balloons()
            
            # Affichage des résultats
            st.success("Contenu prêt !")
            
            tab1, tab2, tab3 = st.tabs(["📱 Posts Instagram", "🎬 Scripts Reels", "📅 Calendrier"])
            
            with tab1:
                for post in data.get("posts", []):
                    st.subheader(post.get("hook", "Post"))
                    st.write(post.get("caption", ""))
                    st.caption(f"Hashtags: {data.get('hashtags', '')}")
                    st.divider()
            
            with tab2:
                for script in data.get("scripts", []):
                    st.code(script, language="markdown")
            
            with tab3:
                st.table(data.get("calendar", []))
