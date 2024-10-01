import random
import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
engine.setProperty('volume',1.5)
engine.setProperty('rate',225)
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)



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


def speak(text):
    engine.say(text)
    engine.runAndWait()
    

def play_rock():
    
        
    user_wins = 0 
    computer_wins = 0    
    options = ["rock", "paper", "scissor"]
    speak("Let's began rock paper scissor game")
    while True:
        speak("sir your turn")
        choice = takeCommand().lower()
        if choice in options:
            break
        else:
            speak("sir ,invalid choice")
            
    for i in range (1,5):
        random_number = random.randint(0, 2)
        # rock:0, paper:1 , scissor:2
        computer_pick = options[random_number]
            
        if choice == "rock" and computer_pick == "paper":
            speak("I won this")
            computer_wins += 1
        elif choice == "rock" and computer_pick == "scissor":
            speak("You won this")
            user_wins += 1    
        elif choice == "paper" and computer_pick == "rock":
            speak("You won this")
            user_wins += 1
        elif choice == "paper" and computer_pick == "scissor":
            speak("I won this")
            computer_wins += 1
        elif choice == "scissor" and computer_pick == "paper":
            speak("You won this")
            user_wins += 1
        elif choice == "scissor" and computer_pick == "rock":
            speak("I won this")
            computer_wins += 1
        elif 'close' in choice:
            speak("sure sir closing the game")
            break
speak("my wins are,{computer_wins}")
speak("your wins are,{user_wins}")