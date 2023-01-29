import streamlit as st
import src.support as sp

st.set_option('deprecation.showPyplotGlobalUse', False)

st.markdown("# Hey!")

persona = st.text_input("Enter the character from The Office you want to analyze 😀", "")

if persona != "":
    output = sp.get_character_info(persona)
    st.write(output)
    output2 = sp.proportion_lines(persona)
    st.pyplot(output2)

else:
    st.write("necesito tu informacion")
