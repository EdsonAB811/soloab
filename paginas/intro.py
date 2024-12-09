import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
import pandas as pd 
import sympy as sy


st.title("RAZONES DE CAMBIO EN LAS DERIVADAS")

c1, c2 = st.columns([1,2], vertical_alignment="center")
with c1:
      st.header("*¿Que es una derivada?*")
      st.markdown(""" 
      Para entender el concepto de derivadas, primero se deben tener en cuenta varias cosas, como:
      ¿Que es una función? Pues en el área de las matemáticas, una función se puede definir en resumidas
      palabras como una cuenta que se hace con variables de entrada (X) que a su vez devuelve variables de salida (Y).
      Existen varios tipos de funciones y estas se pueden graficar en un plano cartesiano:
      """)
with c2:
       st.image("https://quizizz.com/media/resource/gs/quizizz-media/quizzes/b508ffdc-f5f6-4a7b-a728-2583164e26d8?w=900&h=900.png", width=350)

c1, c2 = st.columns([1,2], vertical_alignment="center")

with c1: 
      st.subheader("*¿Que es una pendiente de una recta?*")
      st.markdown("""La pendiente es un parametro de una recta con respecto al eje de las x que mide su grado
      de inclinación, existen varios tipos de pendiente y su valor siempre es un número real:

      """)

with c2:
      st.image("https://www.geogebra.org/resource/zwBVEs4v/rWdwyFgd2igIfcEA/material-zwBVEs4v.png")

c1, c2 = st.columns([1,2], vertical_alignment="center")
with c1:
      st.subheader("*¿Que es una recta tangente?*")
      st.markdown(""" 
      La recta tangengete se puede resumir en pocas palabras como una recta en el plano que toca en un solo
      punto una curva de una función:


      """)
with c2:
      st.image("https://www.fisicalab.com/sites/all/files/contenidos/matematicas/2422_tangente_normal/rectas_tangente_normal.jpg")

st.markdown("""Ahora, conociendo esto podemos decir que la derivada de una función describe la razón de cambio 
instantáneo de la función en un cierto punto. ¿Y que tiene que ver la recta tangente? pues que La recta tangente es, 
a su vez, la gráfica de la mejor aproximación lineal de la función alrededor de dicho punto.

Para explicarlo mejor imaginate que te dan un grupo de datos en una tabla sobre un automovil que viajó durante 
ocho horas de un punto a otro a diferentes velocidades y que la función que describe la relación entre el tiempo que viajó (X)
y las velocidades que tuvo durante ese tiempo (Y) está representada por: 


""")

st.latex(r"f(x) = \sqrt{x}")

st.markdown("""
La derivada de esta función, \(f'(x)\), nos permite conocer cómo cambia la velocidad (Y) con respecto al tiempo (X) 
en cualquier instante. Matemáticamente, la derivada de \(f(x)\) es:
""")

st.latex(r"f'(x) = \frac{1}{2\sqrt{x}}")

st.markdown(""" 
Entonces, para hallar la razón de cambio de la función en una hora específica, solo necesitamos reemplazar 
X, razón de cambio en el tiempo x=4 en la función: 
""")

c1, c2, c3 = st.columns(3)
with c1:
      st.latex(r"f'(x) = \frac{1}{2\sqrt{x}}")
with c2: 
      st.latex(r"f'(x) = \frac{1}{2\sqrt{4}}")
with c3: 
      st.latex(r"f'(x) = \frac{1}{4}")

st.markdown("""Lo segundo a hacer es hallar la recta tangente a la función en el punto x = 4, para ello se emplea la formula: $y-y1 = x(x-x1)$
donde y1 y x1 son las coordenadas del punto, x la variable independiente y Y es la función evaluada en el punto x. Reemplazando en la formula y despejando 
nos quedaría así: 

""")

st.latex(r"y = \frac{1}{4}x + 1")


st.markdown("La función se vería así con la recta tangente, luego de evaluar la función en el punto x = 4:")

x = np.linspace(0, 8, 100)
y = np.sqrt(x)
y2 = (1/4)*x + 1


fig, ax = plt.subplots()
ax.plot(x, y)
ax.plot(x, y2)
ax.set_xlabel("Tiempo (X)")
ax.set_ylabel("Velocidad (Y)")
ax.grid()

st.pyplot(fig)

st.markdown("""La derivada mide cómo cambia una variable dependiente (Y) respecto a una variable
independientemente (X) en un punto especifico. Es entonces, la pendiente de la recta tangente a la 
grafica en la función en ese punto.

En el ejemplo anterior describe cómo varía la velocidad de un automóvil con el tiempo, la derivada 
nos dice cuánto cambia la velocidad en un instante. Además, nos ayuda a aproximar el comportamiento 
de la función con una línea recta cercana, llamada recta tangente. que a su vez es, matematicamente, 
el valor de la derivada en un punto. Y su razón de cambio es 1/4 ya que es valor que nos da cuando evaluamos en la derivada
de la función.

""")
st.divider()

st.header("*¿Como se solucionan las derivadas?*")

st.markdown(""" Existen dos metodos para hallar la derivada de una función, el primero es usando la formula general
de la derivada: 

""")

st.latex(r"f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}")

st.markdown("""La otra forma de resolverla es reconociendo el tipo de función que tengo y usando la formula de la 
derivada de dicha función:

""")

st.image("https://www.funciones.xyz/wp-content/uploads/2021/10/tabla-derivadas-inmediatas-formulas-1024x942.png")