def convertir_a_romano(numero):
    valores = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]

    romano = ""

    for valor, simbolo in valores:
        while numero >= valor:
            romano += simbolo
            numero -= valor

    return romano


def main():
    while True:
        numero = int(input("Ingresa un número (1-3000): "))

        if numero > 0 and numero <= 3000:
            resultado = convertir_a_romano(numero)
            print("Número romano:", resultado)
            break
        else:
            print("Error, número inválido. Intenta de nuevo.")


if __name__ == "__main__":
    main()