import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
import pandas as pd 
import sympy as sy

fun_txt = st.text_input("$f(x)=$", value="x**2")

x_sym= sy.symbols("x")
try:
 exp = sy.parse_expr(fun_txt)

 st.latex(sy.latex(exp))
 
 derivada = sy.diff(exp, x_sym)

 func = sy.lambdify(x_sym, exp)

 st.latex(f"f'(x) = {sy.latex(derivada)}")

 x = np.linspace(-10, 10, 500)
 y = func(x)

 fig, ax = plt.subplots()
 ax.plot(x, y)
 ax.grid(True)

 st.pyplot(fig)

except:
    st.error("La expresión ingresada no es válida")