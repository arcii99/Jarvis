import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import os
import cv2
import random
 
engine = pyttsx3.init('sapi5')
voices =  engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    # tt = time.strftime("%I:%M %p")
    if hour>=0 and hour<12:
        speak("Good Morning Sir. My name is Jarvis. How Can I help You")
    elif hour>=12 and hour<17:
        speak("Good Afternoon Sir. My name is Jarvis. How Can I help You")
    else:
        speak("Good Evening Sir. My name is Jarvis. How Can I help You")

def takeCommand():
    # it takes microphone input from user and gives string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening your command ....")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)
    
    try:
        print("Recognizing....")
        query =r.recognize_google(audio,language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        # print(e)
        speak("Say that again please")
        return "None" 

    return query

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            speak("Open Youtube")
            webbrowser.open("https://www.youtube.com/")
            query=query.replace("Open youtube","")

            
        elif "open instagram" in query:
            webbrowser.open("https://www.instagram.com/")
            speak("opening instagram")
            query=query.replace("open instagram","")

        elif "open google" in query:
            speak("Opening google")
            webbrowser.open("https://www.google.com")
            query=query.replace("open google","")
            

        elif "open notepad" in query:
            npath = "C:\\WINDOWS\\system32"
            os.startfile(npath)

        elif "open camera" in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret , img =cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "open FL studio" in query:
            npath="C:\\Program Files (x86)\\Image-Line\\FL Studio 20\\FL64.exe"
            os.startfile(npath)

        elif "play music" in query:
            music_dir = "D:\songs collection 1"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir,rd))