def es_bisiesto(año):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)


def validar_fecha(fecha):
    # Verificar formato
    partes = fecha.split("/")
    if len(partes) != 3:
        return False

    try:
        dia = int(partes[0])
        mes = int(partes[1])
        anio = int(partes[2])
    except:
        return False

    # Año válido (puedes ajustar rango)
    if anio < 1:
        return False

    # Mes válido
    if mes < 1 or mes > 12:
        return False

    # Días por mes
    if mes == 2:
        if es_bisiesto(anio):
            dias_max = 29
        else:
            dias_max = 28
    elif mes in [4, 6, 9, 11]:
        dias_max = 30
    else:
        dias_max = 31

    # Día válido
    if dia < 1 or dia > dias_max:
        return False

    return True


def main():
    fecha = input("Ingresa la fecha (dd/mm/aaaa): ")

    if validar_fecha(fecha):
        print("Fecha válida")
    else:
        print("Fecha inválida")


if __name__ == "__main__":
    main()