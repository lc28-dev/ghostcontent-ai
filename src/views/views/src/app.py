import streamlit as st
from views import landing, dashboard, history, settings

# Configuration de la page
st.set_page_config(page_title="GhostContent AI", page_icon="👻", layout="wide")

# Menu de navigation (Simulé pour le moment)
if "user" not in st.session_state:
    st.session_state.user = None

def main():
    if st.session_state.user:
        # Sidebar pour les utilisateurs connectés
        st.sidebar.title("👻 GhostContent")
        page = st.sidebar.radio("Navigation", ["Dashboard", "Historique", "Paramètres", "Déconnexion"])
        
        if page == "Dashboard":
            dashboard.show()
        elif page == "Historique":
            history.show()
        elif page == "Paramètres":
            settings.show()
        elif page == "Déconnexion":
            st.session_state.user = None
            st.rerun()
    else:
        # Afficher la Landing Page si pas connecté
        landing.show()

if __name__ == "__main__":
    main()
