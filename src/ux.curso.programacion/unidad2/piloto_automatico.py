def main():
    # Entrada de datos (sensores)
    distancia = float(input("¿A qué distancia está el objeto más cercano (en metros)?: "))
    semaforo = input("¿De qué color está el semáforo? (verde/amarillo/rojo): ").lower()
    peaton = input("¿Hay un peatón cruzando? (si/no): ").lower()

    # Prioridad máxima: Frenado de emergencia
    if distancia < 5 or peaton == "si":
        print("¡FRENO DE EMERGENCIA ACTIVADO! Deteniendo el vehículo inmediatamente.")

    # Regla del semáforo
    elif semaforo == "rojo":
        print("Estado: Detenido. Esperando luz verde.")

    elif semaforo == "amarillo":
        print("Estado: Precaución. Reduciendo velocidad para detenerse.")

    elif semaforo == "verde" and distancia >= 5:
        print("Estado: En movimiento. Todo despejado para avanzar.")

    # Caso de error en sensores
    else:
        print("Error de lectura en sensores: Color de semáforo no reconocido.")

    # Resumen de seguridad
    print("Monitoreo de sensores constante... Sistema activo.")


# Punto de entrada
if __name__ == "__main__":
    main()