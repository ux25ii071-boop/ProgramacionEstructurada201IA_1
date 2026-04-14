# --- SISTEMA DE MONITOREO INDUSTRIAL --- 

def limpiar_dato(lectura_cruda): 
    """
    FUNCIÓN 1: Convierte a float y filtra ruido.
    """
    try:
        valor = float(lectura_cruda)
        if valor > 100 or valor < 0:
            return None
        return valor
    except:
        return None


def calcular_alerta(valor_normalizado): 
    """
    FUNCIÓN 2: Clasifica el nivel de alerta.
    """
    if valor_normalizado > 0.8:
        return "CRÍTICO"
    elif valor_normalizado > 0.5:
        return "PRECAUCIÓN"
    else:
        return "NORMAL"


def obtener_estadisticas(lista_datos): 
    """
    FUNCIÓN 3: Devuelve (max, min, promedio)
    """
    maximo = max(lista_datos)
    minimo = min(lista_datos)
    promedio = sum(lista_datos) / len(lista_datos)
    
    return (maximo, minimo, promedio)


def generar_reporte(total_datos, validos, estadisticas): 
    """
    FUNCIÓN 4: Imprime resumen
    """
    descartados = total_datos - validos
    maximo, minimo, promedio = estadisticas

    print("----- REPORTE DE TELEMETRÍA -----")
    print(f"Total de datos leídos: {total_datos}")
    print(f"Datos válidos: {validos}")
    print(f"Datos descartados: {descartados}")
    print(f"Valor máximo: {maximo:.2f}")
    print(f"Valor mínimo: {minimo:.2f}")
    print(f"Promedio: {promedio:.2f}")


# --- LÓGICA PRINCIPAL (NO MODIFICAR) --- 
def ejecutar_pipeline(): 
    datos_finales = [] 
    cuenta_total = 0 
     
    with open("lecturas_sensores.txt", "r") as f: 
        for linea in f: 
            cuenta_total += 1 
            valor = limpiar_dato(linea.strip()) 
            if valor is not None: 
                datos_finales.append(valor / 100) 
     
    if datos_finales: 
        stats = obtener_estadisticas(datos_finales) 
        generar_reporte(cuenta_total, len(datos_finales), stats) 

if __name__ == "__main__": 
    ejecutar_pipeline()