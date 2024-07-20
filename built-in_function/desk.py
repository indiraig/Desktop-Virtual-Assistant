import os
import speech_recognition as sr
def rec_comm():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak the folder name")
        audio =r.listen(source)
    try:
        command =r.recognize_google(audio)
        print(f"You said:{command}")
        return command
    except sr.UnknownValueError:
        print("Sorry I didn't understand the command")
if __name__ == '__main__':
    folder_name = rec_comm()
    if folder_name:
        desktop_path = r"C:\Users\indhr\OneDrive\Desktop\\"
        folder_path=os.path.join(desktop_path,folder_name)
        if os.path.isdir(folder_path):
            os.startfile(folder_path)
            print(f"Opened folder{folder_path}")
        else:
             print(f" folder{folder_path} does not exist")

    if "net beans " in folder_name:

            os.startfile(r"C:\\Program Files\\NetBeans-15\\netbeans\\bin\\netbeans64.exe")






