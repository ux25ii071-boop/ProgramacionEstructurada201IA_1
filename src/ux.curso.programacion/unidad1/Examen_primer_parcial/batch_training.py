def main():
    limite = 2500
    total = 0

    while True:
        lote = float(input("Ingresa tamaño del lote en MB: "))
        total += lote
        
        if total > limite:
            print("Límite excedido. OOM evitado.")
            break
        
        print("Total acumulado:", total, "MB")


if __name__ == "__main__":
    main()