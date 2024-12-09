import streamlit as st 

st.title("PRESENTACIÓN")

st.markdown("""
    - Trabajo realizado por: Edson Estiven Niño Barbosa
    - Intereses: Fútbol, física, literatura, y los gatos.
    - Área de la matemática favorita: Álgebra lineal (Específicamente SEl)
    - ¿Qué aprendizaje me dejó la materia de programación 1?: Aprendí a brindar soluciones de manera lógica y estructurada a problemas matemáticos mediante el uso de códigos de programación en Python.
    """)


button_pressed = st.button("Lo que más quiero:")
if button_pressed:
        st.image(
            "https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Escudo_Atletico_Bucaramanga_Campe%C3%B3n_2024_I.png/180px-Escudo_Atletico_Bucaramanga_Campe%C3%B3n_2024_I.png", 
            width=250
        )