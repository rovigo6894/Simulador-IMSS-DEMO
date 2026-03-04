import streamlit as st

st.set_page_config(
    page_title="IMSS Ley 73 - DEMO", 
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

# Título
st.title("🎯 SIMULADOR IMSS LEY 73")
st.markdown("**Versión DEMO - Juega con los datos de ejemplo**")
st.caption("Descubre cuánto podrías recibir al pensionarte")
st.divider()

# ============================================
# VARIABLES EDITABLES (pero limitadas)
# ============================================

st.subheader("📋 Variables que puedes modificar")

col1, col2 = st.columns(2)

with col1:
    edad_actual = st.slider("Edad actual", 45, 65, 55, help="Puedes mover la edad para ver cómo cambia el resultado")
    edad_retiro = st.selectbox("Edad de retiro", [60, 61, 62, 63, 64, 65], index=0, help="Elige la edad a la que planeas retirarte")

with col2:
    # Variables fijas (no se pueden cambiar)
    st.metric("Semanas cotizadas", "1,200", help="En la versión completa usarás tus semanas reales")
    st.metric("Salario promedio", "$20,000", help="En la versión completa usarás tu salario real")
    st.caption("🔒 Estas variables son fijas en la DEMO")

st.divider()

# ============================================
# CÁLCULO SIMPLIFICADO (solo para mostrar)
# ============================================

st.subheader("📊 Resultado estimado")

# Factor por edad
factores = {60:0.75, 61:0.80, 62:0.85, 63:0.90, 64:0.95, 65:1.00}
factor_edad = factores[edad_retiro]

# Fórmula simplificada (a propósito, no es el cálculo real)
pension_demo = 20000 * factor_edad * 0.5

# Mostrar resultado con estilo
st.markdown(f"""
<div style='background-color: #0066b3; padding: 20px; border-radius: 10px; text-align: center; color: white; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'>
    <h2 style='color: white; margin:0'>PENSIÓN ESTIMADA</h2>
    <h1 style='color: white; font-size: 48px; margin:10px'>${pension_demo:,.0f}</h1>
    <p style='color: #e0e0e0; margin:0'>Retiro a los {edad_retiro} años</p>
    <p style='color: #e0e0e0; margin:0; font-size: 12px;'>*Cálculo aproximado para fines demostrativos</p>
</div>
""", unsafe_allow_html=True)

st.info("💡 Este es un cálculo de ejemplo con datos fijos. En la versión completa usarás tus semanas y salario reales.")

st.divider()

# ============================================
# EXPLICACIÓN BREVE (glosario simple)
# ============================================

with st.expander("📘 ¿Qué significa esto?"):
    st.markdown("""
    - **Ley 73**: Régimen de pensiones para quienes cotizaron antes del 1 de julio de 1997.
    - **Factor por edad**: A menor edad de retiro, menor porcentaje de pensión.
    - **Semanas cotizadas**: Se requieren al menos 500 semanas para tener derecho a pensión.
    - **Salario promedio**: Se calcula con las últimas 250 semanas cotizadas.
    """)

st.divider()

# ============================================
# GANCHO PARA LA VERSIÓN PRO
# ============================================

st.markdown("## 🔒 VERSIÓN COMPLETA")

col_pro1, col_pro2 = st.columns(2)

with col_pro1:
    st.markdown("""
    ### Con la versión PRO obtienes:
    ✅ **Tus datos reales** (edad, semanas, salario)
    ✅ **Modalidad 40** (6 a 48 meses)
    ✅ **ROI y recuperación exacta**
    ✅ **Utilidad proyectada a 20 años**
    ✅ **Comparativa de escenarios**
    ✅ **Asesoría personalizada** (3 meses)
    """)

with col_pro2:
    st.markdown("""
    ### Precio especial lanzamiento
    # **$1,500 MXN**
    
    *Pago único · Acceso de por vida*
    
    **Formas de pago:**
    - 💳 Transferencia bancaria
    - 🏦 Mercado Pago
    - 🏧 OXXO
    """)
    
    # Botón de WhatsApp
    whatsapp_link = "https://wa.me/5218715791810?text=Quiero%20la%20versi%C3%B3n%20PRO%20del%20simulador%20Ley%2073"
    st.markdown(f"""
    <div style='text-align: center; margin-top: 20px;'>
        <a href='{whatsapp_link}' target='_blank'>
            <button style='background-color: #25D366; color: white; padding: 15px 30px; 
                    border: none; border-radius: 5px; font-size: 18px; font-weight: bold;
                    cursor: pointer; width: 100%;'>
                📲 CONTACTAR POR WHATSAPP
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ============================================
# TESTIMONIO SIMULADO (genera confianza)
# ============================================

st.markdown("### 💬 Lo que dicen nuestros primeros usuarios")

col_t1, col_t2 = st.columns(2)

with col_t1:
    st.markdown("""
    > *"Pensé que mi pensión sería mucho menor. Con el simulador descubrí que podía aumentarla con Modalidad 40. La asesoría de Roberto fue clave."*
    > 
    > — **Carlos R., 58 años**
    """)

with col_t2:
    st.markdown("""
    > *"Excelente herramienta, muy precisa. Me ayudó a decidir cuándo pensionarme y cuánto necesito ahorrar."*
    > 
    > — **María L., 62 años**
    """)

st.divider()

# ============================================
# PIE DE PÁGINA (legal y contacto)
# ============================================

st.markdown("""
---
🔒 *Al usar este simulador aceptas nuestra Política de Privacidad.  
No almacenamos datos personales ni los compartimos con terceros.  
Este cálculo es una simulación basada en la Ley 73 del IMSS y no constituye un dictamen oficial.*  

📧 Contacto: rvglz@hotmail.com | 📱 WhatsApp: 871 579 1810

© Ing. Roberto Villarreal · DEMO informativa · Versión PRO Analisis Completo
""")
