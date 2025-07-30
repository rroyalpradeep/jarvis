# J.A.R.V.I.S. – Python AI Computer Assistant
# Developed by Pradeep Soni & Team

from typing import Union, Any
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib
from tkinter import *
import requests

# ===============================
#   Initialize Text-to-Speech
# ===============================
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 170)  # Speaking speed

# ===============================
#   Voice Selection Functions
# ===============================
def male_voice():
    engine.setProperty('voice', voices[0].id)
    Box.destroy()

def female_voice():
    engine.setProperty('voice', voices[1].id)
    Box.destroy()

# ===============================
#   Speak Function
# ===============================
def speak(audio):
    print(f"J.A.R.V.I.S.: {audio}")
    engine.say(audio)
    engine.runAndWait()

# ===============================
#   Greeting Function
# ===============================
def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("It's JARVIS sir. Tell me how may I help you?")

# ===============================
#   Take Command Function
# ===============================
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        speak("Recognizing...")
        query: Union[str, Any] = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        speak("Sorry sir, please say it again.")
        return "None"

    return query.lower()

# ===============================
#   Email Function
# ===============================
def send_email(to, content):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        # Use your email and app password
        server.login('youremail@gmail.com', 'yourpassword')
        server.sendmail('youremail@gmail.com', to, content)
        server.close()
        speak("Email sent successfully.")
    except:
        speak("Sorry sir, I was unable to send the email.")

# ===============================
#   Weather Function
# ===============================
def get_weather(city):
    url = f'https://wttr.in/{city}?format=3'
    try:
        data = requests.get(url)
        return data.text
    except:
        return "Error fetching weather data."

# ===============================
#   Evaluate Expression
# ===============================
def evaluate_expression(expression):
    try:
        return eval(expression)
    except Exception as e:
        return f"Error: {e}"

# ===============================
#   GUI for Voice Selection
# ===============================
Box = Tk()
Box.geometry('400x150')
Box.title('Welcome to JARVIS')

heading = Label(Box, text='Choose voice version')
heading.pack()

Button(Box, text="Male version", height=2, width=16, command=male_voice).pack()
Button(Box, text="Female version", height=2, width=16, command=female_voice).pack()

speak("Choose your preferred voice")
Box.mainloop()

# ===============================
#   Main Execution
# ===============================
if __name__ == "__main__":
    wish_me()

    while True:
        query = take_command()

        # Wikipedia Search
        if 'tell me about' in query or 'search' in query:
            speak("Searching Wikipedia...")
            query = query.replace("tell me about", "").replace("search", "")
            results = wikipedia.summary(query, sentences=2)
            speak(results)

        # Weather
        elif 'weather' in query:
            speak("For which location, sir?")
            location = take_command()
            report = get_weather(location)
            speak(f"Weather report for {location} is: {report}")

        # Math Evaluation
        elif 'evaluate' in query:
            expression = query.replace("evaluate", "").strip()
            result = evaluate_expression(expression)
            speak(f"The result is {result}")

        # Open YouTube
        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")
            speak("Opening YouTube")

        # Open Google
        elif 'open google' in query:
            webbrowser.open("https://google.com")
            speak("Opening Google")

        # Open WhatsApp
        elif 'open whatsapp' in query:
            webbrowser.open("https://api.whatsapp.com")
            speak("Opening WhatsApp")

        # Open File Manager
        elif 'open file manager' in query:
            webbrowser.open("C:/")
            speak("Opening File Manager")

        # Start Coding
        elif 'start coding' in query:
            webbrowser.open("https://onlinegdb.com")
            speak("Opening Online GDB for coding")

        # Open College Website
        elif 'open college site' in query:
            webbrowser.open("https://liet.in")
            speak("Opening College Website")
