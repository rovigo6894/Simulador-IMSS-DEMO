import streamlit as st

# Configuración
st.set_page_config(
    page_title="IMSS Ley 73 - Demo", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# QUEMAR TODO HASTA LOS CIMIENTOS
hide_streamlit_style = """
            <style>
            /* Ocultar menú principal */
            #MainMenu {visibility: hidden;}
            
            /* Ocultar footer */
            footer {visibility: hidden;}
            
            /* Ocultar header */
            header {visibility: hidden;}
            
            /* MATAR "ADMINISTRAR APLICACIÓN" CON TODAS SUS CLASES */
            .st-emotion-cache-1aeihjq,
            .st-emotion-cache-1wmy9hl,
            .st-emotion-cache-14xtw13,
            .st-emotion-cache-1dp5vir,
            .st-emotion-cache-18ni7ap,
            .st-emotion-cache-1wbqy5l,
            .st-emotion-cache-1gwvy6v,
            .st-emotion-cache-1f3w3xq,
            .st-emotion-cache-1p1nwyz,
            .st-emotion-cache-1r6slv0,
            .st-bn, .st-bm, .st-bl,
            [data-testid="stStatus"],
            [data-testid="stNotification"],
            [data-testid="stBottom"],
            [class*="Manage"],
            [class*="manage"],
            [class*="Admin"],
            [class*="admin"] {
                display: none !important;
                visibility: hidden !important;
                opacity: 0 !important;
                height: 0 !important;
                width: 0 !important;
                position: absolute !important;
                top: -9999px !important;
                left: -9999px !important;
                pointer-events: none !important;
            }
            
            /* Mantener el contenido visible */
            .main .block-container {
                visibility: visible !important;
                max-width: 800px;
                padding-top: 2rem;
            }
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Título
st.title("SIMULADOR IMSS LEY 73")
st.markdown("**Versión DEMO - Muestra gratuita**")
st.divider()

# Datos fijos
st.subheader("📋 Datos de ejemplo (fijos)")

col1, col2 = st.columns(2)
with col1:
    st.markdown("**Edad actual**")
    st.markdown("# 55 años")
    st.markdown("")
    st.markdown("**Semanas cotizadas**")
    st.markdown("# 1315")
with col2:
    st.markdown("**Salario promedio**")
    st.markdown("# $965.25")
    st.markdown("")
    st.markdown("**Edad de retiro**")
    st.markdown("# 60 años")

st.divider()

# Incremento
st.markdown(f"""
<div style='background-color: #00a86b; padding: 20px; border-radius: 10px; text-align: center; color: white; margin-bottom: 20px;'>
    <h2 style='color: white; margin:0'>💰 INCREMENTO MENSUAL</h2>
    <h1 style='color: white; font-size: 48px; margin:10px'>$4,031.00</h1>
    <p style='color: #e0e0e0; margin:0'>Tu pensión aumenta con Modalidad 40</p>
</div>
""", unsafe_allow_html=True)

# Comparativa
col_a, col_b = st.columns(2)

with col_a:
    st.markdown(f"""
    <div style='background-color: #f5f5f5; padding: 15px; border-radius: 10px; text-align: center; border: 1px solid #ffcccc;'>
        <h3 style='margin:0; color: #666'>SIN Modalidad 40</h3>
        <h2 style='margin:10px; color: #333'>$14,522.00</h2>
        <p style='margin:0; font-size: 12px; color: #999'>Escenario base</p>
    </div>
    """, unsafe_allow_html=True)

with col_b:
    st.markdown(f"""
    <div style='background-color: #0066b3; padding: 15px; border-radius: 10px; text-align: center; color: white'>
        <h3 style='color: white; margin:0'>CON Modalidad 40</h3>
        <h2 style='color: white; margin:10px'>$18,553.00</h2>
        <p style='color: #e0e0e0; margin:0; font-size: 12px;'>Ejemplo ilustrativo</p>
    </div>
    """, unsafe_allow_html=True)

# Métricas
st.divider()
col_u1, col_u2, col_u3 = st.columns(3)

with col_u1:
    st.markdown("**Inversión total**")
    st.markdown("# $90,305")

with col_u2:
    st.markdown("**Utilidad 20 años**")
    st.markdown("# $1,930,999")
    st.caption("*Suponiendo 240 meses de cobro")

with col_u3:
    st.markdown("**ROI**")
    st.markdown("# 2138%")

# Versión completa
st.divider()
st.markdown("## 🔒 VERSIÓN COMPLETA")

st.markdown("✅ Tus datos reales")
st.markdown("✅ Modalidad 40 (6 a 48 meses)")
st.markdown("✅ Recuperación exacta en meses")
st.markdown("✅ Desglose técnico completo")
st.markdown("✅ Comparativa de escenarios")
st.markdown("✅ Archivo .exe listo para usar")
st.markdown("✅ Manual incluido")

st.markdown("")
st.markdown("### **$1,500 MXN**")
st.markdown("Pago único · Sin instalaciones")

# Botón WhatsApp
st.markdown("### 📲 ¿Interesado?")
whatsapp_link = "https://wa.me/5218715791810?text=Quiero%20la%20versi%C3%B3n%20completa%20del%20Simulador%20IMSS%20PRO"

st.markdown(f"""
<div style='text-align: center'>
    <a href='{whatsapp_link}' target='_blank'>
        <button style='background-color: #25D366; color: white; padding: 15px 30px; 
                border: none; border-radius: 5px; font-size: 20px; font-weight: bold;
                cursor: pointer; margin-bottom: 20px; width: 100%;'>
            📲 CONTACTAR POR WHATSAPP
        </button>
    </a>
</div>
""", unsafe_allow_html=True)

# Métodos de pago
with st.expander("💳 Métodos de pago aceptados"):
    st.markdown("""
    - **Transferencia bancaria** (CLABE se proporciona al contactar)
    - **OXXO** (generamos código al confirmar)
    """)

# Pie
st.divider()
st.markdown("© Ing. Roberto Villarreal · Demo informativa · Versión completa: $1,500")
