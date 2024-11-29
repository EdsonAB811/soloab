import streamlit as st

st.title("Titulo de nivel 1")
st.header("Titulo de nivel 2")
st.subheader("Titulo de nivel 3")

# textos
st.markdown("""

En una etiqueta tipo markdown se puede poner cualquier texto tipo markdown.
Podemos poner un texto en negrilla **negrilla** en *italica* o en ***ambos***

esto es otra linea

enumeraciones:

1. Primer itema
2. Segundo item
3. tercer item

items:

+ item 1
+ item 2
+ item 3

podemos dar color al texto: :red[rojo], :blue[azul], :green[verde], :rainbow[arcoiris]

""")

#ecuaciones
st.latex("a^2 + b^2= c^2")



st.image("https://th.bing.com/th/id/OIP.kPLj7HLR9LX2O2rGClWmjgHaIT?rs=1&pid=ImgDetMain")
st.video("https://www.youtube.com/watch?v=eTEBvBIz8Ok")

# layout
#container

st.markdown("formula del estudiante:")
st.latex(r"x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}")

#columnas

c1, c2 = st.columns(2)

with c1: 
     st.markdown("texto en la primera columna")
     st.title("titulo")
     st.latex("f(x)= x^x")
with c2:
     st.markdown("texto en la segunda columna")
     st.image("https://th.bing.com/th/id/OIP.fjyhi67Ivh6fF0B6QnSHAQAAAA?rs=1&pid=ImgDetMain")  

# como graficar una función
#funciones

import streamlit as st

st.title("Inputs")

nombre = st.text_input("Digite su nombre")
st.markdown(f"El nombre que ingresó es: {nombre}")

edad = st.number_input("input su edad", min_value=0, max_value=100, value=18)
st.markdown(f"La edad que ingresó es: {edad}")
st.markdown(f"su edad en 10 años será: {edad + 10}")
if edad > 17:
    st.markdown("Eres mayor de edad")
else:
    st.markdown("Eres menor de edad")

rango = st.slider("digite un valor:", min_value=0, max_value=100, value=50)
st.markdown(f"El valor que ingresó es: {rango}")

ini, final = st.slider("Seleccione rangos", min_value=0, max_value=10, value=(5, 7))
st.markdown(f"El valor inicial es: {ini}")
st.markdown(f"El valor final es: {final}")



st.title("Inputs")

nombre = st.text_input("Digite su nombre")
st.markdown(f"El nombre que ingresó es: {nombre}")

edad = st.number_input("input su edad", min_value=0, max_value=100, value=18)
st.markdown(f"La edad que ingresó es: {edad}")
st.markdown(f"su edad en 10 años será: {edad + 10}")
if edad > 17:
    st.markdown("Eres mayor de edad")
else:
    st.markdown("Eres menor de edad")

rango = st.slider("digite un valor:", min_value=0, max_value=100, value=50)
st.markdown(f"El valor que ingresó es: {rango}")

ini, final = st.slider("Seleccione rangos", min_value=0, max_value=10, value=(5, 7))
st.markdown(f"El valor inicial es: {ini}")
st.markdown(f"El valor final es: {final}")

import streamlit as st

intro = st.Page("paginas/intro.py", title="Introduccion")
ejemplos = st.Page("paginas/ejemplos.py", title="Ejemplos")
textos = st.Page("paginas/textos.py", title="Textos")
inputs = st.Page("paginas/inputs.py", title="Inputs")

Pg = st.navigation([intro, ejemplos, textos, inputs])

Pg.run()

st.markdown("""
AAA
""")
