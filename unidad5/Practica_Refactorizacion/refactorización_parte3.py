"""
Materia: Programación Estructurada
Laboratorio: Refactorización y Análisis de Código (Parte III)
Alumno: Bruno Martínez Jiménez
"""
import math  # El novato solo importó math esta vez

# =====================================================================
# RETO 1: Inicializador de Tablero de Juego (Matrices)
# Mejora: 
#- Se utiliza comprensión de listas para crear filas independientes.
# - Evita el problema de referencias compartidas.
# =====================================================================
def inicializar_tablero_vacio():
    return [[0 for _ in range(4)] for _ in range(4)]

# =====================================================================
# RETO 2: Recortador de Valores Atípicos (Clamping de Datos)
# Mejora:
# - Se utilizan las funciones min() y max().
# - Código más compacto y legible.
# =====================================================================
def limitar_senal_sensor(valor_lectura, minimo, maximo):
    return max(minimo, min(valor_lectura, maximo))

# =====================================================================
# RETO 3: Buscador del Valor Más Cercano a Cero (Error Mínimo)
# Mejora:
# - Se utiliza abs() para obtener el valor absoluto.
# - Se utiliza min() para encontrar el menor valor.
# =====================================================================
def buscar_error_minimo(lista_errores):
    return min(abs(error) for error in lista_errores)
# =====================================================================
# RETO 4: Filtro de Valores Únicos (Eliminador de Duplicados)
# Mejora:
# - Se utiliza set() para eliminar duplicados.
# - Mucho más eficiente que los ciclos anidados.
# =====================================================================
def depurar_usuarios_repetidos(lista_ids):
    return list(set(lista_ids))

# === PROGRAMA PRINCIPAL (Punto de entrada para probar) ===
def main():
    print("--- Probando Código Inicial (Parte III) ---")
    
    tablero_ia = inicializar_tablero_vacio()
    print("Tablero inicializado de 4x4:")
    for fila in tablero_ia:
        print(fila)
        
    print(
        "Lectura recortada (125.4 en rango 0-100):", 
        limitar_senal_sensor(125.4, 0.0, 100.0)
    )
    
    errores_entrenamiento = [0.45, -0.12, 0.89, -0.03, 0.22]
    print(
        "El error más cercano a cero es:", 
        buscar_error_minimo(errores_entrenamiento)
    )
    
    ids_discord = [4521, 8892, 4521, 1022, 8892, 9931]
    print(
        "Lista de IDs únicas filtradas:", 
        depurar_usuarios_repetidos(ids_discord)
    )
if __name__ == "__main__":
    main()