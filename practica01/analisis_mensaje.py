# 1. IMPORTACIÓN
# Importamos la biblioteca externa y le asignamos un alias 'np'
import numpy as np


def procesar_estadisticas(lista_mensajes):
    """
    Función que recibe datos y utiliza funciones externas
    de la biblioteca NumPy para procesarlos.
    """

    # Promedio
    promedio = np.mean(lista_mensajes)

    # Valor máximo
    pico_maximo = np.max(lista_mensajes)

    # Desviación estándar redondeada a 1 decimal
    desviacion = np.round(np.std(lista_mensajes), 1)

    # Mediana
    mediana = np.median(lista_mensajes)

    return promedio, pico_maximo, desviacion, mediana


# --- Programa Principal ---
def main():

    # Datos: Mensajes enviados cada hora durante 8 horas
    datos_servidor = [15, 42, 88, 30, 120, 55, 72, 20]

    # Llamada a la función
    prom, maximo, ds, med = procesar_estadisticas(datos_servidor)

    print("=== REPORTE DE ACTIVIDAD DEL SERVIDOR ===")
    print(f"Promedio de mensajes por hora: {prom:.2f}")
    print(f"Pico de actividad registrado: {maximo} mensajes")
    print(f"Variabilidad del tráfico (Desviación): {ds}")
    print(f"Mediana de mensajes por hora: {med}")


# Ejecutar el programa
if __name__ == "__main__":
    main()


# Observación:
# Si usamos np.mean() sin importar NumPy con "import numpy as np",
# Python marcará un error llamado NameError porque no reconoce qué es "np".