
import unicodedata
import json
print("EJECUTANDO EL ARCHIVO CORRECTO")
print("VERSION: 2")
# Proyecto: AI-Py - Mi primer asistente inteligente

print("=" * 40)
print("   AI-Py: MI ASISTENTE INTELIGENTE")
print("=" * 40)
print("¡Hola! Soy AI-Py.")
print("Escribe 'salir' para terminar la conversacion.")


# Funcion para normalizar el texto
def normalizar(texto):
    texto = texto.lower().strip()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(
        letra for letra in texto
        if unicodedata.category(letra) != "Mn"
    )
    return texto


# Base de conocimientos de AI-Py
conocimientos = {
    "python": "Python es un lenguaje de programacion.",
    "html": "HTML es un lenguaje de marcado utilizado "
            "para crear la estructura de paginas web.",
    "cpu": "CPU significa Unidad Central de Procesamiento. "
           "Es el componente que ejecuta instrucciones.",
    "ram": "RAM es la memoria temporal que utiliza "
           "la computadora mientras ejecuta programas.",
    "ia": "IA significa Inteligencia Artificial. "
          "Permite que las maquinas realicen tareas "
          "que normalmente requieren inteligencia humana.",
    "algoritmo": "Un algoritmo es un conjunto ordenado "
                  "de pasos para resolver un problema.",
    "variable": "Una variable es un espacio donde "
                "se almacena un dato en un programa.",
    "html y css": "HTML define la estructura de una pagina "
                   "web y CSS controla su apariencia."
}

# Cargar conocimientos guardados
try:
    with open("conocimientos.json", "r", encoding="utf-8") as archivo:
        conocimientos_guardados = json.load(archivo)
        if isinstance(conocimientos_guardados, dict):
            conocimientos.update(conocimientos_guardados)

except FileNotFoundError:
    pass

except (json.JSONDecodeError, OSError):
    print("AI-Py: No se pudieron cargar los conocimientos guardados.")


# Funcion para guardar conocimientos
def guardar_conocimientos():
    with open("conocimientos.json", "w", encoding="utf-8") as archivo:
        json.dump(
            conocimientos,
            archivo,
            ensure_ascii=False,
            indent=4
        )

# Funcion para realizar calculos
def calcular(operacion):
    partes = operacion.split()

    if len(partes) != 3:
        return "Escribe la operacion asi: 25 * 8"

    try:
        numero1 = float(partes[0])
        operador = partes[1]
        numero2 = float(partes[2])
    except ValueError:
        return "Por favor, utiliza numeros validos."

    if operador == "+":
        respuesta = numero1 + numero2
    elif operador == "-":
        respuesta = numero1 - numero2
    elif operador in ("*", "x", "×"):
        respuesta = numero1 * numero2
    elif operador == "/":
        if numero2 == 0:
            return "No se puede dividir entre cero."
        respuesta = numero1 / numero2
    else:
        return "Operador no valido. Utiliza +, -, * o /."

    if respuesta.is_integer():
        respuesta = int(respuesta)

    return f"El resultado es {respuesta}."


# Preguntas del juego
preguntas_juego = [
    {
        "pregunta": "¿Que lenguaje estamos utilizando?",
        "respuesta": "python"
    },
    {
        "pregunta": "¿Que componente ejecuta las instrucciones?",
        "respuesta": "cpu"
    },
    {
        "pregunta": "¿Como se llama la memoria temporal de la computadora?",
        "respuesta": "ram"
    },
    {
        "pregunta": "¿Que significa IA?",
        "respuesta": "inteligencia artificial"
    },
    {
        "pregunta": "¿Que lenguaje define la estructura de una pagina web?",
        "respuesta": "html"
    }
]


# Funcion para iniciar el juego
def jugar():
    puntaje = 0

    print("\nAI-Py: ¡Comienza el juego de informatica!")
    print("Responde las siguientes preguntas.\n")

    for pregunta in preguntas_juego:
        print(pregunta["pregunta"])
        respuesta_usuario = normalizar(input("Tu respuesta: "))

        if respuesta_usuario == pregunta["respuesta"]:
            print("¡Correcto!")
            puntaje += 1
        else:
            print("Respuesta incorrecta.")
            print("Respuesta correcta:", pregunta["respuesta"])

    print("\nAI-Py: ¡Terminaste el juego!")
    print("Tu puntaje fue:", puntaje, "de", len(preguntas_juego))



