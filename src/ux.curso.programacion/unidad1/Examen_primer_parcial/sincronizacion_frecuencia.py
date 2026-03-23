def main():
    frecuencia_A = int(input("Ingresa la frecuencia del Agente A (Hz): "))
    frecuencia_B = int(input("Ingresa la frecuencia del Agente B (Hz): "))

    if frecuencia_B == 0 or frecuencia_A == 0:
        print("No se puede dividir entre 0")
    elif frecuencia_A % frecuencia_B == 0 or frecuencia_B % frecuencia_A == 0:
        print("Existe sincronización perfecta entre los agentes")
    else:
        print("No hay sincronización de ciclos")


if __name__ == "__main__":
    main()
