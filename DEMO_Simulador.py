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
    logo = Image.open("image.jpg")
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
# PARAMETROS BLOQUEADOS
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

st.info("🔒 Ajustes avanzados disponibles solo en versión PRO")

st.divider()

# ------------------------------------------------
# CALCULO DEMO
# ------------------------------------------------

UMA = 108.57

cuantia_basica = 13
incremento_anual = 2.45

incremento_semanas = max((semanas - 500) // 52, 0)

porcentaje_total = cuantia_basica + (incremento_anual * incremento_semanas)

pension_normal = salario * porcentaje_total * 30 / 100

# estimación optimizada (solo demostración)
pension_optimizada = pension_normal * 1.35

# ------------------------------------------------
# RESULTADOS
# ------------------------------------------------

st.subheader("Resultado estimado")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Pensión estimada sin optimización",
        f"${pension_normal:,.0f}"
    )

with col2:
    st.metric(
        "Pensión estimada optimizada",
        f"${pension_optimizada:,.0f}"
    )

# ------------------------------------------------
# PERDIDA POTENCIAL
# ------------------------------------------------

perdida_mensual = pension_optimizada - pension_normal

perdida_20_anos = perdida_mensual * 12 * 20

st.warning(
    f"⚠️ Sin optimización podrías perder aproximadamente **${perdida_20_anos:,.0f} pesos** durante tu retiro."
)

st.divider()

# ------------------------------------------------
# GRAFICA COMPARATIVA
# ------------------------------------------------

st.subheader("Comparativa de pensión")

labels = ["Pensión actual", "Pensión optimizada"]

valores = [pension_normal, pension_optimizada]

df = pd.DataFrame({
    "Escenario": labels,
    "Pensión Mensual": valores
})

fig, ax = plt.subplots()

ax.bar(df["Escenario"], df["Pensión Mensual"])

ax.set_title("Comparativa de pensión mensual")
ax.set_ylabel("Monto mensual ($)")

st.pyplot(fig)

st.caption("Optimización calculada completamente en versión PRO")

st.divider()

# ------------------------------------------------
# MODALIDAD 40 BLOQUEADA
# ------------------------------------------------

st.subheader("Simulación Modalidad 40")

st.warning("🔒 Simulación completa disponible solo en versión PRO")

st.caption("La versión PRO permite calcular impacto real de Modalidad 40, ROI y escenarios de inversión.")

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
