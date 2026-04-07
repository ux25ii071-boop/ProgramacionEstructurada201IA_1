def main():
    # Inicialización
    saldo = 0
    meta = 1000

    # Ciclo
    while saldo <= meta:
        deposito = float(input("Ingresa el depósito: "))
        saldo = saldo + deposito

    # Salida
    print("Meta superada")
    print("Saldo total:", saldo)


# Punto de entrada
if __name__ == "__main__":
    main()