# acceso_biometrico.py

def main():
    print("--- SISTEMA DE CONTROL BIOMÉTRICO ---\n")

    # Solicitar datos
    nombre = input("Nombre del Ingeniero: ")
    id_empleado = int(input("ID de Empleado: "))

    iris = input("¿El escaneo de Iris coincide con la base de datos? (si/no): ").lower()
    facial = input("¿El reconocimiento facial es mayor al 95%? (si/no): ").lower()

    print("\n> Diagnóstico:")

    # Validación de intruso
    if id_empleado <= 0:
        print("¡ALERTA DE SEGURIDAD! ID inválido detectado. Bloqueando accesos y notificando a la policía.")

    # Acceso Senior
    elif id_empleado < 100 and iris == "si" and facial == "si":
        print(f"Bienvenido, Ingeniero {nombre}. Acceso nivel SENIOR concedido a todas las áreas.")
        print(f"Generando log de entrada para el usuario: {id_empleado}...")

    # Acceso Junior
    elif id_empleado >= 100 and iris == "si" and facial == "si":
        print(f"Bienvenido, Ingeniero {nombre}. Acceso nivel JUNIOR concedido. Áreas de servidores restringidas.")
        print(f"Generando log de entrada para el usuario: {id_empleado}...")

    # Fallo biométrico
    elif iris == "no" or facial == "no":
        print("Error Biométrico: Identidad no verificada al 100%. Por favor, contacte a seguridad.")


# Ejecutar programa
if __name__ == "__main__":
    main()