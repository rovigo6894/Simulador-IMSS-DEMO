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

# Ocultar elementos de Streamlit
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .stApp header {display: none !important;}
            .stApp [data-testid="stToolbar"] {display: none !important;}
            .stApp [data-testid="stDecoration"] {display: none !important;}
            .main .block-container {padding-top: 2rem !important;}
            
            /* Ocultar cualquier elemento de GitHub */
            .stApp [data-testid="stStatusWidget"] {display: none !important;}
            .stApp [data-testid="baseButton-header"] {display: none !important;}
            a[href*="github"] {display: none !important;}
            
            @media (max-width: 768px) {
                .stApp [data-testid="stToolbar"] {display: none !important;}
            }
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
# VERSIÓN PRO
# ============================================
st.subheader("🔒 Versión Profesional")

st.markdown("""
✅ **Diagnóstico personalizado** con tus datos reales  
✅ **Modalidad 40** - Cálculo exacto de inversión y ROI  
✅ **Comparativa de edades** - 60 vs 61...65 años  
✅ **Proyección a 20 años** con ajuste inflacionario  
✅ **Reporte PDF** listo para presentar  
✅ **Asesoría personalizada** vía WhatsApp
""")

st.link_button(
    "📲 CONTACTAR PARA VERSIÓN PRO",
    WHATSAPP,
    use_container_width=True
)

st.divider()

# ============================================
# FOOTER SIMPLE (SIN ERRORES)
# ============================================
st.markdown("### 📌 TÉRMINOS Y CONDICIONES")
st.markdown("""
El uso de este simulador implica la aceptación de los siguientes términos:

• **Naturaleza del servicio**: Este simulador proporciona estimaciones basadas en modelos matemáticos y la Ley 73 del IMSS. Los resultados son aproximados y no constituyen un dictamen oficial ni una garantía de pago.

• **Limitación de responsabilidad**: Optipensión 73 no se hace responsable por decisiones tomadas basadas exclusivamente en los resultados de esta demo. Se recomienda consultar con un asesor certificado.

• **Uso personal**: Esta herramienta es para uso informativo personal.
""")

st.divider()

st.markdown("### 🔒 AVISO DE PRIVACIDAD")
st.markdown("""
**Protección de datos**: Esta aplicación DEMO **NO almacena, guarda ni comparte** ningún dato personal ingresado por el usuario. Todos los cálculos se realizan en tiempo real y los datos se descartan al cerrar la sesión.

**Cookies**: No utilizamos cookies de rastreo ni almacenamos información de navegación.
""")

st.divider()

st.markdown("### ⚖️ LEGAL")
st.markdown(f"""
**Propiedad intelectual**: El código, diseño y contenido de Optipensión 73 son propiedad del Ing. Roberto Villarreal Glz. © 2026. Todos los derechos reservados.

📧 **Email**: {EMAIL}  
📱 **WhatsApp**: {WHATSAPP_NUMERO}  
📍 **Oficina**: Torreón, Coahuila · México

---

© 2026 Optipensión 73 · Versión {VERSION} · Última actualización: {datetime.now().strftime('%d/%m/%Y')}
""")
