import speech_recognition as sr
import os

def ouvir_mic():

    mic = sr.Recognizer()

    with sr.Microphone() as source:

        mic.adjust_for_ambient_noise(source)
        print("Pode falar!")
        audio = mic.listen(source)

    try:
         frase = mic.recognize_google(audio,language='pt-br')
         print("Você disse: " + frase)

         if "desenhar" in frase:
            os.system("start mspaint.exe")

    except sr.UnkownValueError:
        print("Não entendi!")

    return frase

ouvir_mic()