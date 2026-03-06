import streamlit as st
from datetime import datetime

# ============================================
# CONFIGURACIÓN
# ============================================
st.set_page_config(
    page_title="Optipensión 73 DEMO",
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
    semanas = st.number_input("Semanas cotizadas", min_value=500, max_value=3000, value=1315)

salario = st.number_input("Salario diario (SDI)", min_value=200, max_value=2000, value=960)

edad_retiro = st.selectbox("Edad de retiro", [60, 61, 62, 63, 64, 65])

# ============================================
# BOTÓN
# ============================================
if st.button("🔮 Recalcular simulación", use_container_width=True):
    
    # ========================================
    # CÁLCULO SIMPLIFICADO PERO REALISTA
    # ========================================
    # Factores Ley 73
    factores = {60:0.75, 61:0.80, 62:0.85, 63:0.90, 64:0.95, 65:1.00}
    
    # Años hasta retiro
    años_para_retiro = max(0, edad_retiro - edad)
    
    # Semanas totales al retiro
    semanas_totales = semanas + (52 * años_para_retiro)
    
    # Cálculo de cuantía básica (simplificado)
    cuantia_basica = salario * 0.13 * 365
    
    # Incremento por semanas extra
    años_extra = max(0, (semanas_totales - 500) / 52)
    incremento = salario * 0.0245 * 365 * años_extra
    
    # Cuantía total
    cuantia_total = cuantia_basica + incremento
    
    # Asignación por esposa (fijo 15% para demo)
    cuantia_total *= 1.15
    
    # Decreto Fox
    cuantia_total *= 1.11
    
    # Ajuste final
    cuantia_total *= 1.2166
    
    # Aplicar factor por edad
    pension_anual = cuantia_total * factores[edad_retiro]
    pension_mensual = pension_anual / 12
    
    # Pensión optimizada (simulación de estrategia)
    pension_optimizada = pension_mensual * 1.15
    
    diferencia = pension_optimizada - pension_mensual
    perdida_20 = diferencia * 12 * 20
    
    # ========================================
    # MOSTRAR RESULTADOS
    # ========================================
    st.divider()
    st.subheader("Resultado estimado")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Pensión estimada", f"${pension_mensual:,.0f} MXN")
    
    with col2:
        st.metric("Pensión optimizada", f"${pension_optimizada:,.0f} MXN", 
                  delta=f"+${diferencia:,.0f}")
    
    with col3:
        st.metric("En 20 años podrías perder", f"${perdida_20:,.0f} MXN")
    
    # Mensaje de advertencia
    st.warning("⚠️ Una estrategia adecuada podría aumentar tu pensión significativamente.")

# ============================================
# VERSIÓN PRO
# ============================================
st.divider()
st.subheader("🔒 Versión PRO")

st.markdown("""
La versión profesional incluye:

✅ **Modalidad 40** - Cálculo exacto de inversión y ROI  
✅ **Comparativa de edades** - 60 vs 65 años  
✅ **Proyección con inflación** - Valor real futuro  
✅ **Reporte PDF** - Listo para presentar  
✅ **Asesoría personalizada** - Vía WhatsApp
""")

st.link_button(
    "💎 Adquirir versión PRO",
    "https://wa.me/528715791810?text=Hola%20quiero%20la%20versi%C3%B3n%20PRO%20de%20Optipensi%C3%B3n%2073",
    use_container_width=True
)

# ============================================
# FOOTER
# ============================================
st.divider()
st.caption("⚠️ Simulación demostrativa · No constituye dictamen oficial del IMSS")
st.caption(f"© 2026 · Última actualización: {datetime.now().strftime('%d/%m/%Y')}")
