print("--- ANALIZADOR DE SENTIMIENTOS IA ---")

# Vector de sentimientos
puntajes_sentimiento = [0, 0, 0]

# Lectura de 5 palabras
for i in range(5):
    clasificacion = int(input(f"Palabra {i + 1} - Clasificación (0: Positivo, 1: Neutral, 2: Negativo): "))

    # Incrementar posición correspondiente
    puntajes_sentimiento[clasificacion] += 1

# Buscar el valor mayor manualmente
mayor = puntajes_sentimiento[0]
indice_mayor = 0

for i in range(1, 3):
    if puntajes_sentimiento[i] > mayor:
        mayor = puntajes_sentimiento[i]
        indice_mayor = i

# Mostrar vector final
print("\nEstado final del vector de características:", puntajes_sentimiento)

# Resultado final
if indice_mayor == 0:
    print("Resultado de IA: La frase es Positiva (Predominancia en índice 0)")

elif indice_mayor == 1:
    print("Resultado de IA: La frase es Neutral (Predominancia en índice 1)")

elif indice_mayor == 2:
    print("Resultado de IA: La frase es Negativa (Predominancia en índice 2)")