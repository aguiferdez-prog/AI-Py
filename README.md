
# AI-Py — Mi primer asistente inteligente

AI-Py es un asistente conversacional desarrollado en Python como proyecto académico. Permite interactuar mediante texto, realizar cálculos, consultar una base de conocimientos, aprender nuevas respuestas y jugar con preguntas de informática.

## Funcionalidades

- **Conversación:** interacción mediante texto y respuestas a palabras clave.
- **Calculadora:** resolución de operaciones matemáticas básicas.
- **Base de conocimientos:** consulta de conceptos informáticos.
- **Modo profesor:** explicación de conceptos de informática.
- **Modo de aprendizaje:** incorporación y almacenamiento de nuevas respuestas mediante JSON.
- **Modo juego:** preguntas de informática con cálculo de puntuación.
- **Detector básico de estado de ánimo:** reconocimiento de expresiones mediante palabras clave.

## Tecnologías utilizadas

- Python
- JSON
- Visual Studio Code

## Requisitos

- Python 3 instalado.

## Cómo ejecutar el proyecto

1. Descarga o clona este repositorio.
2. Abre la carpeta del proyecto en Visual Studio Code.
3. Ejecuta en la terminal:

```bash
python ai_py.py
```

En Windows también puedes probar:

```bash
py ai_py.py
```

## Cómo interactuar con AI-Py

AI-Py reconoce un conjunto limitado de comandos, palabras clave y frases. Para probarlo, utiliza los siguientes ejemplos.

| Comando o entrada | Función |
|---|---|
| `hola` | Saluda e inicia la interacción. |
| `modo profesor` | Activa el modo profesor. |
| `modo normal` | Desactiva el modo profesor. |
| `ram` | Consulta la definición de RAM. |
| `explica python` | Solicita una explicación de Python. |
| `calcula 25 * 8` | Realiza una operación matemática. |
| `25 * 8` | También permite ingresar una operación directamente. |
| `aprender` | Permite agregar una pregunta y su respuesta. |
| `jugar` | Inicia el juego de informática. |
| `ayuda animo` o `emociones` | Muestra ejemplos de expresiones reconocidas por el detector de ánimo. |
| `salir` | Finaliza la conversación. |

### Ejemplo de uso

```text
Usuario: hola
AI-Py: ¡Hola! ¿En qué puedo ayudarte?

Usuario: modo profesor
AI-Py: Modo profesor activado. ¡Vamos a aprender!

Usuario: ram
AI-Py, modo profesor:
RAM es la memoria temporal que utiliza la computadora mientras ejecuta programas.
```

### Detector básico de estado de ánimo

El asistente reconoce determinadas palabras y expresiones relacionadas con cuatro estados:

- **Feliz:** feliz, contento, alegre.
- **Triste:** triste, desanimado, me siento mal.
- **Cansancio:** cansado, tengo sueño, agotado.
- **Enojo:** enojado, molesto, enfadado.

No es necesario activar un modo especial. El asistente analiza cada mensaje automáticamente.

**Limitación:** el detector utiliza coincidencias de texto y frases predefinidas. No utiliza un modelo de inteligencia artificial entrenado para interpretar emociones.

## Objetivo del proyecto

Aplicar conocimientos de programación en Python mediante el desarrollo de un asistente interactivo que integre lógica condicional, funciones, manejo de texto, estructuras de datos y almacenamiento de información en archivos JSON.

## Autor

Proyecto académico desarrollado como parte del aprendizaje de programación en Python.
