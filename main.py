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
