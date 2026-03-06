import streamlit as st
from datetime import datetime
from calculo_demo import calcular_pension_demo, formatear_moneda, calcular_impacto
from config_demo import VERSION, EMAIL, WHATSAPP, WHATSAPP_NUMERO, SEMANAS_FIJAS, EDAD_RETIRO_FIJA

# ============================================
# CONFIGURACIÓN
# ============================================
st.set_page_config(
    page_title="Optipensión 73 DEMO",
    layout="centered"
)

# Ocultar menús (esto es seguro)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ============================================
# LOGO + TÍTULO
# ============================================
col1, col2 = st.columns([1, 5])

with col1:
    st.image("https://raw.githubusercontent.com/rovigo6894/Simulador-IMSS-DEMO/main/imagen.jpg", width=80)

with col2:
    st.title("Optipensión 73")
    st.caption("Simulador Estratégico de Pensión IMSS Ley 73")

st.divider()

# ============================================
# DATOS BÁSICOS
# ============================================
st.subheader("📋 Datos básicos")

col1, col2 = st.columns(2)

with col1:
    edad = st.number_input("Edad actual", min_value=40, max_value=65, value=57)

with col2:
    salario = st.number_input("Salario diario (SDI)", min_value=200, max_value=2000, value=965)

st.caption(f"⚡ Valores de referencia: {SEMANAS_FIJAS} semanas · Retiro a los {EDAD_RETIRO_FIJA} años")

# ============================================
# BOTÓN
# ============================================
if st.button("🔮 Recalcular simulación", use_container_width=True):
    
    pension = calcular_pension_demo(edad, salario, SEMANAS_FIJAS, EDAD_RETIRO_FIJA)
    impacto = calcular_impacto(pension)
    
    st.success(f"### Pensión estimada: {formatear_moneda(pension)}")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Pensión optimizada", formatear_moneda(impacto['optimizada']))
    with col2:
        st.metric("Diferencia mensual", formatear_moneda(impacto['diferencia']))
    with col3:
        st.metric("En 20 años", formatear_moneda(impacto['perdida_20']))

st.divider()

# ============================================
# VERSIÓN PRO
# ============================================
st.subheader("🔒 Versión PRO")

st.markdown("""
✅ **Modalidad 40** - Cálculo exacto de inversión y ROI  
✅ **Comparativa de edades** - 60 vs 65 años  
✅ **Proyección con inflación** - Valor real futuro  
✅ **Reporte PDF** - Listo para presentar  
✅ **Asesoría personalizada** - Vía WhatsApp
""")

st.link_button(
    "💎 Adquirir versión PRO",
    WHATSAPP,
    use_container_width=True
)

st.divider()

# ============================================
# FOOTER SIMPLE
# ============================================
st.markdown(f"""
<div style='text-align:center; font-size:12px; color:#666;'>

**Términos y Condiciones** · **Aviso de Privacidad** · **Legal**

📧 {EMAIL} · 📱 {WHATSAPP_NUMERO} · 📍 Torreón, Coahuila

© 2026 Optipensión 73 · Versión {VERSION} · {datetime.now().strftime('%d/%m/%Y')}

</div>
""", unsafe_allow_html=True)
