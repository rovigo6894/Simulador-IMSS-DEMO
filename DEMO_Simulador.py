import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# ------------------------------------------------
# CONFIGURACIÓN DE LA PÁGINA
# ------------------------------------------------

st.set_page_config(
    page_title="Optipensión 73",
    layout="wide"
)

# ------------------------------------------------
# HEADER CON LOGO
# ------------------------------------------------

col1, col2 = st.columns([1,6])

with col1:
    logo = Image.open("imagen.jpg")
    st.image(logo, width=90)

with col2:
    st.title("OPTIPENSIÓN 73")
    st.caption("Simulador DEMO · Optimización de Pensión IMSS Ley 73")

st.divider()

# ------------------------------------------------
# DATOS DEL USUARIO
# ------------------------------------------------

st.subheader("Datos del trabajador")

col1, col2, col3 = st.columns(3)

with col1:
    edad = st.number_input("Edad actual", 40, 65, 57)

with col2:
    semanas = st.number_input("Semanas cotizadas", 500, 2500, 1315)

with col3:
    salario = st.number_input("Salario promedio diario ($)", 100.0, 5000.0, 965.25)

edad_retiro = st.slider("Edad de retiro", 60, 65, 60)

st.divider()

# ------------------------------------------------
# CALCULO DEMO SIMPLE
# ------------------------------------------------

UMA = 108.57

veces_uma = salario / UMA

cuantia_basica = 13
incremento_anual = 2.45

incremento_semanas = max((semanas - 500) // 52, 0)

porcentaje_total = cuantia_basica + (incremento_anual * incremento_semanas)

pension_mensual = salario * porcentaje_total * 30 / 100

# ------------------------------------------------
# RESULTADO
# ------------------------------------------------

st.subheader("Resultado estimado")

st.metric(
    "Pensión mensual estimada",
    f"${pension_mensual:,.0f}"
)

st.caption("Resultado aproximado para fines demostrativos")

st.divider()

# ------------------------------------------------
# MODALIDAD 40 DEMO
# ------------------------------------------------

st.subheader("Simulación Modalidad 40 (DEMO)")

salario_m40 = st.slider(
    "Salario Modalidad 40",
    300,
    3000,
    2500
)

meses = [12,24,36,48]

resultados = []

for m in meses:

    incremento_salario = salario_m40 * (m/48)

    pension = (salario + incremento_salario) * porcentaje_total * 30 / 100

    resultados.append(pension)

df = pd.DataFrame({
    "Meses Modalidad 40": meses,
    "Pensión estimada": resultados
})

st.dataframe(df)

# ------------------------------------------------
# GRAFICA
# ------------------------------------------------

fig, ax = plt.subplots()

ax.bar(df["Meses Modalidad 40"], df["Pensión estimada"])

ax.set_title("Impacto Modalidad 40")
ax.set_xlabel("Meses")
ax.set_ylabel("Pensión mensual")

st.pyplot(fig)

st.divider()

st.info("Versión DEMO de Optipensión 73 · Para simulación profesional utilizar versión PRO")
