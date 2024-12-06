import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
import pandas as pd 
import sympy as sy


st.subheader("*Razon de cambio de $f(x)= x^2$ en x = 4*")

x = np.linspace(-10, 10, 500)
y = x**2

x_sym = sy.symbols('x')
f_derivada = sy.diff(x_sym**2, x_sym)

derivada_fun = sy.lambdify(x_sym, f_derivada,)

y2 = derivada_fun(x)

st.markdown(f"La derivada de $f(x) = x^2$ es:")
st.latex(f"f'(x) = {sy.latex(f_derivada)}")

tan = derivada_fun(4)

ytan = tan*(x-4) + 4**2

fig, ax = plt.subplots()
ax.plot(x, y) 
ax.plot(x, y2) 
ax.plot(x, ytan) 
ax.grid()

st.pyplot(fig)

st.markdown("""
En el ejemplo anterior vemos lo siguiente:

- La gráfica :blue[azul] representa la función $f(x) = x^2$.
- La gráfica :orange[naranja] muestra la derivada de $f(x)$, que es $f'(x) = 2x$. La razón de cambio en este caso es 8,
 ya que evaluamos la derivada en $x = 4$, es decir, $f'(4) = 8$.
- La gráfica :green[verde] es la recta tangente a la curva en $x = 4$. La ecuación de esta tangente es $y = 8(x - 4) + 16$,
 o lo que es lo mismo, $y = 8x - 16$. Esta recta toca la curva en el punto $x = 4$, y su pendiente es igual a la razón 
 de cambio de la función en ese punto.

Por último, la razón de cambio de la derivada, es decir, la pendiente de la tangente en $x = 4$, es 8,
 ya que esta es la pendiente de la recta tangente en ese punto de la función $f(x)$.
""")

st.subheader("*Razon de cambio de $f(x)= x^3 + 3*x^2 + 2*x + 4$ en x = -3*")

x = np.linspace(-10, 10, 100)
y = x**3 + 3*x**2 + 2*x + 4

x_sym = sy.symbols('x')
f_derivada = sy.diff(x_sym**3 + 3*x_sym**2 + 2*x_sym + 4, x_sym)

derivada_fun = sy.lambdify(x_sym, f_derivada,)

y2 = derivada_fun(x)

st.markdown(f"La derivada de $f(x) = x^3 + 3x^2 + 2x + 4$ es:")
st.latex(f"f'(x) = {sy.latex(f_derivada)}")

tan = derivada_fun(-3)

f = (-3)**3 + 3*(-3)**2 + 2*(-3) + 4

ytan = tan * (x + 3) + f


 

fig, ax = plt.subplots()
ax.set_xlim(-5, 1)
ax.set_ylim(-10, 10)
ax.plot(x, y) 
ax.plot(x, y2) 
ax.plot(x, ytan) 
ax.grid()

st.pyplot(fig)

st.markdown("""
En el ejemplo anterior vemos lo siguiente:
- La gráfica :blue[azul] representa la función $f(x) = x^3 + 3x^2 + 2x + 4$
- La gráfica :orange[naranja] muestra la derivada de $f(x)$, que es $f'(x) = 3x^2 + 6x + 2$.
- La gráfica :green[verde] es la recta tangente a la curva en $x = -3$. La ecuación de esta tangente es $y = f'(-3)(x + 3) + f(-3)$,
 que corresponde a una recta con pendiente $f'(-3)$ y pasando por el punto de la función en $x = -3$.
La razón de cambio en $x = -3$ es $f'(-3) = 11$.

""")

st.subheader("Razon de cambio de la función $f(x)= sin(x)$ en x = 3")

x = np.linspace(-10, 10, 100)
y = np.sin(x)

x_sym = sy.symbols('x')
f_derivada = sy.diff(sy.sin(x_sym), x_sym)

derivada_fun = sy.lambdify(x_sym, f_derivada)

y2 = derivada_fun(x)

st.markdown(f"La derivada de $f(x) = sin(x)$ es:")
st.latex(f"f'(x) = {sy.latex(f_derivada)}")

tan = derivada_fun(3)

f = np.sin(3)

ytan = tan * (x - 3) + f

fig, ax = plt.subplots()
ax.plot(x, y) 
ax.plot(x, y2) 
ax.plot(x, ytan) 
ax.grid()

st.pyplot(fig)

st.markdown("""
En el ejemplo anterior vemos lo siguiente:
- La gráfica :blue[azul] representa la función $f(x) = sin(x)$
- La gráfica :orange[naranja] muestra la derivada de $f(x)$, que es $f'(x) = cos(x)$.
- la grafica :green[verde] es la recta tangente a la curva en $x = 3$.
- la razon de cambio en $x = 3$ es $f'(3) = cos(3) = -0.909$.


""")
