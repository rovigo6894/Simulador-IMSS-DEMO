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

# Ocultar menús de Streamlit (básico)
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ============================================
# CSS PROFESIONAL (FONDO ELEGANTE)
# ============================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(145deg, #f8fafc 0%, #f1f5f9 100%);
    }
    
    /* Footer profesional */
    .footer {
        text-align: center;
        color: #64748b;
        font-size: 0.8rem;
        margin-top: 3rem;
        padding-top: 2rem;
        border-top: 1px solid #e2e8f0;
    }
    
    .footer a {
        color: #64748b;
        text-decoration: none;
    }
    
    .footer a:hover {
        color: #1e4b6a;
    }
    
    /* Tarjetas de métricas */
    div[data-testid="metric-container"] {
        background: white;
        border-radius: 1rem;
        padding: 1rem;
        box-shadow: 0 4px 12px -6px #cbd5e1;
        border: 1px solid #e9eef3;
    }
    
    /* Badge PRO */
    .pro-badge {
        background: linear-gradient(135deg, #f97316, #fb923c);
        color: white;
        padding: 0.2rem 1rem;
        border-radius: 2rem;
        font-size: 0.7rem;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 0.5rem;
    }
    
    /* Botón PRO */
    .stLinkButton > button {
        background: linear-gradient(135deg, #f97316, #fb923c) !important;
        color: white !important;
        border: none !important;
        border-radius: 2rem !important;
        font-weight: 600 !important;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# LOGO + TÍTULO
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
# BOTÓN Y RESULTADOS
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
st.markdown("""
<div style='text-align: center;'>
    <span class="pro-badge">🔒 VERSIÓN PRO</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style='background: white; border-radius: 1rem; padding: 1.5rem; border: 1px solid #e9eef3; margin: 1rem 0;'>
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
