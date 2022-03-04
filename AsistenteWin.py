import speech_recognition as sr
import pyttsx3
import pyaudio
import pywhatkit
import random
import datetime
import webbrowser
import os
#import telegram_send

listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
#Elegir tipo de voz en --> [] (puede ser 0, 1 (Inglés) o 2)
engine.setProperty('voice', voices[2].id)

#Lista de chistes
chistes = [
    '¿Qué le dice un techo a otro techo?... Techo de menos',
    '¿Qué le dice un gusano a otro?... Me voy a dar una vuelta a la manzana',
    '¿Por qué llora un libro de matemáticas?... ¡Porque tiene muchos problemas!',
    '¿Qué le dice un pez a otro?... ¡Nada!',
    '¿Tienen libros sobre el cansancio?... Sí, pero ahora mismo no hay, ¡están todos agotados!',
    '¿Qué le dice una iguana a su hermana gemela?... Somos iguanitas',
    '¿Qué está al final de todo?... ¡La letra o!',
    '¿Cuál es el baile favorito del tomate?... ¡La salsa!',
    '¿Cómo se dice pañuelo en japonés?... Sacamoko',
    'Papá, ¿hay gelatina?... Pues que yo sepa nada más que existe la ¡i latina! y la ¡y griega!']

#Numeros a mandar mensaje:
Numero1 = "(Numero)"
#Mensajes predefinidos
#Hola = "Hola, este es un mensaje desde el asistente de Marcos"
#Minutos:
#Minutos = datetime.datetime.now().strftime('%M')
#hora:
#Hora = datetime.datetime.now().strftime('%H')
#prueba de hora y minutos:
#print(Hora)

#Navegador Web predeterminado, en este caso Brave
navub = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s"
nav0 = webbrowser.get(navub)
webbrowser.register("Brave", None, nav0)

#Definición de la variable: talk()
def talk(text):
    engine.say(text)
    engine.runAndWait()

#Variable que toma el microfono.
def listen():
    try:
        with sr.Microphone() as source:
            talk('Ya puedo escucharte, habla')
            voice = listener.listen(source)
            #Se puede cambiar el lenguaje en el que se entiende la voz con el comando language="es-AR" (se puede cambiar 'es-AR' por el idioma que prefiera, por ejemplo, 'en-US')
            rec = listener.recognize_google(voice, language="es-AR")
            rec = rec.lower()
            print(rec)
    except:
        pass
    return rec

