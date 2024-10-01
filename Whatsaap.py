import pywhatkit
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
from bs4 import BeautifulSoup
from time import sleep
import os
from datetime import timedelta
from datetime import datetime

engine = pyttsx3.init('sapi5')
engine.setProperty('volume', 1.5)
engine.setProperty('rate', 225)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language="en-in")
        print(f"Bhagat said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again")
        return "None"
    return query

strTime = int(datetime.now().strftime('%H'))
update = int((datetime.now()+timedelta(minutes=2)).strftime('%M'))


def sendMessage():
    #speak("Sir , whom do you want to message")
    speak("what message do you want to send")
    messag = takeCommand().lower()
    pywhatkit.sendwhatmsg("+919832947974",messag,time_hour = strTime,time_min = update)
    speak("message sent ")
    sleep(1)
    