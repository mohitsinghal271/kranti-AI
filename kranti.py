import os
import sys
import pyttsx3
import speech_recognition as sr
from googletrans import Translator
import webbrowser

def speak(text):                               # function creates    
    engine = pyttsx3.init()                    # initialisation of engine of pyttsx3
    voices = engine.getProperty("voices")      # set up of voice property
    engine.setProperty("voice", voices[2].id)  # index of built-in voice as index starts from 0
    engine.setProperty("rate", 160)            # text-to-speech speed defined here
    engine.say(text)                           # whatever text passed, speaks here
    engine.runAndWait()                        # run & wait until above text complete
    
t = Translator()
r = sr.Recognizer()

if __name__ == "_main_":
    speak("हेलो, मेरा नाम क्रांति है। बताइये में आपकी क्या मदद कर सकता हूं") 
    while True:
        with sr.Microphone() as source:            # microphone starts here
            speak("आपकी आवाज़ सुनी जा रही है")
            print("Listening your voice...")
            audio = r.listen(source)               # whatever you say, recorded in audio
            try:
                command = r.recognize_google(audio, language="hi-IN")       # use google search engine to recognize voice here, by default recognize English language
                speak("आपने कहा: " + command)
                translated = t.translate(command, dest="en").text     # whatever language use, translate into English
                if "youtube" in translated.lower():               
                    speak("youtube.com खोला जा रहा है")
                    print("Opening Youtube.com...")
                    webbrowser.open("https://www.youtube.com/")
                elif "wikipedia" in translated.lower():
                    speak("विकिपीडिया खोला जा रहा है")
                    print("Opening Wikipedia...")
                    webbrowser.open("https://wikipedia.org/")
                elif "HTML" in translated.lower():
                    speak("एचटीएमएल प्रोग्राम खोले जा रहे हैं")
                    print("Opening HTML Programs...")
                    os.startfile("C:/Users/gupta/Desktop/Shivani Docs/HTML (Main Practicals)")
                elif "year" in translated.lower():
                    speak("अभी कोनसा साल चल रहा है")
                    print("Year going on is...")
                elif "month" in translated.lower():
                    speak("अभी कोनसा महीना चल रहा है")
                    print("Month going on is...")
                elif "date" in translated.lower():
                    speak("आज क्या तारीख है")
                    print("Today's date is...")
                elif "day" in translated.lower():
                    speak("आज क्या दिन है")
                    print("Today's day is...")
                elif "prime minister" in translated.lower():
                    speak("हमारे प्रधान मंत्री का क्या नाम है")
                    print("Our Prime Minister name is...")
                elif "independence" in translated.lower():
                    speak("स्वतंत्रता दिवस कब मनाया जाता है")
                    print("Independence day celebrated on...")
                elif "colour" in translated.lower():
                    speak("सभी रंगों के नाम हिंदी और अंग्रेजी में")
                    print("Name of colours in Hindi are...")
                    print("Name of colours in English are...")
                elif "fruit" in translated.lower():
                    speak("10 फलों के नाम हिंदी और अंग्रेजी में")
                    print("Name of 10 fruits in Hindi are...")
                    print("Name of 10 fruits in English are...")
                elif "animal" in translated.lower():
                    speak("10 जानवरों के नाम हिंदी और अंग्रेजी में")
                    print("Name of 10 animals in Hindi are...")
                    print("Name of 10 animals in English are...")
                elif "bird" in translated.lower():
                    speak("10 पक्षियों के नाम हिंदी और अंग्रेजी में")
                    print("Name of 10 birds in Hindi are...")
                    print("Name of 10 birds in English are...")
                elif "close" in translated.lower():
                    speak("प्रोग्राम क्लोज किया जा रहा है")
                    print("Stopping Program...")
                    sys.exit()
            except sr.UnknownValueError:
                speak("में आपकी आवाज समझ नहीं पा रहा हूं। कृप्या फिर से बोलिए")
                print("Unrecognized Voice. Say that again please.")