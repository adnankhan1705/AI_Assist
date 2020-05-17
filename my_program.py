import pyttsx3
import speech_recognition as sr
import datetime
from datetime import date


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
#print(voices)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def checkBirthday():
    if date.day == 17 and date.month == 5:
        speak("Hey Buddy")
        speak("It's your Birth Day")
        speak("Happy Birthday")


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")

    checkBirthday()

    speak("I am Jarvis Sir. Please tell me how may I help you")     

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        r.pause_threshold = 1 
        audio = r.listen(source)
    try:
        print("Recognising....")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    
    except Exception as e:
        print("Say that again Please.....")
        return "None"

    return query

if __name__ == "__main__":
    date=date.today()
    speak("Hi Adnan")
    wishMe()
    while True:
        query = takecommand().lower()
        if "name" in query and "my" in query:
            speak("Your name is Adnan Khan")
        if "name" in query and "your" in query:
            speak("My name is Jarvis")

        if "exit" in query or "out" in query or "close" in query:
            speak("Good Bye Adnan")
            break
        

