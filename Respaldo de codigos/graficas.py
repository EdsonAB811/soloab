import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
import pandas as pd 


#paso 1: defina x y y
st.title("Graficas")

x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
y = [0, 1, 2, 3, 4, 5, 6, 7, 8]

#crear canva

fig, ax = plt.subplots()

#graficar ejes: 
#ax.scater(x, y)
ax.plot(x, y)

#adicional:
ax.grid()

#mostrar en streamlit:
st.pyplot(fig)
st.divider()

#graficar una función
x = np.linspace(-np.pi, np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.grid()

st.pyplot(fig)

#graficar x^2
c1, c2 = st.columns([1,2], vertical_alignment="center")
with c1: 
    st.markdown("Para mostrar diferentes intervalos en la grafica de la función $f(x) = x^2 -5$ utilice el siguiente deslizador:")
    xin, xfin = st.slider("intervalo", min_value=-10, max_value=10, value=(10, 10))
    x = np.linspace(-3, 3, 100)
    y = x**2 - 5
with c2:
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.grid()
    ax.set_title("Función Cuadratica")
    ax.set_xlabel("eje x")
    ax.set_ylabel("eje y")
    st.pyplot(fig)

#graficar figuras geometricas
st.divider()
st.subheader("Figuras geometricas")
c1, c2 = st.columns([1, 3], vertical_alignment="center")
puntos = pd.DataFrame({
    "x": [1, 1, -1],
    "y": [1, -1, 0.5],
 })
with c1: 
 puntos = st.data_editor(puntos, hide_index= True, num_rows="dynamic")
pol = patches.Polygon(puntos, closed= True, fill=True, facecolor="skyblue", edgecolor="navy")

fig, ax = plt.subplots()
ax.add_patch(pol)

ax.set_xlim(puntos["x"].min()-1, puntos["x"].max()+1)
ax.set_ylim(puntos["y"].min()-1, puntos["y"].max()+1)
ax.set_aspect("equal")
with c2: 
 st.pyplot(fig)

st.divider()