# Funcion para reconocer el estado de animo
def detectar_animo(texto):
    emociones = {
        "feliz": [
            "feliz",
            "contento",
            "contenta",
            "alegre",
            "me siento bien",
            "estoy de buen humor"
        ],
        "triste": [
            "triste",
            "desanimado",
            "desanimada",
            "me siento mal",
            "deprimido",
            "deprimida"
        ],
        "cansada": [
            "cansado",
            "cansada",
            "tengo sueño",
            "agotado",
            "agotada",
            "estoy sin energia"
        ],
        "enojada": [
            "enojado",
            "enojada",
            "molesto",
            "molesta",
            "enfadado",
            "enfadada"
        ]
    }

    for emocion, palabras in emociones.items():
        for palabra in palabras:
            if palabra in texto:
                return emocion

    return None




# Funcion para aprender nuevas respuestas
def aprender():
    pregunta_nueva = normalizar(
        input("AI-Py: ¿Que pregunta quieres enseñarme? ")
    )

    if not pregunta_nueva:
        print("AI-Py: La pregunta no puede estar vacia.")
        return

    respuesta_nueva = input(
        "AI-Py: ¿Cual es la respuesta correcta? "
    ).strip()

    if not respuesta_nueva:
        print("AI-Py: La respuesta no puede estar vacia.")
        return

    conocimientos[pregunta_nueva] = respuesta_nueva

    try:
        guardar_conocimientos()
        print("AI-Py: ¡He aprendido y guardado una nueva respuesta!")
    except OSError:
        print("AI-Py: Aprendi la respuesta, pero no pude guardarla.")


# Estado del asistente
modo_profesor = False

# Conversacion principal
while True:
    pregunta = input("\nUsuario: ")
    texto = normalizar(pregunta)

    if not texto:
        print("AI-Py: Escribe algo para que pueda responderte.")
        continue

    if texto == "salir":
        print("AI-Py: ¡Hasta pronto! Gracias por conversar.")
        break

    elif texto in ("ayuda animo", "emociones"):
        print("AI-Py: Puedo reconocer estos estados de animo:")
        print("- Feliz: feliz, contento, alegre")
        print("- Triste: triste, desanimado, me siento mal")
        print("- Cansancio: cansado, tengo sueño, agotado")
        print("- Enojo: enojado, molesto, enfadado")
        print("No necesitas activar un modo especial.")

    elif texto == "modo profesor":
        modo_profesor = True
        print("AI-Py: Modo profesor activado. ¡Vamos a aprender!")

    elif texto == "modo normal":
        modo_profesor = False
        print("AI-Py: Modo normal activado.")
        
    elif texto == "jugar":
        jugar()
        
    elif texto == "aprender":
        aprender()


    elif detectar_animo(texto) == "feliz":
        print("AI-Py: ¡Me alegra que te sientas asi!")

    elif detectar_animo(texto) == "triste":
        print("AI-Py: Lo siento. Espero que pronto te sientas mejor. ¡Estoy aqui para escucharte!")

    elif detectar_animo(texto) == "cansada":
        print("AI-Py: Parece que necesitas descansar un poco. ¡Cuidate!")

    elif detectar_animo(texto) == "enojada":
        print("AI-Py: Entiendo. A veces necesitamos un momento para calmarnos.")

    elif "hola" in texto:
        print("AI-Py: ¡Hola! ¿En que puedo ayudarte?")

    elif "como estas" in texto or "que tal estas" in texto:
        print("AI-Py: ¡Estoy listo para ayudarte! ¿Y tu?")

    elif texto.startswith("calcula"):
        operacion = texto[len("calcula"):].strip()
        print("AI-Py:", calcular(operacion))

    

    elif any(
        frase in texto
        for frase in ["explicame", "explica", "que es", "que significa"]
    ):
        concepto = texto

        for frase in ["explicame", "explica", "que es", "que significa"]:
            concepto = concepto.replace(frase, "")

        concepto = concepto.strip(" ?¿.")

        for articulo in ["el ", "la ", "un ", "una "]:
            if concepto.startswith(articulo):
                concepto = concepto[len(articulo):]

        if concepto in conocimientos:
            print("AI-Py, modo profesor:")
            print(conocimientos[concepto])
        else:
            print("AI-Py: Todavia no conozco ese concepto.")

    
    elif any(
        concepto in texto or texto in concepto
        for concepto in conocimientos
        if len(texto) >= 3
    ):
        concepto_encontrado = next(
            concepto for concepto in conocimientos
            if len(texto) >= 3
            and (concepto in texto or texto in concepto)
        )

        if modo_profesor:
            print("AI-Py, modo profesor:")
        else:
            print("AI-Py:")

        print(conocimientos[concepto_encontrado])


    elif any(operador in texto for operador in ["+", "-", "*", "/", "×"]):
        print("AI-Py:", calcular(texto))

    elif "gracias" in texto:
        print("AI-Py: ¡De nada! Estoy aqui para ayudarte.")

    else:
        print(
            "AI-Py: Todavia no conozco esa pregunta. "
            "Pronto aprendere nuevas respuestas."
        )
