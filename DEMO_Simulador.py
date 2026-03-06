import streamlit as st
import pandas as pd
from datetime import datetime

# ============================================
# CONFIGURACIÓN INICIAL
# ============================================
st.set_page_config(
    page_title="OptiPensión 73 · DEMO Profesional",
    page_icon="📊",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Ocultar menús de Streamlit
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ============================================
# CSS DE LUJO
# ============================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(145deg, #f8fafc 0%, #f1f5f9 100%);
    }
    
    /* Header con logo */
    .header-logo {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 1.5rem;
        margin-bottom: 2rem;
        padding: 1rem;
        background: white;
        border-radius: 3rem;
        box-shadow: 0 10px 25px -10px rgba(0,0,0,0.1);
        border: 1px solid #e9eef3;
    }
    
    .logo-image {
        width: 80px;
        height: 80px;
        background: linear-gradient(135deg, #1e4b6a, #0f2b3d);
        border-radius: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 2rem;
        font-weight: 800;
        box-shadow: 0 10px 20px -8px #1e4b6a;
    }
    
    .logo-text {
        text-align: left;
    }
    
    .logo-text h1 {
        font-size: 2.2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #0f2b3d, #1e4b6a);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        line-height: 1.2;
    }
    
    .logo-text p {
        color: #64748b;
        font-size: 0.9rem;
        margin: 0;
        letter-spacing: 0.5px;
    }
    
    .demo-badge {
        background: linear-gradient(135deg, #f97316, #fb923c);
        color: white;
        padding: 0.3rem 1.2rem;
        border-radius: 100px;
        font-size: 0.8rem;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 1rem;
        box-shadow: 0 4px 10px -4px #f97316;
    }
    
    .main-card {
        background: rgba(255,255,255,0.95);
        backdrop-filter: blur(10px);
        border-radius: 3rem;
        padding: 2.5rem;
        box-shadow: 0 25px 50px -12px rgba(0,0,0,0.25);
        border: 1px solid rgba(255,255,255,0.5);
        margin: 1rem 0;
    }
    
    .input-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .input-card {
        background: white;
        border-radius: 1.8rem;
        padding: 1.5rem;
        box-shadow: 0 15px 30px -15px #cbd5e1;
        border: 1px solid #e9eef3;
        transition: transform 0.2s;
    }
    
    .input-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 20px 35px -15px #94a3b8;
    }
    
    .input-label {
        color: #334155;
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    .input-value {
        font-size: 2rem;
        font-weight: 700;
        color: #0f2b3d;
        line-height: 1.2;
    }
    
    .input-unit {
        font-size: 0.9rem;
        color: #94a3b8;
        font-weight: 400;
        margin-left: 0.3rem;
    }
    
    .result-card {
        background: linear-gradient(135deg, #1e4b6a, #0f2b3d);
        border-radius: 2.5rem;
        padding: 2.5rem;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 30px 40px -20px #0f2b3d;
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    .result-label {
        color: rgba(255,255,255,0.7);
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    .result-number {
        font-size: 4.5rem;
        font-weight: 800;
        color: white;
        line-height: 1;
        margin: 0.5rem 0;
        text-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }
    
    .glossary-card {
        background: white;
        border-radius: 2rem;
        padding: 1.8rem;
        margin: 2rem 0;
        border: 1px solid #e9eef3;
        box-shadow: 0 15px 30px -15px #cbd5e1;
    }
    
    .footer {
        text-align: center;
        color: #94a3b8;
        font-size: 0.8rem;
        margin-top: 3rem;
        padding-top: 2rem;
        border-top: 1px solid #e2e8f0;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #1e4b6a, #0f2b3d) !important;
        color: white !important;
        border: none !important;
        padding: 1rem 2rem !important;
        border-radius: 3rem !important;
        font-weight: 600 !important;
        font-size: 1.1rem !important;
        width: 100% !important;
        transition: all 0.3s !important;
        box-shadow: 0 10px 20px -8px #1e4b6a !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 20px 30px -10px #0f2b3d !important;
    }
    
    @media (max-width: 640px) {
        .header-logo { flex-direction: column; text-align: center; }
        .logo-text { text-align: center; }
        .input-grid { grid-template-columns: 1fr; }
        .result-number { font-size: 3rem; }
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# HEADER CON LOGO
# ============================================
st.markdown("""
<div class="header-logo">
    <div class="logo-image">73</div>
    <div class="logo-text">
        <h1>OPTIPENSIÓN 73</h1>
        <p>Optimización de Pensiones · Ley 73</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================
# CONTENEDOR PRINCIPAL
# ============================================
st.markdown('<div class="main-card">', unsafe_allow_html=True)

# ============================================
# BADGE DEMO
# ============================================
st.markdown("""
<div style="text-align: center; margin-bottom: 1rem;">
    <span class="demo-badge">⚡ VERSIÓN DEMO</span>
</div>
""", unsafe_allow_html=True)

# ============================================
# PARÁMETROS
# ============================================
st.markdown("""
<div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem;">
    <span style="background: #e9eef3; padding: 0.3rem 1rem; border-radius: 100px; font-size: 0.8rem; font-weight: 600; color: #1e4b6a;">📋 PARÁMETROS DEMOSTRATIVOS</span>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="input-card">
        <div class="input-label">📅 EDAD ACTUAL</div>
        <div class="input-value">55 <span class="input-unit">años</span></div>
        <div class="input-slider">
    """, unsafe_allow_html=True)
    edad = st.slider("", 40, 65, 55, label_visibility="collapsed")
    st.markdown('</div></div>', unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="input-card">
        <div class="input-label">🎯 EDAD DE RETIRO</div>
    """, unsafe_allow_html=True)
    retiro = st.selectbox("", [60, 61, 62, 63, 64, 65], index=0, label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="input-card">
        <div class="input-label">💰 SALARIO PROMEDIO</div>
        <div class="input-value">$20,000 <span class="input-unit">mensual</span></div>
        <div class="input-slider">
    """, unsafe_allow_html=True)
    salario = st.slider(" ", 5000, 50000, 20000, step=1000, label_visibility="collapsed")
    st.markdown('</div></div>', unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="input-card">
        <div class="input-label">📊 SEMANAS COTIZADAS</div>
        <div style="background: #f8fafc; border-radius: 1rem; padding: 1rem; text-align: center; margin-top: 0.5rem;">
            <span style="font-size: 2rem; font-weight: 700; color: #1e4b6a;">1,200</span>
            <span style="color: #94a3b8; display: block; font-size: 0.9rem;">valor fijo demo</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# BOTÓN
# ============================================
if st.button("🔮 CALCULAR PENSIÓN DEMOSTRATIVA", use_container_width=True):
    factores = {60:0.75, 61:0.80, 62:0.85, 63:0.90, 64:0.95, 65:1.00}
    pension_demo = salario * 0.5 * factores[retiro]
    
    st.markdown(f"""
    <div class="result-card">
        <div class="result-label">PENSIÓN MENSUAL ESTIMADA</div>
        <div class="result-number">${pension_demo:,.0f}</div>
        <div class="result-detail">Retiro a los {retiro} años · Cálculo demostrativo</div>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# GLOSARIO
# ============================================
st.markdown('<div class="glossary-card">', unsafe_allow_html=True)
st.markdown("""
<div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1.5rem;">
    <span style="font-size: 1.5rem;">📘</span>
    <span style="font-size: 1.2rem; font-weight: 700; color: #0f2b3d;">GLOSARIO DE TÉRMINOS</span>
</div>
""", unsafe_allow_html=True)

glosario = [
    ("Ley 73", "Régimen para quienes cotizaron antes del 1 de julio de 1997"),
    ("Factor por edad", "75% (60 años) a 100% (65 años)"),
    ("Semanas cotizadas", "Mínimo 500 semanas para pensión"),
    ("Salario promedio", "Últimas 250 semanas cotizadas"),
    ("Modalidad 40", "Continuación voluntaria"),
]

for term, definicion in glosario:
    st.markdown(f"""
    <div style="display: flex; justify-content: space-between; padding: 0.8rem 0; border-bottom: 1px solid #f1f5f9;">
        <span style="font-weight: 600; color: #1e4b6a;">{term}</span>
        <span style="color: #64748b;">{definicion}</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# OFERTA PRO
# ============================================
st.markdown("""
<div style="text-align: center; margin: 2rem 0;">
    <span style="background: #fee2e2; color: #b91c1c; padding: 0.3rem 1.2rem; border-radius: 100px; font-size: 0.8rem; font-weight: 600;">🔒 VERSIÓN COMPLETA</span>
</div>

<div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin: 1.5rem 0;">
    <div style="background: white; padding: 1rem; border-radius: 1rem; border: 1px solid #e9eef3;">✅ Cálculo con datos reales</div>
    <div style="background: white; padding: 1rem; border-radius: 1rem; border: 1px solid #e9eef3;">✅ Análisis de Modalidad 40</div>
    <div style="background: white; padding: 1rem; border-radius: 1rem; border: 1px solid #e9eef3;">✅ Comparativa 60 vs 65 años</div>
    <div style="background: white; padding: 1rem; border-radius: 1rem; border: 1px solid #e9eef3;">✅ Proyección a 20 años</div>
</div>

<div style="text-align: center; margin: 2rem 0;">
    <div style="font-size: 2rem; font-weight: 800; color: #0f2b3d;">Desde $1,500 MXN</div>
    <div style="color: #64748b;">Transferencia · Mercado Pago · OXXO</div>
</div>

<div style="display: flex; justify-content: center;">
    <a href="https://wa.me/5218715791810" target="_blank">
        <button style="background: #25D366; color: white; border: none; padding: 1rem 3rem; border-radius: 3rem; font-weight: 600; font-size: 1.1rem; cursor: pointer; box-shadow: 0 10px 20px -8px #128C7E;">
            📲 SOLICITAR INFORMACIÓN
        </button>
    </a>
</div>
""", unsafe_allow_html=True)

# ============================================
# CIERRE
# ============================================
st.markdown('</div>', unsafe_allow_html=True)

# ============================================
# FOOTER
# ============================================
st.markdown("""
<div class="footer">
    <div style="display: flex; justify-content: center; gap: 1.5rem; margin: 1rem 0;">
        <a href="#" style="color: #64748b; text-decoration: none;">Inicio</a>
        <a href="#" style="color: #64748b; text-decoration: none;">Aviso de Privacidad</a>
        <a href="#" style="color: #64748b; text-decoration: none;">Términos</a>
        <a href="#" style="color: #64748b; text-decoration: none;">Contacto</a>
    </div>
    <p>📧 contacto@optipension73.com · 📱 871 579 1810</p>
    <p>⚡ Simulación demostrativa · No constituye dictamen oficial del IMSS</p>
    <p>© 2026 · OptiPensión 73</p>
</div>
""", unsafe_allow_html=True)

st.caption(f"Última actualización: {datetime.now().strftime('%d/%m/%Y')}")
