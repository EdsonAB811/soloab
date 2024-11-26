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