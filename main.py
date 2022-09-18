BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

import random  # librería random para el Comodin
import time # Importamos la librería time
comodin = random.randint(2, 4)
puntaje = 0

iniciar_trivia = True  #Variable en True
intentos = 0  # numero de veces que el usuario intenta la trivia.

# texto de bienvenida
print(BLUE+"Bienvenid@ a mi trivia sobre Inteligencia Artificial")
print("Pondré a prueba tus conocimientos con estas 5 preguntas")
nombre = input("Ingresa tu nombre: "+RESET)

while iniciar_trivia == True:

    #  Mientras iniciar_trivia:
    intentos += 1
    puntaje = 0

    print(GREEN+"\nIntento número:", intentos)
    print(
        "\nHola", nombre,
        "cada pregunta tendra un valor de 4 puntos + comodin con multiplicador.\n"
    )
    print(
        "Responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n"
    )
    input("Presiona Enter para continuar"+RESET)
    time.sleep(1) 
    print(MAGENTA+"\nEmpezando la trivia...\n"+RESET)
    time.sleep(1)
    print(
        YELLOW+"1) ¿Cuándo se estableció formalmente el término ‘Inteligencia Artificial?\n"+RESET
    )
    print("a) En 1968, con la película ‘2001: Una odisea en el Espacio’")
    print("b) En 1956, durante la Conferencia de Dartmouth")
    print(
        "c) En 1997, después de una computadora autónoma (Deep Blue) ganase al campeón mundial de ajedrez Gari Kaspárov"
    )
    print("d) En 1971, cuando Ray Tomlinson envío el primer email.")
    respuesta_1 = input("\nTu respuesta: ").lower()

    while respuesta_1 not in ("a", "b", "c", "d"):
        respuesta_1 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

# Verificacion de respuesta
    if respuesta_1 == "b":
        puntaje += 4
        print(BLUE+"\nMuy bien", nombre, "!"+RESET)
    else:
        print(RED+"\nIncorrecto", nombre, "!"+RESET)

    print(nombre, "llevas", puntaje, "puntos")

    # Pregunta 2

    print(YELLOW+"\n2) ¿Cuál es la diferencia entre IA débil e IA fuerte?\n"+RESET)
    print(
        "a) La débil está creada para realizar una tarea concreta. La fuerte es capaz de imitar el procesamiento de la información propio de los seres humanos"
    )
    print(
        "b)  La débil solo lee los labios. La fuerte convierte la voz en texto"
    )
    print(
        "c) La débil busca soluciones simples a problemas. La fuerte indaga más profundamente en el problema y aporta respuestas muy elaboradas para programar robots"
    )
    print("d) Ninguna de las anteriores")

    # Almacenamos la respuesta"
    respuesta_2 = input("\nTu respuesta: ").lower()

    while respuesta_2 not in ("a", "b", "c", "d"):
        respuesta_2 = input(
            "Debes responder a, b, c o d. Ingresa     nuevamente tu respuesta: "
        )

# Verificacion de respuesta
    if respuesta_2 == "b":
        print(RED+"\nIncorrecto!", nombre, "!"+RESET)
    elif respuesta_2 == "c":
        print(RED+"\nIncorrecto!", nombre, "!"+RESET)
    elif respuesta_2 == "d":
        print(RED+"\nIncorrecto!", nombre, "!"+RESET)
    else:
        puntaje += 4
        print(BLUE+"\nMuy bien", nombre, "!"+RESET)

    print(nombre, "llevas", puntaje, "puntos")

    # Pregunta 3

    print(YELLOW+
        "\n3) ¿Qué juego de mesa ha tenido un papel muy importante en el desarrollo de la IA?\n"+RESET
    )
    print("a) Dominó")
    print("b) Ajedrez")
    print("c) Scrabble")
    print("d) Damas")

    
    respuesta_3 = input("\nTu respuesta: ").lower()

    while respuesta_3 not in ("a", "b", "c", "d"):
        respuesta_3 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

    if respuesta_3 == "b":
        puntaje += 4
        print(BLUE+"\nMuy bien", nombre, "!"+RESET)
    else:
        print(RED+"\nIncorrecto", nombre, "!"+RESET)

    print(nombre, "llevas", puntaje, "puntos")

    # Pregunta 4

    print(YELLOW+"\n4) ¿En qué se diferencia un programa informático de una IA?\n"+RESET)
    print(
        "a) Un programa informático es solo una lista de órdenes que le dice al ordenador lo que tiene que hacer."
    )
    print(
        "b) La gran revolución de la IA es que no recibe órdenes para obtener un resultado."
    )
    print(
        "c) Con un programa informático, una máquina no piensa. Simplemente, hace exactamente lo que le dicen."
    )
    print("d) Todas son correctas")
    respuesta_4 = input("\nTu respuesta: ").lower()

    while respuesta_4 not in ("a", "b", "c", "d"):
        respuesta_4 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")


    if respuesta_4 == "d":
        puntaje += 4
        print(BLUE+"\nMuy bien", nombre, "!"+RESET)
    else:
        print(RED+"\nIncorrecto", nombre, "!"+RESET)

    print(nombre, "llevas", puntaje, "puntos")

    # Pregunta 5 comodin

    print(GREEN+"\nPregunta Comodin :)"+RESET)
    print(YELLOW+
        "\n5) Sistemas que piensan como humanos: automatizan actividades como la toma de decisiones, la resolución de problemas y el aprendizaje\n"+RESET
    )
    print("a) Agentes inteligentes")
    print("b) Robots")
    print("c) Redes neuronales artificiales")
    print("d) Sistemas expertos")
    respuesta_5 = input("\nTu respuesta: ").lower()

    while respuesta_5 not in ("a", "b", "c", "d"):
        respuesta_5 = input(
            "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

# Verificamos su respuesta para mandar un mensaje de acierto con multilplicador usando random o de error
    if respuesta_5 == "c":
        puntaje += 2 * comodin
        print(BLUE+"\nMuy bien", nombre, "!"+RESET)
    else:
        print(RED+"\nIncorrecto", nombre, "!"+RESET)
    print(MAGENTA+"\nGracias", nombre, "por jugar mi trivia, alcanzaste", puntaje,
          "puntos sobre 20"+RESET)
    if puntaje >20:
      print(CYAN+"Sacaste mas de 20 eres un GENIO!"+RESET)
    elif puntaje > 10:
      print(CYAN+"Sigue asi lo hiciste muy bien!"+RESET)
    else:
      print(CYAN+"No te rindas! Puedes mejorar :)"+RESET)
      
    print(GREEN+"\n¿Deseas intentar la trivia nuevamente?")
    repetir_trivia = input(
        "Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower(
        )

    if repetir_trivia != "si": 
        print("\nEspero", nombre, "que lo hayas pasado bien, hasta pronto!"+RESET)
        iniciar_trivia = False  
