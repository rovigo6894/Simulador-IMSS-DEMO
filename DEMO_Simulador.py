import streamlit as st
from datetime import datetime
from calculo_demo import calcular_pension_demo, formatear_moneda, calcular_impacto
from config_demo import VERSION, EMAIL, WHATSAPP, WHATSAPP_NUMERO, SEMANAS_FIJAS, EDAD_RETIRO_FIJA

# ============================================
# CONFIGURACIÓN
# ============================================
st.set_page_config(
    page_title="Optipensión 73 · DEMO",
    page_icon="📊",
    layout="centered"
)

# Ocultar menús
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ============================================
# CSS MÁXIMO CONTRASTE
# ============================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Fondo blanco puro - máximo contraste */
    .stApp {
        background: white !important;
    }
    
    /* Todo el texto en negro */
    h1, h2, h3, h4, h5, h6, p, li, span, div {
        color: #000000 !important;
    }
    
    /* Inputs con borde negro */
    .stNumberInput input, .stSelectbox select {
        border: 2px solid #000000 !important;
        color: #000000 !important;
        background: white !important;
    }
    
    /* Labels en negro */
    .stNumberInput label, .stSelectbox label {
        color: #000000 !important;
        font-weight: 600 !important;
    }
    
    /* Botón principal - azul oscuro con texto blanco */
    .stButton > button {
        background: #1e4b6a !important;
        color: white !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        border: 2px solid #000000 !important;
    }
    
    /* Métricas con borde negro */
    div[data-testid="metric-container"] {
        background: #f8fafc !important;
        border: 2px solid #000000 !important;
        border-radius: 0.5rem !important;
        padding: 1rem !important;
    }
    
    div[data-testid="metric-container"] label {
        color: #000000 !important;
        font-weight: 600 !important;
    }
    
    div[data-testid="metric-container"] div {
        color: #000000 !important;
        font-weight: 700 !important;
        font-size: 1.3rem !important;
    }
    
    /* Badge PRO - naranja con texto blanco */
    .pro-badge {
        background: #f97316 !important;
        color: white !important;
        padding: 0.2rem 1rem;
        border-radius: 2rem;
        font-weight: 700;
        border: 2px solid #000000;
    }
    
    /* Footer con texto negro */
    .footer {
        text-align: center;
        color: #000000 !important;
        font-size: 0.8rem;
        margin-top: 3rem;
        padding-top: 2rem;
        border-top: 2px solid #000000;
    }
    
    .footer a {
        color: #000000 !important;
        text-decoration: underline;
        font-weight: 500;
    }
    
    /* Caption en negro */
    .stCaption {
        color: #000000 !important;
    }
    
    /* Línea divisora negra */
    hr {
        border: 1px solid #000000 !important;
    }
</style>
""", unsafe_allow_html=True)

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
# BOTÓN Y RESULTADOS
# ============================================
if st.button("🔮 Recalcular simulación", use_container_width=True):
    
    pension = calcular_pension_demo(edad, salario, SEMANAS_FIJAS, EDAD_RETIRO_FIJA)
    impacto = calcular_impacto(pension)
    
    st.markdown(f"### Pensión estimada: {formatear_moneda(pension)}")
    
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
st.markdown("""
<div style='text-align: center;'>
    <span class="pro-badge">🔒 VERSIÓN PRO</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style='background: #f8fafc; border: 2px solid #000000; border-radius: 0.5rem; padding: 1.5rem; margin: 1rem 0;'>
    <p>✅ <strong>Modalidad 40</strong> - Cálculo exacto de inversión y ROI</p>
    <p>✅ <strong>Comparativa de edades</strong> - 60 vs 65 años</p>
    <p>✅ <strong>Proyección con inflación</strong> - Valor real futuro</p>
    <p>✅ <strong>Reporte PDF</strong> - Listo para presentar</p>
    <p>✅ <strong>Asesoría personalizada</strong> - Vía WhatsApp</p>
</div>
""", unsafe_allow_html=True)

st.link_button(
    "💎 Adquirir versión PRO",
    WHATSAPP,
    use_container_width=True
)

st.divider()

# ============================================
# FOOTER PROFESIONAL
# ============================================
st.markdown(f"""
<div class="footer">
    <div style="display: flex; justify-content: center; gap: 1.5rem; margin-bottom: 1rem;">
        <a href="#">Términos y Condiciones</a>
        <a href="#">Aviso de Privacidad</a>
        <a href="#">Legal</a>
    </div>
    <p>📧 {EMAIL} · 📱 {WHATSAPP_NUMERO} · 📍 Torreón, Coahuila</p>
    <p>© 2026 Optipensión 73 · Versión {VERSION}</p>
    <p style="font-size:0.7rem;">Última actualización: {datetime.now().strftime('%d/%m/%Y')}</p>
</div>
""", unsafe_allow_html=True)
