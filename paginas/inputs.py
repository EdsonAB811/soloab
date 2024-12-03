import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
import pandas as pd 
import sympy as sy

fun_txt = st.text_input("Ingrese su función: $f(x)=$", value="x**2")
x_sym= sy.symbols("x")
punto = st.text_input("Ingrese un punto donde quiera hallar la recta tangente de la función", value="1")


try:
 
 exp = sy.parse_expr(fun_txt)

 exp_value = exp.subs(x_sym, punto)
 st.latex(sy.latex(exp))

 derivada = sy.diff(exp, x_sym)
 
 st.markdown("La derivada de la función es:")

 func = sy.lambdify(x_sym, exp)

 st.latex(f"f'(x) = {sy.latex(derivada)}")

 st.markdown(f"El valor de la función en el punto {punto} es $f(x)= {exp_value}$")

 m= derivada.subs(x_sym, punto)
 st.markdown(f"La pendiente de la recta tangente es $m = {m}$")

 st.markdown("La recta tangente es:")
 st.latex(f"y = {m}x + {exp_value}")

 st.markdown("La gráfica de la función y la recta tangente es:")


 x = np.linspace(-10, 10, 500)
 y = func(x)
 yr = m* (x - float(punto))  + exp_value

 fig, ax = plt.subplots()
 ax.plot(x, y)
 ax.plot(x, yr)
 ax.grid(True)

 st.pyplot(fig)


except:
    st.error("La expresión ingresada no es válida") 


