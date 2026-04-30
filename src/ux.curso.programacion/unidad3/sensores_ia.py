def main():
    print("--- MÓDULO DE SENSORES (VECTORES) ---")

    sensores_distancia = []

    # Llenar vector
    for i in range(5):
        distancia = float(input(f"Ingrese distancia sensor {i+1}: "))
        sensores_distancia.append(distancia)

    # Promedio
    promedio = sum(sensores_distancia) / len(sensores_distancia)

    if promedio < 2.0:
        print("Aviso: Reduciendo velocidad global")
    else:
        print(f"Promedio de proximidad: {promedio}m. Estado: Seguro.")

    print("\n--- MÓDULO DE VISIÓN (MATRICES) ---")

    camara_ia = []

    # Llenar matriz 3x3
    for fila in range(3):
        fila_actual = []
        for col in range(3):
            valor = int(input(f"Fila {fila}, Col {col} (Brillo 0-255): "))

            # Saturación
            if valor > 255:
                valor = 255

            fila_actual.append(valor)

        camara_ia.append(fila_actual)

    # Mostrar matriz
    print("\nVisualización de la imagen capturada:")
    for fila in camara_ia:
        print(fila)

    # Contar píxeles > 200
    contador = 0
    for fila in camara_ia:
        for valor in fila:
            if valor > 200:
                contador += 1

    print("\nResultado de Análisis IA:")
    print(f"Se detectaron {contador} píxeles de alta intensidad.")


if __name__ == "__main__":
    main()