import streamlit as st

st.set_page_config(
    page_title="TeaterSkiftNyckeln",
    page_icon="🎭",
    layout="wide"
)

st.title("🎭 TeaterSkiftNyckeln (TSN)")
st.write("Välkommen till din nya arbetsmiljö! Här bygger vi verktygen för att optimera Riksteaterns lokalföreningssida")

# Enkel testknapp för att se att det funkar
if st.button("Klicka för att testa agenten"):
    st.success("Systemet är igång och redo för utveckling!")
