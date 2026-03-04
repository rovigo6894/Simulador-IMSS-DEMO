import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="OptiPensión 73 - DEMO", 
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
# LOGO Y NOMBRE COMERCIAL
# ============================================

col_logo, col_titulo = st.columns([1, 4])

with col_logo:
    st.markdown("# 📊")  # Placeholder para logo profesional

with col_titulo:
    st.markdown("# OPTIPENSIÓN 73")
    st.markdown("**Optimización Integral de Pensión · Ley 73**")

st.divider()

# ============================================
# DESCRIPCIÓN PROFESIONAL
# ============================================

st.markdown("""
### Simulador Estratégico - Versión DEMO

*Esta es una muestra interactiva. Los cálculos son demostrativos y no constituyen un dictamen oficial del IMSS.*
""")

st.divider()

# ============================================
# VARIABLES EDITABLES (con énfasis demostrativo)
# ============================================

st.subheader("📋 Parámetros demostrativos")

col1, col2 = st.columns(2)

with col1:
    edad_actual = st.slider("Edad actual", 45, 65, 55, 
                           help="Puedes mover la edad para ver cómo cambia el resultado")
    edad_retiro = st.selectbox("Edad de retiro", [60, 61, 62, 63, 64, 65], index=0,
                               help="Elige la edad a la que planeas retirarte")

with col2:
    # Salario EDITABLE pero con advertencia
    salario_demo = st.number_input("Salario promedio (demostrativo)", 
                                   min_value=5000, max_value=50000, 
                                   value=20000, step=1000,
                                   help="💡 VALOR DEMOSTRATIVO - En la versión completa usarás tu salario real")
    
    # Semanas fijas (gancho)
    st.metric("Semanas cotizadas", "1,200", 
             help="En la versión completa usarás tus semanas reales")

st.caption("⚠️ **Importante:** Este es un cálculo demostrativo con datos de ejemplo.")

st.divider()

# ============================================
# CÁLCULO SIMPLIFICADO (demostrativo)
# ============================================

st.subheader("📊 Resultado demostrativo")

# Factor por edad
factores = {60:0.75, 61:0.80, 62:0.85, 63:0.90, 64:0.95, 65:1.00}
factor_edad = factores[edad_retiro]

# Fórmula simplificada (a propósito)
pension_demo = salario_demo * factor_edad * 0.5

# Mostrar resultado con estilo profesional
st.markdown(f"""
<div style='background-color: #f8f9fa; padding: 20px; border-radius: 10px; text-align: center; border: 1px solid #dee2e6;'>
    <h2 style='color: #0066b3; margin:0'>PENSIÓN ESTIMADA</h2>
    <h1 style='color: #0066b3; font-size: 48px; margin:10px'>${pension_demo:,.0f}</h1>
    <p style='color: #6c757d; margin:0'>Retiro a los {edad_retiro} años</p>
    <p style='color: #6c757d; margin:0; font-size: 12px;'>*Cálculo demostrativo con parámetros de ejemplo</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ============================================
# GLOSARIO PROFESIONAL
# ============================================

with st.expander("📘 Glosario de términos"):
    st.markdown("""
    | Término | Descripción |
    |---------|-------------|
    | **Ley 73** | Régimen de pensiones para quienes cotizaron antes del 1 de julio de 1997 |
    | **Factor por edad** | Porcentaje de la pensión según la edad de retiro (75% a 60 años, 80% a 61, etc.) |
    | **Semanas cotizadas** | Mínimo 500 semanas para tener derecho a pensión |
    | **Salario promedio** | Se calcula con las últimas 250 semanas cotizadas |
    | **Modalidad 40** | Continuación voluntaria para aumentar el salario promedio |
    """)

st.divider()

# ============================================
# OFERTA COMERCIAL (sin "pago único" ni "acceso de por vida")
# ============================================

st.markdown("## 🔒 Versión Completa")

col_pro1, col_pro2 = st.columns([3, 2])

with col_pro1:
    st.markdown("""
    ### Obtén tu diagnóstico personalizado:
    
    ✅ **Cálculo con tus datos reales** (semanas, salario, edad)
    ✅ **Análisis de Modalidad 40** (ROI, recuperación, utilidad)
    ✅ **Comparativa de escenarios** (60 vs 61...65 años)
    ✅ **Proyección a 20 años** con ajuste inflacionario
    ✅ **Recomendación estratégica personalizada**
    ✅ **Asesoría post-diagnóstico**
    """)

with col_pro2:
    st.markdown("""
    ### Diferentes paquetes disponibles
    
    **Desde $1,500 MXN**
    
    **Formas de pago:**
    - Transferencia bancaria
    - Mercado Pago
    - OXXO
    """)
    
    # Botón de WhatsApp profesional
    whatsapp_link = "https://wa.me/5218715791810?text=Quiero%20información%20sobre%20los%20paquetes%20de%20OptiPensión%2073"
    st.markdown(f"""
    <div style='text-align: center; margin-top: 20px;'>
        <a href='{whatsapp_link}' target='_blank'>
            <button style='background-color: #25D366; color: white; padding: 12px 20px; 
                    border: none; border-radius: 5px; font-size: 16px; font-weight: bold;
                    cursor: pointer; width: 100%;'>
                📲 SOLICITAR INFORMACIÓN
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ============================================
# TESTIMONIOS (profesionales)
# ============================================

st.markdown("### 💬 Experiencias de usuarios")

col_t1, col_t2 = st.columns(2)

with col_t1:
    st.markdown("""
    > *"El análisis de Modalidad 40 me ayudó a decidir invertir en mi pensión. La recuperación estimada fue exacta."*
    > 
    > — **Carlos R., Ingeniero Industrial**
    """)

with col_t2:
    st.markdown("""
    > *"Pensé que me pensionaba a los 60, pero el simulador me mostró que esperar un año más aumentaba mi pensión en $1,500 mensuales."*
    > 
    > — **María L., Contadora**
    """)

st.divider()

# ============================================
# PIE DE PÁGINA PROFESIONAL
# ============================================

st.markdown("""
---
🔒 *Al usar este simulador aceptas nuestros Términos y Condiciones.  
No almacenamos datos personales ni los compartimos con terceros.  
Este cálculo es una simulación demostrativa y no constituye un dictamen oficial del IMSS.*  

📧 contacto@optipension73.com | 📱 WhatsApp: 871 579 1810

**OptiPensión 73®** · Optimización Integral de Pensión  
© 2026 · Todos los derechos reservados

[Política de Privacidad](https://www.optipension73.com/privacidad) · [Términos de Servicio](https://www.optipension73.com/terminos)
""")

st.caption(f"Última actualización: {datetime.now().strftime('%d/%m/%Y')}")
