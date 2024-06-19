import streamlit as st
from taxonomy import slow, speed

# Sidebar
st.sidebar.title("Taxonomy WHATS")

# Dictionary to link page names to Taxonomy
taxonomy = {
    "Slow": slow,
    "Speed": speed,
}

# Sidebar navigation
selection = st.sidebar.radio("Go to", list(taxonomy.keys()))

# Run the selected page
pages = taxonomy[selection]
pages.app()

