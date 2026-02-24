import streamlit as st

# Configuración
st.set_page_config(page_title="IMSS Ley 73 - Demo", page_icon="🎯", layout="centered")

# Título
st.title("🎯 SIMULADOR IMSS LEY 73")
st.markdown("**Versión DEMO – Muestra gratuita**")
st.divider()

# ❄️ DATOS CONGELADOS
st.subheader("📋 Datos de ejemplo (fijos)")

col1, col2 = st.columns(2)
with col1:
    st.metric("Edad actual", "55 años")
    st.metric("Semanas cotizadas", "1315")
with col2:
    st.metric("Salario promedio", "$965.25")
    st.metric("Edad de retiro", "60 años")

# Resultados fijos
pension_sin_m40 = 14522
pension_con_m40 = 18553
incremento = pension_con_m40 - pension_sin_m40
inversion_total = 90305
utilidad_20 = 1930999
roi = round((utilidad_20 / inversion_total) * 100, 0)

# ========== RESULTADOS ==========
st.divider()

# INCREMENTO protagonista
st.markdown(f"""
<div style='background-color: #00a86b; padding: 20px; border-radius: 10px; text-align: center; color: white; margin-bottom: 20px;'>
    <h2 style='color: white; margin:0'>💰 INCREMENTO MENSUAL</h2>
    <h1 style='color: white; font-size: 48px; margin:10px'>${incremento:,.2f}</h1>
    <p style='color: #e0e0e0; margin:0'>Tu pensión aumenta con Modalidad 40</p>
</div>
""", unsafe_allow_html=True)

# Comparativa
col_a, col_b = st.columns(2)

with col_a:
    st.markdown(f"""
    <div style='background-color: #f5f5f5; padding: 15px; border-radius: 10px; text-align: center; border: 1px solid #ffcccc;'>
        <h3 style='margin:0; color: #666'>SIN Modalidad 40</h3>
        <h2 style='margin:10px; color: #333'>${pension_sin_m40:,.2f}</h2>
        <p style='margin:0; font-size: 12px; color: #999'>Escenario base</p>
    </div>
    """, unsafe_allow_html=True)

with col_b:
    st.markdown(f"""
    <div style='background-color: #0066b3; padding: 15px; border-radius: 10px; text-align: center; color: white'>
        <h3 style='color: white; margin:0'>CON Modalidad 40</h3>
        <h2 style='color: white; margin:10px'>${pension_con_m40:,.2f}</h2>
        <p style='color: #e0e0e0; margin:0; font-size: 12px;'>Ejemplo ilustrativo</p>
    </div>
    """, unsafe_allow_html=True)

# Métricas
st.divider()
col_u1, col_u2, col_u3 = st.columns(3)

with col_u1:
    st.metric("Inversión total", f"${inversion_total:,.0f}")

with col_u2:
    st.metric("Utilidad 20 años", f"${utilidad_20:,.0f}")
    st.caption("*Suponiendo 240 meses de cobro")

with col_u3:
    st.metric("ROI %", f"{roi:,.0f}%")

# Pie profesional
st.divider()
st.caption("🧾 Modelo basado en Art. 167 Ley 73 y porcentajes vigentes por edad.")
st.caption("© Ing. Roberto Villarreal - Demo informativa")

# ========== GANCHO COMERCIAL ==========
st.divider()
st.markdown("## 🔒 ¿Quieres calcular TU pensión real?")

with st.container():
    st.markdown("---")
    st.markdown("### VERSIÓN COMPLETA")
    
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
    st.markdown("---")

# ========== BOTÓN WHATSAPP (VERDE GRANDE) ==========
st.markdown("### 📲 ¿Interesado?")

whatsapp_link = "https://wa.me/5218715791810?text=Quiero%20la%20versi%C3%B3n%20completa%20del%20Simulador%20IMSS%20PRO"

st.markdown(f"""
<div style='text-align: center'>
    <a href='{whatsapp_link}' target='_blank'>
        <button style='background-color: #25D366; color: white; padding: 15px 30px; 
                border: none; border-radius: 5px; font-size: 20px; font-weight: bold;
                cursor: pointer; margin-bottom: 20px;'>
            💬 CONTACTAR POR WHATSAPP
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

st.divider()
st.caption("© Roberto Villarreal · Demo v2.4 · Versión completa: $1,500")