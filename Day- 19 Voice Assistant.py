import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime

#Initialize Voice Engine
engine = pyttsx3.init()

def speak(Text):
    engine.say(Text)
    engine.runAndWait()

def take_commands():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except Exception:
        print("Sorry, please say that again.")
        return ""

def wish_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning \nI am Your Virtual Assistant")
    elif hour < 18:
        speak("Good Afternoon \nI am Your Virtual Assistant")
    else:
        speak("Good Evening \nI am Your Virtual Assistant")
wish_user()

while True:
    commands = take_commands()
    if "Open linkedin" in commands:
        linkedin.open("https://www.linkedin.com/feed/")
    elif "open youtube" in commands:
        webbrowser.open("https://www.youtube.com")
    elif "open google" in commands:
        webbrowser.open("https://www.google.com")
    elif "who is" in commands:
        person = commands.replace("who is", "")
        info = wikipedia.summary(commands,2)
        print(info)
        speak(info)
    elif "exit" in commands:
        speak("Goodbye")
        break
    

        
    
