def main():
    # Inicialización
    suma = 0

    # Ciclo
    while True:
        numero = int(input("Ingresa un número: "))

        # Validación de rango
        if numero >= 10 and numero <= 50:
            suma += numero
        else:
            break

    # Salida
    print("La suma total es:", suma)


# Punto de entrada
if __name__ == "__main__":
    main()