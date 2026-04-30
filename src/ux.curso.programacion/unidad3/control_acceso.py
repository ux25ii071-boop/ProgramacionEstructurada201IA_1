class ControlAcceso:
    def __init__(self):
        self.usuarios_autorizados = {
            "2024001": "Investigador",
            "2024002": "Estudiante",
            "2024003": "Administrador"
        }

    def verificar_permisos(self, matricula):
        if matricula in self.usuarios_autorizados:
            rol = self.usuarios_autorizados[matricula]
            print(f"[ACCESO CONCEDIDO] Bienvenido, rol detectado: {rol}.")
            return rol
        else:
            print("[ACCESO DENEGADO] Usuario no registrado en la base de datos de IA.")
            return None


def main():
    print("--- Sistema de Seguridad Laboratorio IA - UX ---\n")

    sistema = ControlAcceso()

    while True:
        try:
            matricula = input("Ingrese su matrícula: ")

            if matricula == "":
                raise ValueError("Entrada vacía")

            rol = sistema.verificar_permisos(matricula)

            # Funcionalidad extra (solo si es admin)
            if rol == "Administrador":
                opcion = input("¿Desea agregar un nuevo usuario? (s/n): ")
                if opcion.lower() == "s":
                    nueva_mat = input("Nueva matrícula: ")
                    nuevo_rol = input("Rol: ")
                    sistema.usuarios_autorizados[nueva_mat] = nuevo_rol
                    print("Usuario agregado correctamente.")

        except ValueError:
            print("[ERROR] Debe ingresar una matrícula válida.")

        finally:
            print("--- Intento de acceso registrado en el log del servidor ---\n")


if __name__ == "__main__":
    main()