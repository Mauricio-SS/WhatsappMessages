#importamos la librería 
import pywhatkit 

#escribimos nuestro mensaje dentro de las comillas
msg = " "

#usamos un try-except 
try: 
    #enviamos el mensaje 
    pywhatkit.sendwhatmsg("",msg,,)

    print("Mensaje enviado")
except: 

    print("Ocurrio un error")