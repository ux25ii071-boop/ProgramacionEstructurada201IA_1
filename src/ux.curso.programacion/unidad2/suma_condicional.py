def main():
    # Inicialización
    suma = 0
    i = 1

    # Ciclo mientras i sea menor o igual a 100
    while i <= 100:
        
        # Condición: divisible por 3 y impar
        if i % 3 == 0 and i % 2 != 0:
            suma += i
        
        # Incremento
        i = i + 1

    # Mostrar resultado
    print("La suma es:", suma)


# Punto de entrada del programa
if __name__ == "__main__":
    main()