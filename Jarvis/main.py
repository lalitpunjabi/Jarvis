import speech_recognition as sr
import webbrowser
import pyttsx3
import datetime
import wikipedia
import os
import google.generativeai as genai

# 🔹 PASTE YOUR GEMINI API KEY HERE
genai.configure(api_key="YOUR_GEMINI_API_KEY_HERE")

model = genai.GenerativeModel("gemini-1.5-flash")

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_time():
    return datetime.datetime.now().strftime("%I:%M %p")

def get_date():
    return datetime.datetime.now().strftime("%A, %d %B %Y")

def ai_response(prompt):
    response = model.generate_content(prompt)
    return response.text

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

    elif "time" in c:
        speak(f"The time is {get_time()}")

    elif "date" in c:
        speak(f"Today is {get_date()}")

    elif "wikipedia" in c:
        speak("Searching Wikipedia")
        query = c.replace("wikipedia", "").strip()
        result = wikipedia.summary(query, sentences=2)
        speak(result)

    elif "open notepad" in c:
        speak("Opening Notepad")
        os.system("notepad")

    elif "open chrome" in c:
        speak("Opening Chrome")
        os.system("start chrome")

    elif "play" in c:
        song = (
            c.replace("play", "")
             .replace("song", "")
             .replace("please", "")
             .strip()
        )
        speak(f"Playing {song}")
        webbrowser.open(f"https://www.youtube.com/results?search_query={song}")

    elif "exit" in c or "quit" in c:
        speak("Goodbye Lalit. Shutting down.")
        exit()

    else:
        speak("Thinking with Gemini...")
        answer = ai_response(c)
        print("Gemini:", answer)
        speak(answer)

if __name__ == "__main__":
    speak("Jarvis AI with Gemini is now online. Say Jarvis to activate.")

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
                    print("Jarvis Active...")
                    audio = recognizer.listen(source, phrase_time_limit=6)

                command = recognizer.recognize_google(audio)
                print("Command:", command)
                processCommand(command)

        except Exception as e:
            print("Error:", e)
