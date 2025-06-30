import speech_recognition as sr
import pyttsx3


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

        # preparar la respuesta
        engine.say(texto)

        # que se quede a la espera
        engine.runAndWait()

    except:
        print("error en el texto")

respuesta_PC("Hola, día sábado")