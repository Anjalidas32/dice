import streamlit as st
import random

st.title("Dice")

roll = st.button("Roll")

if roll==True:
    result = random.randint(1,6)
    st.markdown(f"<h2>{result}<h2>",unsafe_allow_html=True) 
