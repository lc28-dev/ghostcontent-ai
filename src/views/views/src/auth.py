import streamlit as st

def check_password():
    """Simple démo d'auth - À lier à Supabase plus tard"""
    if "user" not in st.session_state:
        st.session_state.user = None
    return st.session_state.user is not None
