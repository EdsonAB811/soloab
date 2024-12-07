import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
import pandas as pd 
import sympy as sy

st.title("CUESTIONARIO")

st.subheader("Pregunta 1")
preg1 = st.selectbox("¿Qué representa el valor de la pendiente de una recta?", [
    "El grado de inclinación de la recta",
    "El punto de intersección de la recta con el eje x",
    "El punto de intersección de la recta con el eje y",
    "La razón de cambio de la gráfica"
])
c1 = st.empty()

st.subheader("Pregunta 2")
preg2 = st.selectbox("¿Qué es una función?", [
    "Una relación entre valores de entradas que arrojan un valor de salida",
    "Un conjunto de números que no siguen ningún patrón específico",
    "Un sistema de ecuaciones",
    "Un conjunto de operaciones entre números naturales"
])
c2 = st.empty()

st.subheader("Pregunta 3")
preg3 = st.selectbox("¿Qué es una recta tangente?", [
    "Una recta que siempre corta a la función en dos puntos",
    "Una recta paralela a la función",
    "Una recta que toca la curva de la función en un solo punto",
    "Una línea perpendicular a la función"
])
c3 = st.empty()

st.subheader("Pregunta 4")
preg4 = st.selectbox("¿Qué es una derivada?", [
    "La suma de los valores de una función en un intervalo específico",
    "Mide la razón de cambio de una función en un punto específico",
    "Una recta tangente",
    "El valor numérico de una función en un punto determinado"
])
c4 = st.empty()

st.subheader("Pregunta 5")
preg5 = st.selectbox("¿Qué es la razón de cambio en una función?", [
    "El cambio en los valores de salida respecto al cambio en los valores de entrada",
    "La cantidad de puntos donde una función alcanza su máximo o mínimo valor",
    "El valor total acumulado de una función en un intervalo específico",
    "La pendiente exacta de la recta tangente a la gráfica de una función en un punto"
])
c5 = st.empty()
puntos = 0
if st.button("Verificar Todo"):
    if preg1 == "El grado de inclinación de la recta":
        c1.success("Pregunta 1: Correcto")
        puntos += 1
    else:
        c1.error("Pregunta 1: Incorrecto")

    if preg2 == "Una relación entre valores de entradas que arrojan un valor de salida":
        c2.success("Pregunta 2: Correcto")
        puntos += 1
    else:
        c2.error("Pregunta 2: Incorrecto")

    if preg3 == "Una recta que toca la curva de la función en un solo punto":
        c3.success("Pregunta 3: Correcto")
        puntos += 1
    else:
        c3.error("Pregunta 3: Incorrecto")

    if preg4 == "Mide la razón de cambio de una función en un punto específico":
        c4.success("Pregunta 4: Correcto")
        puntos += 1
    else:
        c4.error("Pregunta 4: Incorrecto")

    if preg5 == "El cambio en los valores de salida respecto al cambio en los valores de entrada":
        c5.success("Pregunta 5: Correcto")
        puntos += 1
    else:
        c5.error("Pregunta 5: Incorrecto")
st.subheader(f"La cantidad de puntos obtenidos es de: {puntos}")






