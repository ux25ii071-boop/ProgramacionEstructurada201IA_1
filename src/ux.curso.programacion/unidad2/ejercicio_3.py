def main():
    # Leer N
    N = int(input("Ingresa la cantidad de números impares: "))

    # Inicialización
    contador = 0
    numero = 1

    # Ciclo
    while contador < N:
        print(numero)
        numero = numero + 2
        contador = contador + 1


# Punto de entrada del programa
if __name__ == "__main__":
    main()