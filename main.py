import streamlit as st
import src.support as sp

st.markdown("# Hey!")

persona = st.text_input("Enter the character from The Office you want to analyze 😀", "")

if persona != "":
    output = sp.get_character_info(persona)
    st.write(output)

else:
    st.write("necesito tu informacion")
