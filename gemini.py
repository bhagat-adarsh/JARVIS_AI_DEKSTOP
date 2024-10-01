from dotenv import load_dotenv
load_dotenv()

import os
import google.generativeai as genai
import keyboard
import pyttsx3
engine = pyttsx3.init('sapi5')
engine.setProperty('volume',1.5)
engine.setProperty('rate',225)
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
 
                                              

genai.configure(api_key=os.getenv("API_KEY"))

#loading gmini pro
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def gemini_response(question):
    response = chat.send_message(question)
    final_answer = response.text
    
    print(final_answer)
    sentences = final_answer.split(". ")
    summary = sentences[0] + "."
    print("Summary:")
    print(summary)
    speak("Here's a summary:")
    speak(summary)
    speak("do you want to save it.")
    n=input("Enter")
    if n.lower()=="y":
        file = open("prompt", "w")
        file.write(final_answer)
        file.close()