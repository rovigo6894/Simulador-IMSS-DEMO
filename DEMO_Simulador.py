import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# ------------------------------------------------
# CONFIGURACION PAGINA
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

col1, col2 = st.columns(2)

with col1:
    edad = st.number_input("Edad actual", 40, 65, 57)

with col2:
    semanas = st.number_input("Semanas cotizadas", 500, 2500, 1315)

# ------------------------------------------------
# PARAMETROS BLOQUEADOS (PRO)
# ------------------------------------------------

st.divider()

st.subheader("Parámetros avanzados (versión PRO)")

salario = st.number_input(
    "Salario promedio diario ($)",
    100.0,
    5000.0,
    965.0,
    disabled=True
)

edad_retiro = st.slider(
    "Edad de retiro",
    60,
    65,
    60,
    disabled=True
)

st.info("🔒 Ajuste de salario, edad de retiro y optimización avanzada disponibles solo en versión PRO.")

st.divider()

# ------------------------------------------------
# CALCULO DEMO BASICO
# ------------------------------------------------

UMA = 108.57

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

st.caption("Resultado aproximado con fines demostrativos")

# ------------------------------------------------
# GATILLO DE PERDIDA POTENCIAL
# ------------------------------------------------

pension_optimizada = pension_mensual * 1.35
perdida = pension_optimizada - pension_mensual

st.warning(
    f"⚠️ Sin optimización de pensión podrías estar perdiendo aproximadamente **${perdida:,.0f} pesos mensuales**."
)

st.caption("La optimización completa se calcula en la versión profesional.")

st.divider()

# ------------------------------------------------
# MODALIDAD 40 BLOQUEADA
# ------------------------------------------------

st.subheader("Simulación Modalidad 40")

st.warning("🔒 Simulación completa disponible solo en versión PRO")

meses = [12, 24, 36, 48]

pensiones_demo = [
    pension_mensual * 1.1,
    pension_mensual * 1.2,
    pension_mensual * 1.3,
    pension_mensual * 1.4
]

df = pd.DataFrame({
    "Meses Modalidad 40": meses,
    "Pensión estimada": pensiones_demo
})

st.dataframe(df)

fig, ax = plt.subplots()

ax.bar(df["Meses Modalidad 40"], df["Pensión estimada"])

ax.set_title("Impacto Modalidad 40 (Vista DEMO)")
ax.set_xlabel("Meses")
ax.set_ylabel("Pensión mensual")

st.pyplot(fig)

st.caption("Datos ilustrativos · cálculo real disponible en versión PRO")

# ------------------------------------------------
# BOTON VERSION PRO
# ------------------------------------------------

st.divider()

st.subheader("🔓 Desbloquear versión profesional")

st.write(
"""
La versión **PRO de Optipensión 73** incluye:

✔ Simulación completa Ley 73  
✔ Optimización Modalidad 40  
✔ Comparativa ROI inversión vs pensión  
✔ Escenarios avanzados  
✔ Reporte profesional
"""
)

st.link_button(
"Comprar versión PRO",
"https://wa.me/528715791810?text=Hola%20quiero%20informacion%20de%20Optipension%2073%20PRO"
)

# ------------------------------------------------
# FOOTER
# ------------------------------------------------

st.divider()

st.caption(
"Optipensión 73 · Simulador DEMO | Optimización de pensiones IMSS Ley 73"
)
