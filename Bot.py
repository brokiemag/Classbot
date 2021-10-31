import wikipedia
import speech_recognition as sr
from GoogleNews import GoogleNews
import pyttsx3
from datetime import date
import datetime
import pyjokes


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# wishme (regular greetings according to the time )


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)


    if hour >= 0 and hour <= 12:
        speak(f"good morning ayaan")
    elif hour >= 12 and hour <= 18:
        speak(f"good afternoon ayaan")
    else:
        speak(f"good evening ayaan")
        
# voice input


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

wish()
while True:
        query = takeCommand().lower()
# search/order_commands
        if "hi sohan" in query or "hello sohan" in query:
            speak("hi ayaan")
        elif "how are you sohan" in query:
            speak("great ayaan")
        elif "thank you sohan" in query:
            speak("welcome ayaan")
        elif "good evening sohan" in query or "good morning sohan" in query or "good afternoon sohan" in query:
            wish = query
            wish = wish.replace("sohan", "")
            speak(wish)
        elif 'sohan can you tell me a joke' in query:
            s = pyjokes.get_joke(language='en', category='all')
            speak(s)
        elif "sohan what" in query or "sohan who" in query or "sohan how" in query:
            speak('one second ayaan')
            query = query
            query = query.replace("sohan", "")
            result = wikipedia.summary(query, sentences=2)
            speak("ayaan"+result)
        elif "sohan" in query:
            speak('Yes ayaan...')
            query = takeCommand()
            result = wikipedia.summary(query, sentences=2)
            speak("ayaan"+result)
#test
        # if "hi sohan" in query or "hello sohan" in query:
        #         speak("hi ayaan")
        #         query = query
        #         if "how are you" in query:
        #             speak("great ayaan")
        #         elif "thank you" in query:
        #             speak("welcome ayaan")
        #         elif "good evening" in query or "good morning" in query or "good afternoon" in query:
        #             wish = query
        #             wish = wish.replace("sohan", "")
        #             speak(wish)
        #         elif 'sohan can you tell me a joke' in query:
        #             s = pyjokes.get_joke(language='en', category='all')
        #             speak(s)
        #         elif "sohan what" in query or "sohan who" in query:
        #             speak('one second ayaan')
        #             query = query
        #             query = query.replace("sohan", "")
        #             result = wikipedia.summary(query, sentences=2)
        #             speak("ayaan"+result)
        #         elif "sohan" in query:
        #             speak('Yes ayaan...')
        #             query = takeCommand()
        #             result = wikipedia.summary(query, sentences=2)
        #             speak("ayaan"+result)
        #         else:
        #             pass
#test


        

