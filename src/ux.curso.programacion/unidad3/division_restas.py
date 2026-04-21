def division_por_restas(dividendo, divisor):
    if divisor == 0:
        return None, None

    cociente = 0
    resto = dividendo

    while resto >= divisor:
        resto -= divisor
        cociente += 1

    return cociente, resto


def main():
    # Entrada de datos
    dividendo = int(input("Ingresa el dividendo: "))
    divisor = int(input("Ingresa el divisor: "))

    # Validación y proceso
    if divisor == 0:
        print("Error: División por cero")
    else:
        cociente, resto = division_por_restas(dividendo, divisor)
        print("Cociente:", cociente)
        print("Resto:", resto)


# Punto de entrada del programa
if __name__ == "__main__":
    main()