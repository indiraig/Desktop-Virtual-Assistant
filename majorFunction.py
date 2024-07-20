import math
import warnings
#import gktest
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import playsound
import os
from nltk import word_tokenize
import datetime
from bs4 import BeautifulSoup
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
def process_input(rec_text):
    text = word_tokenize(rec_text)
    return text
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
        "20th"
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
def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])
while True:


    try:

        text = rec_audio()
        speak = ""



        if call(text):

            speak = speak + say_hello(text)


            if " today date" in text or "day" in text or "month" in text:
                get_today = today_date()
                speak = speak + " " + get_today

            elif "time" in text:
                now = datetime.datetime.now()
                meridiem = ""
                if now.hour >= 12:
                    meridiem = "p.m"
                    hour = now.hour - 12
                else:
                    meridiem = "a.m"
                    hour = now.hour

                if now.minute < 10:
                    minute = "0" + str(now.minute)
                else:
                    minute = str(now.minute)
                speak = speak + " " + "It is " + str(hour)  + ":" + minute + " " + meridiem + "."




            elif "who are you" in text or "define yourself" in text:
                speak = speak + "Hello, I am an Inertia. Your Assistant. You can command me to perform various tasks such as asking questions or opening applications etcetera"
            elif "made you" in text or "created you" in text:
                speak = speak + "I was created by Akshara Indira Revathy Jothika"
            elif "how are you" in text:
                speak = speak + "I am awesome, Thank you"
                speak = speak + "\nHow are you?"

            elif "fine" in text or "good" in text:
                speak = speak + "It's good to know that your fine"


            elif "open" in text.lower():

                if "chrome" in text.lower():
                    speak = speak + "Opening Google Chrome"

                    os.startfile(
                        r"C:\Program Files\Google\Chrome\Application\chrome.exe"

                    )



                if "microsoft edge" in text.lower():
                    speak = speak + "Opening Google Chrome"

                    os.startfile(
                        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"



                    )

                elif ' incognito window' in text.lower():
                    pyautogui.hotkey('ctrl', 'shift', 'n')

                elif 'open history' in text.lower():
                    pyautogui.hotkey('ctrl', 'h')
                elif 'open downloads' in text.lower():
                    pyautogui.hotkey('ctrl', 'j')

                elif "youtube" in text.lower():
                    speak = speak + "Opening Youtube\n"
                    webbrowser.open("https://youtube.com/")
                elif "google" in text.lower():
                    speak = speak + "Opening Google\n"
                    webbrowser.open("https://google.com/")
                elif "stackoverflow" in text.lower():
                    speak = speak + "Opening StackOverFlow"
                    webbrowser.open("https://stackoverflow.com/")
                elif 'open new window' in text.lower():
                    pyautogui.hotkey('ctrl', 'n')

                elif 'open gmail' in text.lower():
                    webbrowser.open_new_tab("https://www.gmail.com")
                    speak = speak +"Gmail is open"
                    time.sleep(5)
                elif " code" in text.lower():
                    speak = speak + "Opening Visual Studio Code"
                    os.startfile(
                        r"C:\Users\indhr\.vscode.exe"
                    )
                elif "word" in text.lower():
                    speak = speak + "Opening Microsoft Word"
                    os.startfile(
                        r"C:\Program Files\Microsoft Office\root\Office16\Winword.exe"
                    )
                elif "excel" in text.lower():
                    speak = speak + "Opening Microsoft Excel"
                    os.startfile(
                        r"C:\Program Files\Microsoft Office\root\Office16\excel.exe"
                    )

                elif 'website' in text.lower():
                    speak = speak + "website launching"
                    text = text.replace("inertia"," ")
                    text = text.replace("website", " ")
                    web1 = text.replace("open", " ")
                    web2 = "https://www." + web1 + ".com"
                    webbrowser.open(web2)


                elif "file explorer" in text.lower():
                    os.startfile(os.path.join(os.environ["WINDIR"],"explorer.exe"))

                elif 'open command prompt' in text:
                    os.system("start cmd")
                elif ' instagram' in text.lower():
                    webbrowser.open("instagram.com")

                elif ' facebook' in text.lower():
                    webbrowser.open("https://www.facebook.com/")
                elif 'amazon' in text.lower():
                    webbrowser.open("https://www.amazon.in/")


                else:
                    speak = speak + "Application not available"
            elif 'add two number' in text.lower():
                print(math.sum(1.0,2.9))

            elif "scroll down" in text.lower():
                pyautogui.hotkey('shift','pgdn')
                speak = speak + "Scrolling a page down"
            elif "scroll up" in text.lower():
                pyautogui.hotkey('shift','pgup')
                speak = speak + "Scrolling a page up"


            elif ' folder from desktop' in text.lower():
                ans = "folder name"
                speak = speak + "tell" + ans


            elif ' paint' in text.lower():
                text = text.replace("open", "")
                text = text.replace("inertia", "")
                pyautogui.press("super")
                pyautogui.typewrite(text)
                pyautogui.sleep(2)
                pyautogui.press("enter")

            elif 'maximize this window' in text.lower():
                pyautogui.hotkey('alt', 'space')
                time.sleep(1)
                pyautogui.press('x')

            elif 'refresh' in text.lower():
                pyautogui.hotkey('fn', 'f5')

            elif 'notepad' in text.lower():
                text = text.replace("open", "")
                text = text.replace("inertia", "")
                pyautogui.press("super")
                pyautogui.typewrite(text)
                pyautogui.sleep(2)
                pyautogui.press("enter")
            elif 'vs code' in text.lower():
                text = text.replace("open", "")
                text = text.replace("inertia", "")
                pyautogui.press("super")
                pyautogui.typewrite(text)
                pyautogui.sleep(2)
                pyautogui.press("enter")

            elif 'netbeans' in text.lower():
                from dictapp import openappweb
                openappweb(text)
            elif 'designer' in text.lower():
                from dictapp import openappweb
                openappweb(text)


            elif "play" in text.lower():
                pyautogui.press("k")
                speak("video played")

            elif "volume up" in text.lower():
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")

            elif "volume down" in text.lower():
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")

            elif "mute" in text.lower():
                pyautogui.press("volumemute")


            elif 'minimise this window' in text.lower():
                pyautogui.hotkey('alt', 'space')
                time.sleep(1)
                pyautogui.press('n')


            elif 'previous tab' in text.lower():
                pyautogui.hotkey('ctrl', 'shift', 'tab')
            elif 'next tab' in text.lower():
                pyautogui.hotkey('ctrl', 't')
            elif 'close tab' in text.lower():
                pyautogui.hotkey('ctrl', 'w')


            elif "search youtube" in text.lower():
                ind = text.lower().split().index("youtube")
                search = text.split()[ind + 1:]
                webbrowser.open(
                "http://www.youtube.com/results?search_query=" + "+".join(search)
                )
                speak = speak + "Opening " + str(search) + "the search  on youtube"


            elif "search" in text.lower():
                ind = text.lower().split().index("search")
                search = text.split()[ind + 1:]
                webbrowser.open( "https://www.google.com/search?q=" + "+".join(search))
                speak = speak + "Searching " + str(search) + " on google"


            elif "google" in text.lower():
                ind = text.lower().split().index("google")
                search = text.split()[ind + 1:]
                webbrowser.open(
                    "https://www.google.com/search?q=" + "+".join(search))
                speak = speak + "Searching " + str(search) + " on google"

            elif "change background" in text or "change wallpaper" in text:
                img = r"C:\Users\indhr\OneDrive\Desktop\image"
                list_img = os.listdir(img)
                imgChoice = random.choice(list_img)
                randomImg = os.path.join(img, imgChoice)
                ctypes.windll.user32.SystemParametersInfoW(20, 0, randomImg, 0)
                speak = speak + "Background changed successfully"


            elif 'close window' in text.lower():
                pyautogui.hotkey('ctrl', 'shift', 'w')

            elif "remember that" in text.lower():
                #text= text.replace("remember that", " ")
                #text = text.replace("inertia", " ")
                text= "tomorrow is my friend birthday"
                print("ok done")
                speak = speak +  "You told me to remember that" + text
                #remember = open("remember.txt", "a")
                #remember.write(text)
                #remember.close()
            elif "what do you remember" in text.lower():
                #remember = open("remember.txt", "r")
                #speak =  "You told me to remember that" + remember.read()
                text1 = "tomorrow is my friend birthday"
                speak = "You told me to remember that"+ text1

            elif "whatsapp" in text.lower():
                from whatsapp import sendMessage

                sendMessage()

            elif "empty recycle bin" in text:
                winshell.recycle_bin().empty(
                    confirm=True, show_progress=False, sound=True
                )
                speak = speak + "Recycle Bin Emptied"

            elif "make a note" in text:
                talk("What would you like me to write down?")
                note_text = rec_audio()
                note(note_text)

                speak = speak + "I have made a note of that."

            elif "type" in text:
                pyautogui.hotkey('win', 'h')

            elif "stop typing " in text:
                pyautogui.hotkey('win', 'h')

            elif "joke" in text:
                speak = speak + pyjokes.get_joke()
            elif "where is" in text:
                 ind = text.lower().split().index("is")
                 location = text.split()[ind + 1:]
                 url = "https://www.google.com/maps/place/" + "".join(location)
                 speak = speak + "This is where " + str(location) + " is."
                 webbrowser.open(url)

            elif "email to computer" in text or "gmail to computer" in text:
                try:
                    talk("What should I say?")
                    content = rec_audio()
                    talk("whom should i send ")
                    to = input("Receiver email address:")
                    send_email(to, content)
                    speak = speak + "Email has been sent !"
                except Exception as e:
                    print(e)
                    talk("I am not able to send this email")

            #elif "who" or "what" or "which" or "why" in text.lower():
                    #from gktest import gkques
                   # gktest.gkques()
            elif " world news" in text:
                url = ('https://newsapi.org/v2/top-headlines?'
                       'country=us&'
                       'apiKey=ff2b18b364a3473d9831159d8ecfce37')
                try:
                         response = requests.get(url)
                except:
                        talk("check your connection")
                news = json.loads(response.text)

                for new in news["articles"]:
                    print(str(new["title"]), "\n")
                    talk(str(new["title"]))
                    engine.runAndWait()
                    print(str(new["description"]), "\n")
                    talk(str(new["description"]))
                    engine.runAndWait()

            elif "calculate" in text or 'send a message' in text:
                app_id = "X8ALKK-2QYRYPH6WW"
                client = wolframalpha.Client(app_id)
                ind = text.lower().split().index("calculate")
                text = text.split()[ind + 1:]
                res = client.query(" ".join(text))
                answer = next(res.results).text
                speak = speak + "The answer is " + answer



            elif "wikipedia" in text.lower():
                    speak("Searching from wikipedia....")
                    text = text.replace("wikipedia", "")
                    text = text.replace("search wikipedia", "")
                    text = text.replace("inertia", "")
                    results = wikipedia.summary(text, sentences=2)
                    speak("According to wikipedia..")
                    print(results)
                    speak = speak + "the answer is " +results


               # app_id ="X8ALKK-2QYRYPH6WW"
               # client = wolframalpha.Client(app_id)
                #ind = text.lower().split().index("is")
                #text = text.split()[ind + 1:]
               # res = client.query(" ".join(text))
              #  answer = next(res.results).text
               # speak = speak + "The answer is " + answer
            elif "temperature" in text.lower():
                search = "temperature in delhi"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
               # speak(f"current{search} is {temp}")
                speak = speak + "the temperature in this area is  " + temp

            elif "weather" in text.lower():
                search = "temperature in delhi"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                speak = speak + "the temperature in this area is  " + temp

            elif "don't listen" in text or "stop listening" in text or "do not listen" in text:
                talk("for how many seconds do you want me to sleep")
                print("for how many seconds do you want me to sleep")
                a = 5
                time.sleep(a)
                print (" Completed. Now you can ask me anything")
                speak = speak + str(a) + " seconds completed. Now you can ask me anything"






            elif "exit" in text or "quit" in text:
                exit()

            elif 'open command prompt' in text:
                os.system("start cmd")

            elif " see folder" in text.lower():
                os.startfile('C:\\')

            elif " tea folder" in text.lower():
                os.startfile('D:\\')
            elif " Desktop  folder" in text.lower():
                os.startfile( r"C:\\Users\\indhr\\OneDrive\\Desktop")
            elif " Document folder" in text.lower():
                os.startfile('D:\\')




            elif "close" in text.lower():
                if "chrome" in text.lower():
                    speak = speak + "Closing Google Chrome"
                    os.system("taskkill /f /im chrome.exe")
                elif "word" in text.lower():
                    speak = speak + "Closing Microsoft Word"
                    os.system("taskkill /f /im WINWORD.exe")
                elif "excel" in text.lower():
                    speak = speak + "Closing Microsoft Excel"
                    os.system("taskkill /f /im WINWORD.exe")
                elif "this page" in text.lower():
                    os.system("taskkill /f /im explorer.exe")
                elif ' command' in text:
                    os.system("taskkill /f /im cmd.exe")
                elif ' notepad' in text:
                    os.system("taskkill /f /im notepad.exe")
                elif 'Netbeans' in text:
                    os.system("taskkill /f /im netbeans.exe")
            elif "shut down" in text:
                speak = speak +"Ok , your system will shut down in 10 secs"
                subprocess.call(["shutdown", "/l"])

            talk(speak)
    except:
        response(speak)

