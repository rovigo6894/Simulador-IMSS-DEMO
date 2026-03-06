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

# ============================================
# OCULTAR TODO DE STREAMLIT (también la derecha)
# ============================================
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            
            /* Ocultar elementos de la derecha */
            .stApp header {display: none !important;}
            .stApp [data-testid="stToolbar"] {display: none !important;}
            .stApp [data-testid="stDecoration"] {display: none !important;}
            .stApp [data-testid="baseButton-header"] {display: none !important;}
            .stApp [aria-label="Menu"] {display: none !important;}
            
            /* Forzar que todo el espacio sea para la app */
            .main .block-container {
                padding-top: 2rem !important;
                max-width: 800px !important;
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ============================================
# TÍTULO Y LOGO
# ============================================
col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://raw.githubusercontent.com/rovigo6894/Simulador-IMSS-DEMO/main/image.jpg", width=80)
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
# BOTÓN PRINCIPAL
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
# VERSIÓN PRO (SIN PRECIOS)
# ============================================
st.subheader("🔒 Versión Profesional")

st.markdown("""
La versión profesional incluye:

✅ **Diagnóstico personalizado** con tus datos reales  
✅ **Modalidad 40** - Cálculo exacto de inversión y ROI  
✅ **Comparativa de edades** - 60 vs 61...65 años  
✅ **Proyección a 20 años** con ajuste inflacionario  
✅ **Reporte PDF** listo para presentar  
✅ **Asesoría personalizada** vía WhatsApp
""")

st.link_button(
    "📲 CONTACTAR PARA VERSIÓN PRO",
    "https://wa.me/528715791810?text=Hola%2C%20quiero%20información%20sobre%20la%20versión%20PRO%20de%20Optipensión%2073",
    use_container_width=True
)
""", unsafe_allow_html=True)
