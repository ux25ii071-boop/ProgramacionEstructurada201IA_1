def main():
    # Encabezado
    print("   ", end="")
    for i in range(1, 16):
        print(f"{i:4}", end="")
    print()

    # Tabla
    for i in range(1, 16):
        print(f"{i:2}*", end="")  # fila
        for j in range(1, 16):
            print(f"{i*j:4}", end="")
        print()


if __name__ == "__main__":
    main()