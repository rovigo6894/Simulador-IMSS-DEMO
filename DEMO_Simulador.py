import streamlit as st

# Configuración de página (oculta sidebar)
st.set_page_config(
    page_title="IMSS Ley 73 - Demo", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Ocultar menú de Streamlit
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Título
st.title("SIMULADOR IMSS LEY 73")
st.markdown("**Versión DEMO - Muestra gratuita**")
st.divider()

# Datos fijos
st.subheader("Datos de ejemplo (fijos)")
col1, col2 = st.columns(2)
with col1:
    st.write("Edad actual: **55 años**")
    st.write("Semanas cotizadas: **1315**")
with col2:
    st.write("Salario promedio: **$965.25**")
    st.write("Edad de retiro: **60 años**")

st.divider()

# Incremento
st.markdown("""
<div style='background-color: #00a86b; padding: 20px; border-radius: 10px; text-align: center'>
    <h2 style='color: white; margin:0'>INCREMENTO MENSUAL</h2>
    <h1 style='color: white; font-size: 48px; margin:10px'>$4,031.00</h1>
    <p style='color: white'>Tu pensión aumenta con Modalidad 40</p>
</div>
""", unsafe_allow_html=True)

# Comparativa
col_a, col_b = st.columns(2)
with col_a:
    st.markdown("### SIN Modalidad 40")
    st.markdown("## $14,522")
    st.caption("Escenario base")
with col_b:
    st.markdown("### CON Modalidad 40")
    st.markdown("## $18,553")
    st.caption("Ejemplo ilustrativo")

# Métricas
st.divider()
col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    st.metric("Inversión total", "$90,305")
with col_m2:
    st.metric("Utilidad 20 años", "$1,930,999")
with col_m3:
    st.metric("ROI", "2138%")
st.caption("*Suponiendo 240 meses de cobro")

# Versión completa
st.divider()
st.subheader("VERSIÓN COMPLETA")
puntos = [
    "✅ Tus datos reales",
    "✅ Modalidad 40 (6 a 48 meses)",
    "✅ Recuperación exacta en meses",
    "✅ Desglose técnico completo",
    "✅ Comparativa de escenarios",
    "✅ Archivo .exe listo para usar",
    "✅ Manual incluido"
]
for p in puntos:
    st.write(p)

st.markdown("## **$1,500 MXN**")
st.caption("Pago único · Sin instalaciones")

# Botón WhatsApp
whatsapp = "https://wa.me/5218715791810?text=Quiero%20la%20versi%C3%B3n%20completa"
st.markdown(f'<a href="{whatsapp}" target="_blank"><button style="background-color:#25D366; color:white; padding:15px; width:100%; border:none; border-radius:5px; font-size:18px; font-weight:bold">📲 CONTACTAR POR WHATSAPP</button></a>', unsafe_allow_html=True)

# Pie
st.divider()
st.caption("© Ing. Roberto Villarreal · Demo informativa · Versión completa: $1,500")
