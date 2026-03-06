import streamlit as st
from datetime import datetime
from calculo_demo import calcular_pension_demo, formatear_moneda, calcular_impacto
from config_demo import VERSION, EMAIL, WHATSAPP, WHATSAPP_NUMERO, SEMANAS_FIJAS, EDAD_RETIRO_FIJA

# ============================================
# CONFIGURACIÓN
# ============================================
st.set_page_config(
    page_title="Optipensión 73 · DEMO Profesional",
    page_icon="📊",
    layout="centered"
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
# CSS PROFESIONAL
# ============================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
    }
    
    /* Tarjetas de métricas */
    div[data-testid="metric-container"] {
        background: white;
        border-radius: 1.5rem;
        padding: 1.2rem;
        box-shadow: 0 10px 25px -10px rgba(0,0,0,0.1);
        border: 1px solid #e9eef3;
        transition: transform 0.2s;
    }
    
    div[data-testid="metric-container"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 15px 30px -12px rgba(0,0,0,0.15);
    }
    
    /* Tarjeta de pensión */
    .result-card {
        background: linear-gradient(135deg, #1e4b6a, #0f2b3d);
        border-radius: 2rem;
        padding: 2rem;
        text-align: center;
        margin: 1.5rem 0;
        box-shadow: 0 20px 30px -15px #0f2b3d;
    }
    
    .result-label {
        color: rgba(255,255,255,0.7);
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .result-number {
        color: white;
        font-size: 3.5rem;
        font-weight: 700;
        line-height: 1.2;
        margin: 0.5rem 0;
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
        margin-left: 0.5rem;
    }
    
    /* Separador elegante */
    .divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, #cbd5e1, transparent);
        margin: 2rem 0;
    }
    
    /* Footer */
    .footer-text {
        text-align: center;
        color: #94a3b8;
        font-size: 0.75rem;
        line-height: 1.6;
    }
    
    .footer-text a {
        color: #64748b;
        text-decoration: none;
    }
    
    .footer-text a:hover {
        color: #1e4b6a;
    }
    
    /* Botón PRO */
    .stButton > button {
        background: linear-gradient(135deg, #f97316, #fb923c) !important;
        color: white !important;
        border: none !important;
        border-radius: 2rem !important;
        padding: 0.8rem 2rem !important;
        font-weight: 600 !important;
        transition: all 0.3s !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px -8px #f97316 !important;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# LOGO + TÍTULO
# ============================================
col1, col2 = st.columns([1, 5])

with col1:
    st.image("https://raw.githubusercontent.com/rovigo6894/Simulador-IMSS-DEMO/main/imagen.jpg", width=90)

with col2:
    st.markdown("""
    <div style='margin-top: 10px;'>
        <h1 style='margin-bottom: 0;'>Optipensión 73</h1>
        <p style='color: #64748b;'>Simulador Estratégico de Pensión IMSS Ley 73</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ============================================
# DATOS BÁSICOS
# ============================================
st.markdown("### 📋 Datos básicos")

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
    
    # Tarjeta de pensión
    st.markdown(f"""
    <div class="result-card">
        <div class="result-label">PENSIÓN ESTIMADA</div>
        <div class="result-number">{formatear_moneda(pension)}</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.caption("💡 Una estrategia adecuada podría aumentar este monto.")
    
    # Impacto potencial en tarjetas
    st.markdown("### 📊 Impacto potencial")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Pensión optimizada", formatear_moneda(impacto['optimizada']))
    
    with col2:
        st.metric("Diferencia mensual", formatear_moneda(impacto['diferencia']))
    
    with col3:
        st.metric("En 20 años", formatear_moneda(impacto['perdida_20']))

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ============================================
# VERSIÓN PRO
# ============================================
st.markdown("""
<div style='text-align: center; margin: 1rem 0;'>
    <span class="pro-badge">🔒 VERSIÓN PRO</span>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style='background: white; border-radius: 1.5rem; padding: 1.5rem; border: 1px solid #e9eef3; margin: 1rem 0;'>
    <p style='margin: 0.5rem 0;'>✅ <strong>Modalidad 40</strong> - Cálculo exacto de inversión y ROI</p>
    <p style='margin: 0.5rem 0;'>✅ <strong>Comparativa de edades</strong> - 60 vs 65 años</p>
    <p style='margin: 0.5rem 0;'>✅ <strong>Proyección con inflación</strong> - Valor real futuro</p>
    <p style='margin: 0.5rem 0;'>✅ <strong>Reporte PDF</strong> - Listo para presentar</p>
    <p style='margin: 0.5rem 0;'>✅ <strong>Asesoría personalizada</strong> - Vía WhatsApp</p>
</div>
""", unsafe_allow_html=True)

st.link_button(
    "💎 Adquirir versión PRO",
    WHATSAPP,
    use_container_width=True
)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# ============================================
# FOOTER COMPLETO
# ============================================
st.markdown(f"""
<div class="footer-text">

### 📌 TÉRMINOS Y CONDICIONES

El uso de este simulador implica la aceptación de los siguientes términos:

• **Naturaleza del servicio**: Este simulador proporciona estimaciones basadas en modelos matemáticos y la Ley 73 del IMSS. Los resultados son aproximados y no constituyen un dictamen oficial ni una garantía de pago.

• **Limitación de responsabilidad**: Optipensión 73 no se hace responsable por decisiones tomadas basadas exclusivamente en los resultados de esta demo. Se recomienda consultar con un asesor certificado.

• **Uso personal**: Esta herramienta es para uso informativo personal. No debe utilizarse como asesoría financiera profesional.

---

### 🔒 AVISO DE PRIVACIDAD

**Protección de datos**: Esta aplicación DEMO **NO almacena, guarda ni comparte** ningún dato personal ingresado por el usuario. Todos los cálculos se realizan en tiempo real y los datos se descartan al cerrar la sesión.

**Cookies**: No utilizamos cookies de rastreo ni almacenamos información de navegación.

**Enlaces a terceros**: El botón de WhatsApp dirige a un canal externo. Una vez que abandonas esta app, la privacidad ya no está bajo nuestro control.

---

### ⚖️ LEGAL

**Propiedad intelectual**: El código, diseño y contenido de Optipensión 73 son propiedad del Ing. Roberto Villarreal Glz. © 2026. Todos los derechos reservados.

---

### 📞 CONTACTO

📧 **Email**: {EMAIL}  
📱 **WhatsApp**: {WHATSAPP_NUMERO}  
📍 **Oficina**: Torreón, Coahuila · México

---

© 2026 Optipensión 73 · Versión {VERSION} · Última actualización: {datetime.now().strftime('%d/%m/%Y')}

</div>
""", unsafe_allow_html=True)
