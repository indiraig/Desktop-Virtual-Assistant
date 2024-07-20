import os
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
dictapp =   {"commandprompt":"cmd","paint":"paint","word":"winword","excel":"excel","chrome":"chrome","vscode":"code","powerpoint":"powerpnt"}

def openappweb(text):
    text = text.replace("open", "")
    text = text.replace("inertia", "")
    pyautogui.press("super")
    pyautogui.typewrite(text)
    pyautogui.sleep(2)
    pyautogui.press("enter")