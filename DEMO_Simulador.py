import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image

# -------------------------
# CONFIGURACION DE PAGINA
# -------------------------

st.set_page_config(
    page_title="Optipension 73",
    layout="wide"
)

# -------------------------
# OCULTAR MENU STREAMLIT
# -------------------------

hide_streamlit_style = """
<style>

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
[data-testid="stToolbar"] {display:none;}
[data-testid="stDecoration"] {display:none;}
[data-testid="stStatusWidget"] {display:none;}

</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# -------------------------
# HEADER CON LOGO
# -------------------------

col1, col2 = st.columns([1,5])

with col1:
    logo = Image.open("image.jpg")
    st.image(logo, width=120)

with col2:
    st.title("Optipension 73")
    st.subheader("Simulador DEMO de pensión IMSS Ley 73")

st.markdown("---")

# -------------------------
# PARAMETROS DEMO
# -------------------------

st.sidebar.header("Parámetros básicos")

edad = st.sidebar.slider(
    "Edad actual",
    55,
    65,
    60
)

semanas = st.sidebar.slider(
    "Semanas cotizadas",
    500,
    2000,
    1300
)

st.sidebar.markdown("🔒 Otros parámetros disponibles en versión PRO")

# -------------------------
# SIMULACION DEMO SIMPLE
# -------------------------

pension_normal = semanas * 10
pension_mejorada = pension_normal * 1.35

# -------------------------
# CALCULOS ADICIONALES
# -------------------------

diferencia = pension_mejorada - pension_normal

perdida_20_anios = diferencia * 12 * 20

# -------------------------
# RESULTADOS
# -------------------------

st.header("Resultado estimado")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Pensión estimada normal",
        f"${pension_normal:,.0f} MXN"
    )

with col2:
    st.metric(
        "Pensión optimizada",
        f"${pension_mejorada:,.0f} MXN"
    )

with col3:
    st.metric(
        "Diferencia mensual",
        f"${diferencia:,.0f} MXN"
    )

st.markdown("---")

st.subheader("Impacto financiero")

st.metric(
    "Dinero que podría perder en 20 años si no optimiza su pensión",
    f"${perdida_20_anios:,.0f} MXN"
)

st.warning(
"⚠️ Sin una estrategia adecuada podrías perder una cantidad importante de dinero en tu pensión."
)

# -------------------------
# GRAFICA COMPARATIVA
# -------------------------

st.markdown("---")

st.subheader("Comparativa de escenarios")

labels = ["Normal", "Optimizada"]
valores = [pension_normal, pension_mejorada]

fig, ax = plt.subplots()

ax.bar(labels, valores)

ax.set_ylabel("Pensión mensual estimada")

st.pyplot(fig)

# -------------------------
# BLOQUE VERSION PRO
# -------------------------

st.markdown("---")

st.markdown("""
### 🔒 Versión PRO disponible

La versión profesional de **Optipension 73** incluye:

✅ Optimización avanzada de pensión  
✅ Estrategia Modalidad 40  
✅ Simulación con inflación anual  
✅ Análisis ROI del plan de pensión  
✅ Comparativa de múltiples escenarios  
✅ Reporte financiero completo
""")

st.link_button(
"💎 Comprar versión PRO",
"https://wa.me/528715791810?text=Hola%20quiero%20la%20version%20PRO%20de%20Optipension%2073"
)

# -------------------------
# PIE DE PAGINA
# -------------------------

st.markdown("---")

st.markdown("""
<div style='text-align: center; font-size: 13px; color: gray;'>

<b>Optipension 73 - Simulador DEMO</b><br><br>

Este simulador tiene fines exclusivamente informativos y educativos.  
Los resultados mostrados son estimaciones basadas en modelos matemáticos y no constituyen asesoría financiera, legal o previsional.<br><br>

Las pensiones reales pueden variar conforme a la legislación vigente del IMSS, reformas futuras y condiciones individuales del asegurado.<br><br>

<b>Términos y Condiciones:</b> El uso de este simulador implica la aceptación de que los cálculos presentados son aproximaciones y no garantizan resultados finales.<br><br>

<b>Privacidad de Datos:</b> Esta aplicación DEMO no almacena información personal. Los datos ingresados se utilizan únicamente para generar cálculos temporales.<br><br>

© 2026 <b>Ing. Roberto Villarreal Glz.</b><br>
Derechos Reservados.<br>
Propiedad intelectual del simulador <b>Optipension 73</b>.

</div>
""", unsafe_allow_html=True)
