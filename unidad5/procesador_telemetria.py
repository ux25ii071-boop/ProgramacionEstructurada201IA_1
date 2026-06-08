import sys


def limpiar_lecturas(lista_datos):
    """
    Elimina valores atípicos de una lista de lecturas.
    Solo conserva valores entre 0.0 y 100.0.
    """
    lista_filtrada = []

    for dato in lista_datos:
        if dato >= 0.0 and dato <= 100.0:
            lista_filtrada.append(dato)

    return lista_filtrada


def calcular_alertas(lista_filtrada, umbral_critico):
    """
    Cuenta cuántas lecturas están por debajo
    del umbral crítico.
    """
    total_alertas = 0

    for lectura in lista_filtrada:
        if lectura < umbral_critico:
            total_alertas += 1

    return total_alertas


def generar_log_sistema(total_alertas):
    """
    Genera un mensaje de log indicando
    la plataforma y la acción a realizar.
    """
    sistema = sys.platform

    if total_alertas > 3:
        accion = "ABORTAR"
    else:
        accion = "PERMITIDA"

    log = f"[SISTEMA {sistema}] Alertas críticas encontradas: {total_alertas}. Acción: {accion}"

    return log


if __name__ == "__main__":

    lecturas_raw = [12.5, -5.0, 88.2, 120.1, 1.2, 0.0, 45.6, 2.5]

    UMBRAL = 3.0

    print("=== SISTEMA DE TELEMETRÍA DE AGENTE AUTÓNOMO ===\n")

    lecturas_limpias = limpiar_lecturas(lecturas_raw)

    total_alertas = calcular_alertas(lecturas_limpias, UMBRAL)

    log_final = generar_log_sistema(total_alertas)

    print(log_final)


"""
EVIDENCIAS DE CONTROL DE CALIDAD

1. PROMPT UTILIZADO

Actúa como un programador experto en Python Estructurado.
Escribe el código de una función llamada limpiar_lecturas.
Recibe como parámetro una lista de números flotantes y debe
retornar una nueva lista con los valores válidos.
Restricciones estrictas:
1. No utilices programación orientada a objetos.
2. No utilices manejo de excepciones.
3. Incluye documentación mediante Docstring descriptivo.

--------------------------------------------------

2. TABLA DE PRUEBA MANUAL

Datos de entrada:

lecturas_raw = [-10.0, 150.0, -5.0]
UMBRAL = 3.0

Paso 1:
limpiar_lecturas()

-10.0 -> descartado
150.0 -> descartado
-5.0 -> descartado

Resultado:
[]

Paso 2:
calcular_alertas([], 3.0)

No hay elementos para recorrer.

Resultado:
0

Paso 3:
generar_log_sistema(0)

Como 0 no es mayor que 3:
accion = PERMITIDA

Resultado:
[SISTEMA plataforma] Alertas críticas encontradas: 0.
Acción: PERMITIDA

--------------------------------------------------

3. AUDITORÍA DE CÓDIGO

La IA inicialmente sugirió una comprensión de listas para
filtrar datos:

[dato for dato in lista_datos if 0 <= dato <= 100]

Sin embargo, se sustituyó por un ciclo for tradicional
porque el objetivo de la práctica es mantener una
programación estructurada básica.

No se utilizaron bibliotecas externas.
No se utilizaron bloques try-except.
No se utilizó programación orientada a objetos.
"""