#Acciones que se realizaran según lo que se escuche
def run():
    #Se puede desmarcar rec='' para realizar las acciones sin necesidad del microfono, si hace esto recuerde marcar con # a rec = listen()
    #rec = 'abrir word'
    rec = listen()
    #Reproducción en YouTube.com
    if 'reproduce' in rec:
        youtube = rec.replace('reproduce', '')
        talk('Reproduciendo '+youtube)
        pywhatkit.playonyt(youtube)
    
    #Hora actual
    elif 'hora' in rec:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        talk('Son las '+hora)

    #Día actual
    elif 'día' in rec:
        #dia = datetime.now().strftime('%d, %m, %H, %M')
        dia = datetime.datetime.now().strftime('%d')
        mes = datetime.datetime.now().strftime('%m')
        año = datetime.datetime.now().strftime('%Y')
        hora = datetime.datetime.now().strftime('%I:%M %p')
        talk(f" Hoy es {dia} de {mes} del {año} y son las "+hora)

    #Chistes (Recordar que se pueden cambiar en: #Lista de chistes --> chistes = [])
    elif 'chiste' in rec:
        talk(random.choice(chistes))

    #Buscar en Google
    elif 'buscar' in rec:
        busca = rec.replace('buscar', '')
        talk ('Buscando '+busca)
        pywhatkit.search(busca)
    
    #Enviar mensajes (A mi mismo)
    elif 'enviarme' in rec:
        ordenMsj = rec.replace('enviarme', '')
        talk('Estoy enviandote el mensaje')
        #Nota: Quitar # del comando que prefiera usar y agregar al que no. 
        #Envio con horario especifico:
        #pywhatkit.sendwhatmsg(f"+54{Numero1}", ordenMsj, 2, 22, 20, True)
        #Envio instantaneo:
        pywhatkit.sendwhatmsg_instantly(f"+541123176699", ordenMsj, 20)

    #Mensaje a contacto especifico
    elif 'enviar' in rec:
        #Mensaje a mamá XD
        if 'mamá' in rec:
            ordenMsj = rec.replace('enviar mensaje a mamá', '')
            talk('Enviando mensaje a mamá')
            #pywhatkit.sendwhatmsg_instantly(f"+541169574483", ordenMsj, 20)
        else:
            #Respuesta si no encuentra al contacto que dijo
            talk('Lo siento, no esta en mis contacto')

    #Información sobre un tema
    elif 'información' in rec:
        info = rec.replace('información sobre', '')
        talk('Abajo tienes información sobre '+info)
        pywhatkit.info(info)

    #Convertir imagen a ASCII art
    elif 'convertir' in rec:
        talk('Estoy haciendo arte... ahora te muestro')
        pywhatkit.image_to_ascii_art(r"D:/Asistente Win/img.png")
    
    #Abrir Twitch.tv a traves de URL
    elif 'twitch' in rec:
        talk ('Abriendo Twitch')
        webbrowser.get("Brave").open('twitch.tv', new= 1, autoraise=True)
    
    elif 'tarea' in rec:

        #Abrir Moodle a traves de URL
        if 'plataforma' in rec:
            print('Abriendo plataforma de la escuela')
            webbrowser.get("Brave").open('eest1moodle.duckdns.org/my/', new= 1, autoraise= True)
    
        #Abrir carpeta de tarea
        elif 'carpeta' in rec:
            print('Buscando la carpeta de tareas')
            direccion = "C:/Users/alumno/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/"
            os.system(direccion + 'TPs Cole.lnk')

    #Abrir nube de archivos TeraBox
    elif 'nube' in rec:
        talk ('Abriendo la nube')
        webbrowser.get("Brave").open('terabox.com/disk/home#/all?path=%2F&vmode=list', new= 1, autoraise=True)

    #Abrir configuración del Internet con IP
    elif 'ip' in rec:
        talk('Abriendo configuración con IP')
        webbrowser.get("Brave").open('192.168.1.1', new= 1, autoraise=True)

    #Mensajes por Telegram (no encontre una API que funciones bien)
    #elif 'telegram' in rec:
        #talk('Eviando mensaje')
    
    #Escribir a mano un texto, en este caso lo que dijimos (fallo al abrir la imagen \_(°-°)_/)
    #elif 'escribir' in rec:
        #escribir = rec.replace('escribir', '')
        #talk('Estoy copiando, espere')
        #pywhatkit.text_to_handwriting(escribir)

    #Abrir Spotify, o un programa
    elif 'spotify' in rec:
        talk('Abriendo Spotify')
        direccion = "C:/Users/alumno/AppData/Roaming/Spotify/"
        os.system(direccion + 'Spotify.exe')

    #Abrir Word
    elif 'word' in rec:
        talk('Abriendo Word')
        direccion = "C:/Program Files/Microsoft Office/root/Office16/"
        os.system(direccion + 'WINWORD.EXE')

    #Abrir Paint
    elif 'Pintar' in rec:
        talk('Abriendo Paint')
        direccion = "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Accessories/"
        os.system(direccion + "Paint.lnk")


    #Abir Gimp
    elif 'editar' in rec:
        talk('Abriendo GIMP')
        direccion = "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/"
        os.system(direccion + 'GIMP 2.10.20.lnk')

    #Abrir programas de programación
    elif 'programar' in rec:
        talk('Espero que me mejores...')
        #IDE Web Replit.com
        if 'web' in rec:
            talk('Abriendo Replit.io')
            webbrowser.get("Brave").open('replit.com', new= 1, autoreise=True)
        #VS Code
        elif 'visual' in rec:
            talk('Abriendo Visual Studio')
            direccion = "C:/Users/alumno/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Visual Studio Code/"
            os.system(direccion + 'Visual Studio Code.lnk')

        #IDE Android Studio
        elif 'android' in rec:
            talk('Abriendo Android Studio')
            direccion = "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Android Studio/"
            os.system(direccion + 'Android Studio.lnk')

        #DFD
        elif 'boceto' in rec:
            talk('Abriendo DFD')
            direccion = "C:/Users/alumno/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/"
            os.system(direccion + 'dfd.lnk')

        else:
            talk('No se que programa es ese, pero puedes seguir programandome a mí')

    #Abrir juegos
    elif 'jugar' in rec:

        #Move or Die
        if 'primer' in rec:
            direccion = "C:/Users/alumno/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Steam/"
            print('Abriendo Move or Die')
            os.system(direccion + "Move or die.url")
        
        #Don't Strave Together
        elif 'robot' in rec:
            direccion = "C:/Users/alumno/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Steam/"
            print("Abriendo Don't Strave Together")
            os.system(direccion + "Don't Strave Together.url")
        
        #Minecraft
        elif 'minecraft' in rec:
            direccion = "C:/Users/alumno/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/"
            print("Abriendo Minecraft")
            os.system(direccion + 'LauncherFenix-Minecraft-6.lnk')
        
        #Steam
        else:
            direccion = "C:/Users/alumno/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Steam/"
            print('Abriendo Steam')
            os.system(direccion + 'Steam.lnk')

    #Saludo
    elif 'hola' in rec:
        talk ('Hola, mucho gusto. ¿En que puedo ayudarte?')

    #Respuesta a ¿Cómo estás?
    elif 'estás' in rec:
        talk ('Estoy bien, con ganas de ayudar')

    #Despedida
    elif 'chau' in rec:
        talk ('Adios. Espero haber sido de ayuda')
    
    #Respuesta a ¿Qué eres?
    elif 'eres' in rec:
        talk ('Soy un asistente virtual hecho por Marcos (mi programador)')

    #Nombre (Forma 1)
    elif 'llamas' in rec:
        talk ('Todavía Marcos no elige un nombre para mí así que puedes decirme como te guste hasta que se le ocurra algo')

    #Nombre (Forma 2)
    elif 'nombre' in rec:
        talk ('Todavía Marcos no elige un nombre para mí así que puedes decirme como te guste hasta que se le ocurra algo')

    #Calculadora


    #Respuesta, predefinida, en caso de no encontrar ninguna de las acciones anteriores
    else:
        talk('Parece que deben de seguir programandome. Dime otra cosa, lo siento')
run()