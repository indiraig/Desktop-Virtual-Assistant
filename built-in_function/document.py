import warnings
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import datetime
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup
from playsound import playsound
import calendar
import random
import pyautogui
import wikipedia
import  webbrowser
import ctypes
import winshell
import subprocess
import pyjokes
import smtplib
import requests
import json
from selenium import webdriver
import time

from time import sleep
import wolframalpha

warnings.filterwarnings("ignore")
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def talk(audio):
    engine.say(audio)
    engine.runAndWait()


def rec_audio():
    recog = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        audio = recog.listen(source)

    data = " "
    try:
        data = recog.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Assistant could not understand the audio")
    except sr.RequestError as ex:
        print("Request Error from Google Speech Recognition" + ex)

    return  data

def response(text):
    print(text)
    tts = gTTS(text=text, lang="en")
    audio = "Audio.mp3"
    tts.save(audio)
    playsound.playsound(audio)
    os.remove(audio)

def call(text):
    action_call = "inertia"

    text = text.lower()

    if action_call in text:
        return True

    return False

def today_date():
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    ordinals = [
        "1st",
        "2nd",
        "3rd",
        "4th",
        "5th",
        "6th",
        "7th",
        "8th",
        "9th",
        "10th",
        "11th",
        "12th",
        "13th",
        "14th",
        "15th",
        "16th",
        "17th",
        "18th",
        "19th",
        "20th",
        "21st",
        "22nd",
        "23rd",
        "24th",
        "25th",
        "26th",
        "27th",
        "28th",
        "29th",
        "30th",
        "31st",
    ]

    return "Today is " + week_now + ", " + months[month_now - 1] + " the " + ordinals[day_now - 1] + "."

def open_folder(folder_name):
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    folder_path = os.path.join(desktop_path, folder_name)
    if os.path.isdir(folder_path):
        os.startfile(folder_path)
    else:
        print(f"{folder_name} not found on desktop.")
def say_hello(text):
    greet = ["hi", "hey", "hola", "greetings", "wassup", "hello"]

    response = ["hello", "hello", "hello", "hey there"]

    for word in text.split():
        if word.lower() in greet:
            return random.choice(response) + "."

    return ""
def send_email(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login("email", "pass")
    server.sendmail("email", to, content)
    server.close()
def wiki_person(text):
    list_wiki = text.split()
    for i in range(0, len(list_wiki)):
        if i + 3 <= len(list_wiki) - 1 and list_wiki[i].lower() == "who" and list_wiki[i + 1].lower() == "is":
            return list_wiki[i + 2] + " " + list_wiki[i + 3]


def open(folder_name):
    desktop_path = r"C:\Users\indhr\OneDrive\Desktop\\"
    folder_path = os.path.join(desktop_path, folder_name)
    if os.path.isdir(folder_path):
        os.startfile(folder_path)
        print(f"Opened folder{folder_path}")

    else:
        print(f" folder{folder_path} does not exist")








def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])

def process_input(rec_text):
    text = word_tokenize(rec_text)
    return text


while True:

        try:
            rec_text = rec_audio()
            text = process_input(rec_text)
            speak = ""



            if call(text):

                speak = speak + say_hello(text)



               # elif 'notepad' in text.lower():
                    #text = text.replace("open", "")
                    #text = text.replace("assistant", "")
                    #pyautogui.press("super")
                    #pyautogui.typewrite(text)
                    #pyautogui.sleep(2)
                    #pyautogui.press("enter")



                if 'play music' in text.lower():

                    from playmusic import music
                    music()

                elif "screenshot" in text.lower():
                    import pyautogui  # pip install pyautogui
                    im = pyautogui.screenshot()
                    im.save("ss.jpg")
                elif 'open camera' in text.lower():
                    text = text.replace("open", "")
                    text = text.replace("inertia", "")
                    pyautogui.press("super")
                    pyautogui.typewrite(text)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")




                elif ' folder from desktop' in text.lower():
                    print("Tell the folder name")
                    folder = rec_audio()

                    open(folder)



                elif "google" in text.lower():
                    ind = text.lower().split().index("google")
                    search = text.split()[ind + 1:]
                    webbrowser.open(
                        "https://www.google.com/search?q=" + "+".join(search))
                    speak = speak + "Searching " + str(search) + " on google"
                # app_id ="X8ALKK-2QYRYPH6WW"
                   # client = wolframalpha.Client(app_id)
                    #ind = text.lower().split().index("is")
                    #text = text.split()[ind + 1:]
                   # res = client.query(" ".join(text))
                  #  answer = next(res.results).text
                   # speak = speak + "The answer is " + answer



                elif "ipl score" in text.lower():
                    response = requests.get(
                        "https://cricapi.com/api/cricketScore?apikey=YOUR_API_KEY&unique_id=IPL_MATCH_ID")
                    data = json.loads(response.text)
                    team1 = data["team-1"]
                    team2 = data["team-2"]
                    score = data["score"]
                    sentence = f"The current score for {team1} versus {team2} is {score}."
                    speak = speak + f"The current score for {team1} versus {team2} is {score}"


                talk(speak)
        except:

            response(speak)


