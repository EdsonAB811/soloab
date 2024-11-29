import streamlit as st

intro = st.Page("paginas/intro.py", title="Introduccion")
ejemplos = st.Page("paginas/ejemplos.py", title="Ejemplos")
inputs = st.Page("paginas/inputs.py", title="Inputs")

pg = st.navigation([intro, ejemplos, inputs])

pg.run()

st.title("Hola")