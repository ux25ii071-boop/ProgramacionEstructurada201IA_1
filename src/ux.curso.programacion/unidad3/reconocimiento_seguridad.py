print("--- ESCÁNER BIOMÉTRICO DE IA ---")

# Patrón maestro almacenado
patron_maestro = [1, 0, 1, 1, 0]

# Lista para guardar la lectura del sensor
lectura_sensor = []

# Captura de datos
for i in range(5):
    bit = int(input(f"Ingrese bit {i + 1}: "))
    lectura_sensor.append(bit)

print("\n> Comparando lectura con base de datos...")

# Contador de coincidencias
coincidencias = 0

# Comparación de listas
for i in range(5):
    if lectura_sensor[i] == patron_maestro[i]:
        coincidencias += 1

# Calcular porcentaje
similitud = (coincidencias / 5) * 100

# Mostrar resultados
print(f"\n> Coincidencias encontradas: {coincidencias}")
print(f"> Porcentaje de Similitud: {similitud}%")

# Mostrar listas (reto adicional)
print("\nPatrón Maestro:", patron_maestro)
print("Lectura Sensor:", lectura_sensor)

# Decisión final
if similitud == 100:
    print("\nESTADO: ACCESO TOTAL: Identidad Verificada.")

elif similitud >= 60:
    print("\nESTADO: ADVERTENCIA: Similitud parcial. Se requiere verificación manual.")

else:
    print("\nESTADO: ALERTA: Intruso detectado. Sistema bloqueado.")