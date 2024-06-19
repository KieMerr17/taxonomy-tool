import streamlit as st
from taxonomy import accelerate, early_turn

# Sidebar
st.sidebar.title("Taxonomy WHATS")

# Dictionary to link page names to Taxonomy
taxonomy = {
    "Early Turn": early_turn,
    "Accelerate": accelerate,
}

# Sidebar navigation
selection = st.sidebar.radio("Go to", list(taxonomy.keys()))

# Run the selected page
pages = taxonomy[selection]
pages.app()

