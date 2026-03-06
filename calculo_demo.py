def calcular_pension_demo(salario_diario):

    pension_base = salario_diario * 0.55

    pension_mejorada = pension_base * 1.28

    diferencia = pension_mejorada - pension_base

    perdida_20 = diferencia * 12 * 20

    return pension_base, pension_mejorada, diferencia, perdida_20
