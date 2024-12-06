import streamlit as st

intro = st.Page("paginas/intro.py", title="Introduccion", icon=":material/description:")
ejemplos = st.Page("paginas/ejemplos.py", title="Ejemplos", icon=":material/function:")
inputs = st.Page("paginas/inputs.py", title="Inputs", icon=":material/calculate:")

pg = st.navigation([intro, ejemplos, inputs])

pg.run()
