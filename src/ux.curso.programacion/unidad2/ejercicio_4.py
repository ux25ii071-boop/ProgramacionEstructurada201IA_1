def main():
    # Inicialización
    suma = 0

    # Ciclo
    while True:
        numero = int(input("Ingresa un número: "))
        suma = suma + numero

        # Evaluación de parada
        if suma > 500:
            break

    # Salida
    print("La suma total es:", suma)


if __name__ == "__main__":
    main()