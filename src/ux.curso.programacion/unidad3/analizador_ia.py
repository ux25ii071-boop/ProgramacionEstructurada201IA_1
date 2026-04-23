def normalizar_mensaje(texto):
    # Convierte a minúsculas y elimina espacios extra
    return texto.lower().strip()


def detectar_intencion(mensaje):
    # Palabras clave
    comandos = ["encender", "activar", "reproducir"]
    soporte = ["ayuda", "error", "fallo"]

    # Buscar palabras en el mensaje
    for palabra in comandos:
        if palabra in mensaje:
            return "COMANDO DE ACCIÓN"

    for palabra in soporte:
        if palabra in mensaje:
            return "REPORTE DE SOPORTE"

    return "CONSULTA GENERAL"


def main():
    # Entrada del usuario
    mensaje = input("Ingrese comando de voz: ")

    print("\n--- PROCESANDO POR IA ---")

    # Normalizar mensaje
    mensaje_limpio = normalizar_mensaje(mensaje)

    # Detectar intención
    categoria = detectar_intencion(mensaje_limpio)

    # Longitud del mensaje original
    longitud = len(mensaje)

    # Salida
    print(f'Mensaje Normalizado: "{mensaje_limpio}"')
    print(f"Categoría de Intención: {categoria}")
    print(f"Longitud del mensaje: {longitud} caracteres")
    print("--------------------------")


if __name__ == "__main__":
    main()