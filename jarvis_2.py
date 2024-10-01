import pyttsx3
import speech_recognition as sr
import pyautogui
import datetime
from conv import random_text
import keyboard
import os 
import tkinter as tk
import subprocess as sp
import webbrowser
import wikipedia
import smtplib
from online import find_my_ip,search_on_gooogle,youtube,bing_ai,black_box_ai
from intro import play_gif
from gemini import gemini_response


import google.generativeai as genai

engine = pyttsx3.init('sapi5')
engine.setProperty('volume',1.5)
engine.setProperty('rate',225)
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

USER = "ADARSH"
BOT = "JARVIS"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning sir")

    elif hour >=12 and hour <= 16:
        speak("Good Afternoon sir")

    else:
        speak("Good Evening sir")

    speak("I am Jarvis. Please tell me how may I help you today")
   
    #speak("I am JARVIS , your personal AI assistant. How can I assist you today? Whether you need information, reminders, or just a bit of entertainment, I amm here to help. Please let me know your request, and I will do my best to assist you promptly and efficiently. Lets make today productive and enjoyable")

listening = True
def start_listening():
    global listening
    listening = True
    print("Started listening")
    
def pause_listening():
    global listening
    listening = False
    print("Stopped listening")
    speak("Stopped listening")
def pause():
    pyautogui.hotkey('k')
    speak("paused sir")
def close_tab():
    pyautogui.hotkey('ctrl', 'w')
    speak("Tab closed")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold 
        audio = r.listen(source)
    try :
        print("Recognizing....")
        query = r.recognize_google(audio, language ="en-in")
        print(f"Bhagat said: {query}\n")
    
    except Exception as e:
        print(e)
        print("Say that again") 
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls
    server.login('jarviswa82@gmail.com','1qaz2wsx3edc..?')
    #file me email or password likh,  woh bhi jarvis se
    server.sendmail('adarshbhagat171@gmail.com',to,content)
    server.close()

i=0
if __name__ =="__main__":  
    wishMe()
    keyboard.add_hotkey('ctrl + shift',start_listening)
    while True:
        
        if listening:    
        #keyboard.add_hotkey('ctrl + tab',pause_listening) 
            query = takeCommand().lower()
            if 'how are you' in query:
                speak("I am all good sir. What about you")   
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
                
                speak("what would you like to play on Youtube")
                video = takeCommand().lower()
                youtube(video)     
            elif 'sleep' in query:
                speak("This was my lovely time call me whenever you will need me ")
                pause_listening()     
            elif 'wikipedia' in query:
                speak(random_text)
                speak("Searching Wikipedia......")
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query,sentences=4)
                speak("According to wikipedia")
                print(results)
                speak(results)
            elif 'copilot ai' in query:
                speak(random_text)
                webbrowser.open("bing.ai")
                speak("opening microsoft ai for you")
            elif 'close' in query:
                pyautogui.press("alt","F4")
            elif 'news' in query:
                from newsRead import latestNews
                latestNews() 
                
            elif 'jarvis open'in query:
                query = query.replace("open","")
                query = query.replace("jarvis","")  
                query = query.replace("please","")
                pyautogui.press("super")
                pyautogui.typewrite(query)
                pyautogui.press("enter")
            elif 'switch to open ai' in query:
                speak("Switching to openai mode,sir")
                print("Switching to openai mode,sir")
                speak("Ready sir")
                print("Ready sir")
                while True:
                    quert = takeCommand().lower()
                    print("Listening....")
                    if 'exit' in quert: 
                        speak("Processisng that")
                        break
                    else:
                        gemini_response(quert)
                        
                                                
            elif 'thank you' in query:
                speak("mention not sir")
            elif 'open whatsapp' in query:
                speak(random_text)
                #webbrowser.open("web.whatsapp.com")
                speak("WhatsApp is now opening")
                try:
                   from Whatsaap import sendMessage
                   sendMessage()
                except Exception as e:
                    speak("Unable to send message")
                    speak(e)
                    print(e)
            elif 'let us play' in query:
                from rock_paper import play_rock
                speak("lets play rock paper scissor")
                play_rock()
            elif 'screenshot' in query:
                im = pyautogui.screenshot()
                speak("in what name should i save it")
                im.save("ss.jpg")
            elif 'shutdown the system' in query:
                os.system("shutdown /s /t 1")           
            elif 'pause' in query:
                pyautogui.press("k")
                speak("vedio paused")
            
            elif 'play' in query:
                pyautogui.press("k")
                speak("vedio played")    
            elif 'mute in query' in query:
                pyautogui.press("m")
                speak("vedio muted")
            
            elif 'volume up' in query:
                from keyboard_1 import volumeUp
                speak("Turning volume up, sir")
                volumeUp()
            
            elif 'volume down' in query:
                from keyboard_1 import volumeDown
                speak("Turning volume down, sir")
                volumeDown()
                
            
            elif 'close tab' in query:
                close_tab() 
                        
            elif 'open google' in query:
                webbrowser.open("google.com")
                
                speak("What would you like to search on google Adarsh")
                query = takeCommand().lower()
                search_on_gooogle(query)
                    
                                    
            elif 'stack overflow' in query:
                speak(random_text)
                webbrowser.open("stackoverflow.com")
            elif 'rohit sharma' in query:
                speak("Badam khaye,  Eat almonds dimag ki shakti badhaye, should eat almonds to do so rest his such habbit is funny, that is what made him shaanaa ")
            elif 'chess' in query :
                speak(random_text)
                webbrowser.open("chess.com")
            elif 'black box ai' in query:
                speak(random_text)
                webbrowser.open("blackbox.ai")
                speak("opening black box ai")
                
            
            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M")
                speak(f"Sir, the time is{strTime}")
                
            elif 'send email' in query:
                speak(random_text)
                try:
                    speak("What should I say")
                    content = takeCommand()
                    to = "adarshbhagat171@gmail.com"
                    sendEmail(to,content)
                    speak("Email has been sent")
                except Exception as e:
                    print(e)
                    speak("sorry i am unable to send that email") 
                    quer = takeCommand().lower()
                    if 'what is the problem in email' in quer:
                        speak(e)
            
            elif 'open command prompt' in query:
                speak(random_text)
                speak("Opening command prompt")
                os.system('start cmd')
                        
            #Add karo jo bhi khulwana hai
                    
            elif 'ip address' in query:
                ip_address = find_my_ip() 
                speak(
                    f"your ip address is{ip_address}"
                    )
                print(f"your ip address is{ip_address}")
                    