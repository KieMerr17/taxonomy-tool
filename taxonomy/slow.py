import streamlit as st

def app():
    st.title("Taxonomy: 'SPEED'")

    st.selectbox(
        'Please select which "WHY" examples you would like to see:',
            ('Amber Light', 
             'Stationary Vehicle'
             ))

