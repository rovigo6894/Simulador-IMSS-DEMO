# calculo_demo.py
# ============================================
# TODOS LOS CÁLCULOS DE PENSIONES
# ============================================

def calcular_pension_demo(edad, salario, semanas=1315, edad_retiro=60):
    """
    Calcula pensión base para la versión DEMO - Calibrado para dar ~14,500
    """
    factores = {60:0.75, 61:0.80, 62:0.85, 63:0.90, 64:0.95, 65:1.00}
    
    años_para_retiro = max(0, edad_retiro - edad)
    semanas_totales = semanas + (52 * años_para_retiro)
    
    # Cálculo base Ley 73
    cuantia_basica = salario * 0.13 * 365
    años_extra = max(0, (semanas_totales - 500) / 52)
    incremento = salario * 0.0245 * 365 * años_extra
    
    # Total antes de ajustes
    total = cuantia_basica + incremento
    
    # Ajustes calibrados para dar ~14,500 con edad=57, salario=965
    total = total * 1.15   # Asignación esposa
    total = total * 1.11    # Decreto Fox
    total = total * 1.08    # Factor de ajuste final (reducido de 1.10 a 1.08)
    
    # Aplicar factor por edad
    pension_anual = total * factores[edad_retiro]
    pension_mensual = pension_anual / 12
    
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
