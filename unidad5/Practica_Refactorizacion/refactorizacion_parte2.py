"""
Materia: Programación Estructurada
Laboratorio: Refactorización y Análisis de Código (Parte II)
Alumno: Bruno Martínez Jiménez
"""

import random
import statistics  # Se agrega para calcular la mediana


# =====================================================================
# RETO 1: Formateador de Nombres de Usuario para Discord
# Mejora:
# - Se utiliza strip() para eliminar espacios al inicio y final.
# - Se utiliza capitalize() para poner la primera letra en mayúscula
#   y el resto en minúscula.
# =====================================================================
def limpiar_nombre_usuario(nombre_sucio):
    return nombre_sucio.strip().capitalize()


# =====================================================================
# RETO 2: Buscador de Palabras Prohibidas
# Mejora:
# - Se utiliza el operador "in" para buscar subcadenas.
# - Código más simple y eficiente.
# =====================================================================
def contiene_palabra_bloqueada(mensaje_chat, palabra_prohibida):
    return palabra_prohibida in mensaje_chat


# =====================================================================
# RETO 3: Generador de Contraseñas Temporales
# Mejora:
# - Se utiliza random.choices() para seleccionar varios caracteres.
# - Se utiliza join() para unir los caracteres de forma eficiente.
# =====================================================================
def generar_clave_temporal():
    caracteres_validos = (
        "ABCDEFGHJKLMNPQRSTUVWXYZ"
        "abcdefghijkmnpqrstuvwxyz"
        "23456789"
    )

    return "".join(random.choices(caracteres_validos, k=8))


# =====================================================================
# RETO 4: Buscador del Valor Central (Mediana)
# Mejora:
# - Se utiliza statistics.median().
# - Evita implementar manualmente el ordenamiento y el cálculo.
# =====================================================================
def calcular_mediana_latencia(lista_pings):
    return statistics.median(lista_pings)


# =====================================================================
# PROGRAMA PRINCIPAL
# =====================================================================
def main():
    print("--- Probando Código Refactorizado (Parte II) ---")

    print("Usuario limpio:",
          limpiar_nombre_usuario("   luNA_eDUaRDo  "))

    msg = "No digas malas palabras en este servidor"
    print("¿Tiene groserías?:",
          contiene_palabra_bloqueada(msg, "malas"))

    print("Clave generada por el sistema:",
          generar_clave_temporal())

    pings_servidor = [120, 45, 80, 23, 150, 62]
    print("Mediana de latencia encontrada:",
          calcular_mediana_latencia(pings_servidor))


if __name__ == "__main__":
    main()