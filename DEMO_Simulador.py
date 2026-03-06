import streamlit as st
from calculo_demo import calcular_pension_demo
from config_demo import PRO_FEATURES, WHATSAPP_LINK

st.set_page_config(page_title="Optipension 73 DEMO", layout="centered")

# LOGO + TITULO
col1, col2 = st.columns([1,5])

with col1:
    st.image("assets/logo.png", width=80)

with col2:
    st.title("Optipension 73")
    st.subheader("Simulador Estratégico de Pensión IMSS Ley 73")

st.markdown("---")

st.write("Versión DEMO")

# INPUTS BASICOS
edad = st.number_input("Edad actual", min_value=40, max_value=65, value=57)

salario = st.number_input(
    "Salario diario aproximado",
    min_value=200,
    max_value=3000,
    value=965
)

if st.button("Recalcular simulación"):

    pension, optimizada, diferencia, perdida = calcular_pension_demo(salario)

    st.markdown("### Resultado estimado")

    st.metric("Pensión estimada", f"${pension:,.0f} MXN")

    st.metric("Pensión optimizada posible", f"${optimizada:,.0f} MXN")

    st.metric("Diferencia mensual", f"${diferencia:,.0f} MXN")

    st.warning(f"En 20 años podrías perder aproximadamente ${perdida:,.0f} MXN")

st.markdown("---")

# FUNCIONES BLOQUEADAS
st.markdown("### Funciones avanzadas")

st.info("Disponible solo en la versión PRO:")

st.write("✔ Modalidad 40 optimizada")
st.write("✔ Cálculo real Ley 73")
st.write("✔ ROI de inversión")
st.write("✔ Proyección a 30 años")
st.write("✔ Exportar reporte PDF")

# BOTON WHATSAPP
st.link_button("Comprar versión PRO", WHATSAPP_LINK)

st.markdown("---")

# FOOTER
st.markdown(
"""
© 2026 Ing. Roberto Villarreal Glz.  
Todos los derechos reservados  

Optipension 73 es un simulador informativo.
"""
)
