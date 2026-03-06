import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# ---------------------------------------------------------
# CONFIGURACIÓN DE PÁGINA
# ---------------------------------------------------------

st.set_page_config(
    page_title="Optipensión 73 | Simulador Ley 73",
    page_icon="https://raw.githubusercontent.com/rovigo6894/Simulador-IMSS-DEMO/main/imagen.jpg",
    layout="centered"
)

# ---------------------------------------------------------
# HEADER CON LOGO
# ---------------------------------------------------------

col1, col2 = st.columns([1,5], vertical_alignment="center")

with col1:
    st.image(
        "https://raw.githubusercontent.com/rovigo6894/Simulador-IMSS-DEMO/main/imagen.jpg",
        width=90
    )

with col2:
    st.markdown("""
    <div>
        <h1 style="color:#0f2b3d; margin:0;">OPTIPENSIÓN 73</h1>
        <p style="color:#64748b; margin:0;">
        Optimización de Pensiones · Ley 73
        </p>
    </div>
    """, unsafe_allow_html=True)

st.caption(f"Última actualización: {datetime.now().strftime('%d/%m/%Y')}")

st.divider()

# ---------------------------------------------------------
# INTRO
# ---------------------------------------------------------

st.markdown("""
### Simulador preliminar de pensión IMSS (Ley 73)

Este simulador permite estimar:

- Pensión aproximada
- Comparación con Modalidad 40
- Escenario de optimización

⚠️ **Resultados orientativos para fines educativos.**
""")

# ---------------------------------------------------------
# INPUTS
# ---------------------------------------------------------

st.subheader("Datos del trabajador")

edad = st.number_input("Edad actual", 50, 65, 57)
semanas = st.number_input("Semanas cotizadas", 500, 2000, 1300)
sdi = st.number_input("Salario Diario Promedio ($)", 200.0, 2000.0, 965.0)

uma = 113.14

# ---------------------------------------------------------
# CÁLCULOS
# ---------------------------------------------------------

salario_uma = sdi / uma

cuantia_basica = 13
incremento = 2.45 * ((semanas - 500) / 52)

porcentaje_total = cuantia_basica + incremento

pension_mensual = sdi * 30 * porcentaje_total / 100

# Escenario Modalidad 40 (estimación simple)

sdi_mod40 = sdi * 1.3
pension_mod40 = sdi_mod40 * 30 * porcentaje_total / 100

# ---------------------------------------------------------
# RESULTADOS
# ---------------------------------------------------------

st.subheader("Resultado estimado")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Pensión estimada",
        f"${pension_mensual:,.0f} MXN / mes"
    )

with col2:
    st.metric(
        "Escenario con Modalidad 40",
        f"${pension_mod40:,.0f} MXN / mes"
    )

# ---------------------------------------------------------
# GRÁFICA COMPARATIVA
# ---------------------------------------------------------

st.subheader("Comparación de escenarios")

escenarios = ["Actual", "Modalidad 40"]
valores = [pension_mensual, pension_mod40]

fig, ax = plt.subplots()

ax.bar(escenarios, valores)

ax.set_ylabel("Pensión mensual MXN")
ax.set_title("Comparación de pensión estimada")

st.pyplot(fig)

# ---------------------------------------------------------
# CTA
# ---------------------------------------------------------

st.divider()

st.markdown("""
### Diagnóstico completo Optipensión 73

Incluye:

✔ cálculo exacto Ley 73  
✔ análisis Modalidad 40  
✔ ROI de inversión  
✔ estrategia personalizada  

""")

if st.button("Solicitar diagnóstico completo"):
    st.markdown(
        "[Contactar por WhatsApp](https://wa.me/526311234567)"
    )

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.divider()

st.caption("""
Optipensión 73 · Simulador independiente

Esta herramienta no está afiliada al IMSS.  
Resultados estimados.
""")
