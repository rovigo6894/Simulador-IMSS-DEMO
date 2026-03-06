import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image

# -------------------------
# CONFIGURACION PAGINA
# -------------------------

st.set_page_config(
    page_title="Optipension 73",
    layout="wide"
)

# -------------------------
# OCULTAR MENU STREAMLIT
# -------------------------

hide_streamlit = """
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
[data-testid="stToolbar"] {display:none;}
[data-testid="stDecoration"] {display:none;}
</style>
"""

st.markdown(hide_streamlit, unsafe_allow_html=True)

# -------------------------
# HEADER
# -------------------------

col1, col2 = st.columns([1,5])

with col1:
    logo = Image.open("image.jpg")
    st.image(logo, width=110)

with col2:
    st.title("Optipension 73")
    st.subheader("Simulador DEMO de pensión IMSS Ley 73")

st.markdown("---")

# -------------------------
# DATOS BASICOS
# -------------------------

st.header("Datos básicos")

col1, col2 = st.columns(2)

with col1:
    edad = st.number_input(
        "Edad actual",
        min_value=55,
        max_value=65,
        value=60
    )

with col2:
    salario = st.number_input(
        "Salario promedio diario (SDI)",
        min_value=200,
        max_value=2000,
        value=965
    )

# -------------------------
# BOTON
# -------------------------

calcular = st.button("Recalcular pensión")

# -------------------------
# VARIABLES INTERNAS
# -------------------------

factor_base = 0.30

# ajuste simple por edad (solo para demo)
factor_edad = 1 + ((edad - 60) * 0.04)

# -------------------------
# CALCULO
# -------------------------

if calcular:

    pension_normal = salario * 30 * factor_base

    pension_mejorada = pension_normal * factor_edad * 1.25

    diferencia = pension_mejorada - pension_normal

    perdida_20_anios = diferencia * 12 * 20

    # -------------------------
    # RESULTADOS
    # -------------------------

    st.markdown("---")

    st.header("Resultado estimado")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Pensión estimada normal",
            f"${pension_normal:,.0f} MXN"
        )

    with c2:
        st.metric(
            "Pensión optimizada",
            f"${pension_mejorada:,.0f} MXN"
        )

    with c3:
        st.metric(
            "Diferencia mensual",
            f"${diferencia:,.0f} MXN"
        )

    # -------------------------
    # IMPACTO
    # -------------------------

    st.markdown("---")

    st.subheader("Impacto financiero")

    st.metric(
        "Dinero que podría perder en 20 años",
        f"${perdida_20_anios:,.0f} MXN"
    )

    st.warning(
        "⚠️ Sin una estrategia adecuada podrías perder una cantidad importante de dinero en tu pensión."
    )

    # -------------------------
    # GRAFICA
    # -------------------------

    st.markdown("---")

    st.subheader("Comparativa de escenarios")

    labels = ["Pensión Normal", "Pensión Optimizada"]
    valores = [pension_normal, pension_mejorada]

    fig, ax = plt.subplots()

    ax.bar(labels, valores)

    ax.set_ylabel("Pensión mensual estimada")

    st.pyplot(fig)

# -------------------------
# VERSION PRO
# -------------------------

st.markdown("---")

st.header("Versión PRO")

st.markdown("""
La versión profesional de **Optipension 73** incluye:

✅ Optimización Modalidad 40  
✅ Estrategia de pensión óptima  
✅ Simulación con inflación  
✅ ROI del plan de pensión  
✅ Comparativa de múltiples escenarios  
✅ Reporte financiero completo
""")

st.link_button(
"💎 Comprar versión PRO",
"https://wa.me/528715791810?text=Hola%20quiero%20la%20version%20PRO%20de%20Optipension%2073"
)

# -------------------------
# FOOTER
# -------------------------

st.markdown("---")

st.markdown("""
<div style='text-align:center;font-size:13px;color:gray;'>

<b>Optipension 73 - Simulador DEMO</b><br><br>

Este simulador tiene fines informativos y educativos.  
Los resultados mostrados son estimaciones basadas en modelos matemáticos.<br><br>

Las pensiones reales pueden variar conforme a la legislación vigente del IMSS y condiciones individuales del asegurado.<br><br>

<b>Términos y Condiciones:</b> El uso de este simulador implica aceptación de que los cálculos son aproximaciones.<br><br>

<b>Privacidad de Datos:</b> Esta aplicación DEMO no almacena información personal.<br><br>

© 2026 <b>Ing. Roberto Villarreal Glz.</b><br>
Derechos Reservados<br>
Optipension 73

</div>
""", unsafe_allow_html=True)
