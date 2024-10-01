import requests
import json
import pyttsx3
import speech_recognition as sr

# Initialize the speech engine
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

def latestNews():
    api_dict = {
        "normal news": "https://newsapi.org/v2/everything?q=tesla&from=2024-07-17&sortBy=publishedAt&apiKey=52ab01cec87c45e58510d2cf5bfcbcb5",
        "science": "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=52ab01cec87c45e58510d2cf5bfcbcb5",
        "technology": "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=52ab01cec87c45e58510d2cf5bfcbcb5",
        "business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=52ab01cec87c45e58510d2cf5bfcbcb5"
    }

    while True:
        speak("Which field news do you want? [business], [science], [normal news], [technology]")
        field = takeCommand().lower()
        url = api_dict.get(field)
        if url:
            speak("URL found")
            print("URL found")
        elif 'close' in field:
            break
        else:
            speak("URL not found")
            print("URL not found")
            continue

        news = requests.get(url).text
        news = json.loads(news)
        speak("Here is the first news.")
        arts = news["articles"]
        if 1:
            for articles in arts:
                article = articles["title"]
                print(article)
                speak(article)
                news_url = articles["url"]
                speak("For more info, visit the below-mentioned URL")
                print(f"For more info, visit: {news_url}")

                speak("Do you want to stop the news or continue?")
                response = takeCommand().lower()
                if 'stop' in response or 'end' in response:
                    break
            break
        break