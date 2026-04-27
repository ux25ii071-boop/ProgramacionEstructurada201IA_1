# Agente básico de preguntas sobre programación

def limpiar_texto(texto):
    return texto.lower().strip()


def obtener_conocimientos():
    return {
        # Estructuras de control
        "if": "La sentencia if es un condicional. Permite tomar decisiones basadas en una condición booleana.",
        "for": "El bucle for se usa para recorrer secuencias como listas o cadenas y ejecutar código varias veces.",
        "while": "El bucle while ejecuta código mientras una condición sea verdadera.",

        # Tipos de datos
        "int": "Representa números enteros sin decimales.",
        "float": "Representa números con decimales.",
        "str": "Representa texto o cadenas de caracteres.",

        # Funciones
        "def": "Se usa para definir funciones en Python.",
        "print": "Muestra información en la consola.",
        "return": "Devuelve el resultado de una función.",

        # Programación estructurada
        "programacion estructurada": "Organiza el código en bloques usando condicionales, bucles y funciones.",
        "secuencia": "Las instrucciones se ejecutan en orden.",
        "seleccion": "Permite elegir entre diferentes caminos según una condición.",
        "iteracion": "Permite repetir un bloque de código varias veces."
    }


def procesar_pregunta(mensaje_usuario):
    mensaje = limpiar_texto(mensaje_usuario)
    base = obtener_conocimientos()

    for clave, valor in base.items():
        if clave in mensaje:
            return valor

    return "No entiendo la pregunta."


def main():
    print("Asistente de programación activo. Escribe 'salir' para terminar.")

    while True:
        entrada = input("Pregunta: ")

        if limpiar_texto(entrada) == "salir":
            print("Programa finalizado.")
            break

        respuesta = procesar_pregunta(entrada)
        print("Respuesta:", respuesta)


if __name__ == "__main__":
    main()