# calculos.py
# ============================================
# TODOS LOS CÁLCULOS DE PENSIONES
# ============================================

def calcular_pension_demo(edad, salario, semanas=1315, edad_retiro=60):
    """
    Calcula pensión base para la versión DEMO
    """
    factores = {60:0.75, 61:0.80, 62:0.85, 63:0.90, 64:0.95, 65:1.00}
    
    años_para_retiro = max(0, edad_retiro - edad)
    semanas_totales = semanas + (52 * años_para_retiro)
    
    cuantia_basica = salario * 0.13 * 365
    años_extra = max(0, (semanas_totales - 500) / 52)
    incremento = salario * 0.0245 * 365 * años_extra
    cuantia_total = (cuantia_basica + incremento) * 1.15 * 1.11 * 1.2166
    pension_mensual = cuantia_total * factores[edad_retiro] / 12
    
    return round(pension_mensual, 2)

def formatear_moneda(valor):
    """Formatea números a moneda MXN"""
    return f"${valor:,.0f} MXN"

def calcular_impacto(pension_base):
    """Calcula impacto financiero aproximado"""
    pension_optimizada = pension_base * 1.15
    diferencia = pension_optimizada - pension_base
    perdida_20 = diferencia * 12 * 20
    return {
        'base': pension_base,
        'optimizada': pension_optimizada,
        'diferencia': diferencia,
        'perdida_20': perdida_20
    }
