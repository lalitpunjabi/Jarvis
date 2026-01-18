import speech_recognition as sr
import webbrowser
import pyttsx3
import datetime
import wikipedia
import os
import psutil
import pyautogui
import tkinter as tk
from tkinter import Label, Button
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# -------------------- VOICE ENGINE --------------------
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# -------------------- SYSTEM UTILITIES --------------------
def get_time():
    return datetime.datetime.now().strftime("%I:%M %p")

def get_date():
    return datetime.datetime.now().strftime("%A, %d %B %Y")

def battery_status():
    battery = psutil.sensors_battery()
    percent = battery.percent
    speak(f"Your battery is at {percent} percent")

def shutdown_pc():
    speak("Shutting down your computer")
    os.system("shutdown /s /t 3")

def restart_pc():
    speak("Restarting your computer")
    os.system("shutdown /r /t 3")

def take_screenshot():
    img = pyautogui.screenshot()
    img.save("jarvis_screenshot.png")
    speak("Screenshot taken and saved")

# -------------------- VOLUME CONTROL --------------------
def set_volume(change):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None
    )
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    current = volume.GetMasterVolumeLevelScalar()

    if change == "up":
        new = min(current + 0.1, 1.0)
    else:
        new = max(current - 0.1, 0.0)

    volume.SetMasterVolumeLevelScalar(new, None)
    speak("Volume adjusted")

# -------------------- GUI FOR JARVIS --------------------
def open_gui():
    root = tk.Tk()
    root.title("Jarvis Assistant")
    root.geometry("300x250")

    Label(root, text="Jarvis Control Panel", font=("Arial", 14)).pack(pady=10)

    Button(root, text="Open Google", command=lambda: webbrowser.open("https://google.com")).pack(pady=5)
    Button(root, text="Open Spotify", command=lambda: os.system("start spotify")).pack(pady=5)
    Button(root, text="Take Screenshot", command=take_screenshot).pack(pady=5)
    Button(root, text="Shutdown PC", command=shutdown_pc).pack(pady=5)
    Button(root, text="Close", command=root.destroy).pack(pady=5)

    root.mainloop()

# -------------------- COMMAND PROCESSOR --------------------
def processCommand(c):
    c = c.lower()
    print("Processing:", c)

    if "open google" in c:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "open youtube" in c:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open linkedin" in c:
        speak("Opening LinkedIn")
        webbrowser.open("https://linkedin.com")

    elif "open spotify" in c:
        speak("Opening Spotify")
        os.system("start spotify")

    elif "play on spotify" in c:
        song = c.replace("play on spotify", "").strip()
        speak(f"Searching {song} on Spotify")
        webbrowser.open(f"https://open.spotify.com/search/{song}")

    elif "send whatsapp" in c:
        msg = c.replace("send whatsapp", "").strip()
        speak("Opening WhatsApp")
        webbrowser.open(f"https://wa.me/?text={msg}")

    elif "open gmail" in c:
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")

    elif "time" in c:
        speak(f"The time is {get_time()}")

    elif "date" in c:
        speak(f"Today is {get_date()}")

    elif "battery" in c:
        battery_status()

    elif "shutdown" in c:
        shutdown_pc()

    elif "restart" in c:
        restart_pc()

    elif "increase volume" in c:
        set_volume("up")

    elif "decrease volume" in c:
        set_volume("down")

    elif "screenshot" in c:
        take_screenshot()

    elif "open jarvis window" in c or "open gui" in c:
        speak("Opening Jarvis panel")
        open_gui()

    elif "wikipedia" in c:
        speak("Searching Wikipedia")
        query = c.replace("wikipedia", "").strip()
        try:
            result = wikipedia.summary(query, sentences=2)
            speak(result)
        except:
            speak("I couldn't find that on Wikipedia")

    elif "play" in c:
        song = c.replace("play", "").strip()
        speak(f"Searching and playing {song}")
        webbrowser.open(f"https://www.youtube.com/results?search_query={song}")

    elif "exit" in c or "quit" in c:
        speak("Goodbye Lalit. Shutting down.")
        exit()

    else:
        speak("I did not understand that command.")

# -------------------- MAIN LOOP --------------------
if __name__ == "__main__":
    speak("Jarvis is online. Say Jarvis to activate.")

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=3)

            word = recognizer.recognize_google(audio)
            print("Heard:", word)

            if word.lower() == "jarvis":
                speak("Yes Lalit")

                with sr.Microphone() as source:
                    print("Jarvis Active... Speak your command")
                    audio = recognizer.listen(source, phrase_time_limit=6)

                command = recognizer.recognize_google(audio)
                print("Command:", command)
                processCommand(command)

        except Exception as e:
            print("Error:", e)
