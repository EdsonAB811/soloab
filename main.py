import streamlit as st

intro = st.Page("paginas/intro.py", title="Introduccion")
ejemplos = st.Page("paginas/ejemplos.py", title="Ejemplos")
textos = st.Page("paginas/textos.py", title="Textos")
inputs = st.Page("paginas/inputs.py", title="Inputs")

Pg = st.navigation([intro, ejemplos, textos, inputs])

Pg.run()
