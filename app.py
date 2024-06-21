import streamlit as st
from taxonomy import accelerate, early_turn, close_proximity, diversion, emergency_services, lane_position, late_turn, overtake, route, slow, speed, stopped, uncategorised

# Sidebar
st.sidebar.title("Taxonomy WHATS")

# Dictionary to link page names to Taxonomy
taxonomy = {
    "Accelerate": accelerate,
    "Slow": slow,
    "Stopped": stopped,
    "Speed": speed,
    "Route": route,
    "Overtake": overtake,
    "Late Turn": late_turn,
    "Early Turn": early_turn,
    "Lane Position": lane_position,
    "Emergency Services": emergency_services,
    "Diversion": diversion,
    "Close Proximity": close_proximity,
    "Uncategorised": uncategorised,
}

# Sidebar navigation
selection = st.sidebar.radio("Go to", list(taxonomy.keys()))

# Run the selected page
pages = taxonomy[selection]
pages.app()

