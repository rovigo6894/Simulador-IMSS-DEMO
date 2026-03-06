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
    st.image("https://raw.githubusercontent.com/rovigo6894/Simulador-IMSS-DEMO/main/image.jpg", width=80)

with col2:
    st.title("Optipensión 73")
    st.caption("Simulador Estratégico de Pensión IMSS Ley 73")

st.divider()

# ============================================
# DATOS BÁSICOS (SOLO EDAD Y SALARIO)
# ============================================
st.subheader("📋 Datos básicos")

col1, col2 = st.columns(2)

with col1:
    edad = st.number_input("Edad actual", min_value=40, max_value=65, value=57)

with col2:
    salario = st.number_input("Salario diario (SDI)", min_value=200, max_value=2000, value=960)

# Valores fijos para demo
semanas = 1315
edad_retiro = 60

st.caption(f"⚡ Valores de referencia: {semanas} semanas cotizadas · Retiro a los {edad_retiro} años")

# ============================================
# BOTÓN
# ============================================
if st.button("🔮 Recalcular simulación", use_container_width=True):
    
    # ========================================
    # CÁLCULO SIMPLIFICADO PERO REALISTA
    # ========================================
    factores = {60:0.75, 61:0.80, 62:0.85, 63:0.90, 64:0.95, 65:1.00}
    
    años_para_retiro = max(0, edad_retiro - edad)
    semanas_totales = semanas + (52 * años_para_retiro)
    
    cuantia_basica = salario * 0.13 * 365
    años_extra = max(0, (semanas_totales - 500) / 52)
    incremento = salario * 0.0245 * 365 * años_extra
    cuantia_total = (cuantia_basica + incremento) * 1.15 * 1.11 * 1.2166
    pension_mensual = cuantia_total * factores[edad_retiro] / 12
    
    st.success(f"### Pensión estimada: ${pension_mensual:,.0f} MXN")
    st.caption("Una estrategia adecuada podría aumentar este monto.")

st.divider()

# ============================================
# VERSIÓN PRO (SOLO INFORMATIVO)
# ============================================
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
# FOOTER COMPLETO (TÉRMINOS, PRIVACIDAD, COPYRIGHT)
# ============================================
st.divider()

st.markdown("""
<div style='text-align:center; font-size:12px; color:#666; line-height:1.6;'>

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

**Legislación aplicable**: Este servicio se rige por las leyes de los Estados Unidos Mexicanos.

---

### 📞 CONTACTO

📧 **Email**: contacto@optipension73.com  
📱 **WhatsApp**: 871 579 1810  
📍 **Oficina**: Torreón, Coahuila · México

---

</div>
""", unsafe_allow_html=True)

# Copyright al final (simple y claro)
st.caption(f"© 2026 Optipensión 73 · Ing. Roberto Villarreal Glz. · Última actualización: {datetime.now().strftime('%d/%m/%Y')}")
