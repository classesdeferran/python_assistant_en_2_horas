import speech_recognition as sr
import pyttsx3
import datetime

nombre_asistente = "Axela"


# Función para que escuche la máquina
def audio_pc():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        # demora para dar tiempo a activar el hardware
        r.pause_threshold = 0.5 # entre 0.5 y 0.8

        # mensaje pra saber que podemos empezar a hablar
        print("Esperando ...")

        # guardar el audio
        audio = r.listen(source)

        try :

            text = r.recognize_google(audio, language="es")

            print("Has dicho ...", text)

            return text
        
        except:
            print("No te he podido entender")

# audio_pc()

# Función para que hable el PC
def respuesta_PC(texto):

    try:

        engine = pyttsx3.init()

        # Ajustes de la salida
        engine.setProperty("rate", 150)

        engine.setProperty("volume", 1)

        # preparar la respuesta
        engine.say(texto)

        # que se quede a la espera
        engine.runAndWait()

    except:
        print("error en el texto")

# Comprobación 
# respuesta_PC("Hola, día sábado")

def decir_dia_semana ():
    # obtener el dia
    dia = datetime.date.today()
    # print(dia.weekday())

    nombres_dias = {
        0 : "lunes",
        1 : "maertes",
        2 : "miércoles",
        3 : "jueves",
        4 : "viernes",
        5 : "sábado",
        6 : "domingo"
    }

    respuesta_PC(f"Hoy es {nombres_dias[dia.weekday()]}")

def decir_hora():

    # variable para la hora
    hora = datetime.datetime.now()
    # print(hora)

    mensaje = f"Son las {hora.hour} horas, {hora.minute} minutos y {hora.second} segundos"

    respuesta_PC(mensaje)

# decir_hora()

def saludo_inicial():
    
    # hora para establecer el saludo
    hora = datetime.datetime.now()

    if 6 <= hora.hour < 14:
        ahora = "Buenos días"
    elif 14 <= hora.hour < 20:
        ahora = "Buenos tardes"
    else:
        ahora = "Buenas noches"

    respuesta = f"{ahora}, soy {nombre_asistente}. ¿En qué puedo ayudarte?"
    respuesta_PC(respuesta)

saludo_inicial()