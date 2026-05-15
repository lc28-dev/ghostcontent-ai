import streamlit as st

def show():
    st.markdown("""
        <div style='text-align: center; padding: 2rem 0;'>
            <h1 style='font-size: 3.5rem; font-weight: 800; color: #6366f1;'>GhostContent AI 👻</h1>
            <p style='font-size: 1.5rem; color: #94a3b8;'>L'IA qui gère vos réseaux sociaux pendant que vous gérez votre business.</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### ⚡️ Ultra Rapide")
        st.write("Générez 1 mois de contenu en moins de 30 secondes.")
        
    with col2:
        st.markdown("### 🎯 Ultra Précis")
        st.write("Adapté à votre secteur : resto, immo, coaching...")
        
    with col3:
        st.markdown("### 💰 Ultra Rentable")
        st.write("Le prix d'un café pour le travail d'une agence.")

    st.divider()
    
    st.subheader("Nos Tarifs")
    c1, c2 = st.columns(2)
    with c1:
        st.info("### Plan Gratuit\n- 3 générations / mois\n- Accès Dashboard\n- Support Standard")
        if st.button("Commencer gratuitement", key="free_btn"):
            st.session_state.user = {"id": "test_user", "email": "demo@example.com"} # Pour la démo
            st.rerun()
            
    with c2:
        st.success("### Plan Pro (29€/mois)\n- Générations illimitées\n- Calendrier mensuel\n- Export PDF\n- Support Prioritaire")
        st.button("Devenir Pro (Stripe)", key="pro_btn")
