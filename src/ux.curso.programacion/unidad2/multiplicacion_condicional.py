def main():
    # Leer N
    N = int(input("Ingresa un número: "))

    # Inicialización
    factorial = 1
    i = 1

    # Ciclo
    while i <= N:
        factorial = factorial * i
        i = i + 1

    # Mostrar resultado
    print("El factorial es:", factorial)


if __name__ == "__main__":
    main()