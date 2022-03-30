import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import random
import webbrowser
import smtplib
import subprocess

print("Starting .......")

engine = pyttsx3.init("sapi5")
rate = engine.getProperty("rate")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", rate-30)

engine.say("Initializing ......")

# Speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function
def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Hello, Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Hello, Good Afternoon Sir")
    else:
        speak("Hello, Good Evening Sir")

# Microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ......")
        audio = r.listen(source)
    try:
        print("Recognizing ......")
        query = r.recognize_google(audio, language="en-us").lower()
        print(f"User said : {query}\n")
    except Exception as e:
        speak("Please say that again")
        query = takeCommand()
    
    return query

# Main
speak("I'am your virtual assisstant")
greetMe()
for a in range(9999):
    query = takeCommand()
    
    # Logic
    if "wikipedia" in query.lower():
        speak("Searching Wikipedia .... ")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=4)
        print(results)
        speak(results)

    elif "how are you" in query.lower():
        sayhi = ("I'am fine sir, nice to meet you", "Not bad, how about you sir", "very well, and how about you sir", "iam good sir, how about you", "i am great")
        respon = random.choice(sayhi)
        speak(f"{respon}")

    elif "good" in query.lower():
        speak("Thats great")

    elif "who are you" in query.lower():
        speak("I am an artificial intelligence program, which is used to assist users in carrying out daily activities")

    elif "a joke" in query.lower():
        print("8 / 2 is o")
        speak("8 divided 2 is o")

    elif "age" in query.lower():
        age = (7,8,9,10,11,12,13,14,15,16,17,18,18,20,21,22,23,24,25) 
        a = random.choice(age)
        speak(f"Your age is {a}")

    elif "true" in query.lower():
        speak("nice")

    elif "wrong" in query.lower():
        speak("sorry my bad")

    elif "color of the sun"in query.lower():
        speak("color of the sun is yellow")

    elif "google" in query.lower():
        speak("Open Google Chrome")
        subprocess.Popen("path_to_chrome_application")
