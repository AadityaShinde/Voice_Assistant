import pyttsx3  #pip install pyttsx3
import datetime
import speech_recognition as sr        #pip install SpeechRecognition
import pyaudio      #pip install pyaudio
import wikipedia             
import smtplib
import webbrowser as wb
import os
import pyautogui    #pip install pyautogui
import psutil   #pip install psutil
import pyjokes  #pip install pyjokes

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
newVoiceRate = 190
engine.setProperty('rate', newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back sir!")
    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <= 12:
        speak("Good Morning!")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon!")
    elif hour >= 18 and hour <= 24:
        speak("Good Evening!")
    else:
        speak("Good Night!")

    speak("Allen at your service. How I can help you?")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        print("Say that again please...")

        return "None"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('Your-user-name@gmail.com', 'your-password-here')
    server.sendmail('Your-user-name@gmail.com', to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.saver("path_of_folder_where_you_can_save_ss")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage)

    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

if __name__ == '__main__':
    wishme()
    while True:
        query = takecommand().lower()

        if "time" in query:
            time()

        elif "date" in query:
            date()

        elif "offline" in query:
            speak("Going offline")
            quit()

        elif "wikipedia" in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "send email" in query:
            try:
                speak("What should I say?")
                print("What should I say?")
                content = takecommand()
                to = "reciver-user-name@gmail.com"
                #sendEmail(to, content)
                speak("Email sent successfully...")
                print("Email sent successfully...")
            except Exception as e:
                speak(e)
                speak("Unable to send the Email")
                print("Unable to send the Email")

        elif "search in chrome" in query:
            speak("What should I search?")
            print("What should I search?")
            chromepath = "cromepath_on_your_system"
            search = takecommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")

        elif "log out" in query:
            os.system("shutdown - 1")

        elif "shutdown" in query:
            os.system("shutdown /s /t 1")

        elif "restart" in query:
            os.system("shutdown /r /t 1")

        elif "play songs" in query:
            songs_dir = "musicpath"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif "remember that" in query:
            speak("What should I remember?")
            print("What should I remember?")
            data = takecommand()
            speak("You should be remember" + data)
            print("You should be remember" + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you know something" in query:
            remember = open("data.txt", "r")
            speak("You said me to remember that" + remember.read())
            print("You said me to remember that" + remember.read())

        elif "screenshot" in query:
            screenshot()
            speak("Done!")
            print("Done!")

        elif "cpu" in query:
            cpu()

        elif "joke" in query:
            jokes()
