import streamlit as st

intro = st.Page("paginas/intro.py", title="Introduccion", icon=":material/description:")
ejemplos = st.Page("paginas/ejemplos.py", title="Ejemplos", icon=":material/function:")
inputs = st.Page("paginas/inputs.py", title="Inputs", icon=":material/calculate:")
cuest = st.Page("paginas/cuest.py", title="Cuestionario", icon=":material/question_answer:")
prest = st.Page("paginas/prest.py", title="Presentación", icon=":material/person:")

pg = st.navigation([intro, ejemplos, inputs, cuest, prest])

pg.run()
