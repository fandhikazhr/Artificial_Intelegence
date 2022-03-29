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
