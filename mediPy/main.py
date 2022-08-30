import sys
import speech_recognition
import pyttsx3 as tts
import webbrowser
import pyjokes
import wikipedia



recognizer = speech_recognition.Recognizer()

#setting speaker properties
speaker = tts.init();
speaker.setProperty('rate', 180)
voices = speaker.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
speaker.setProperty('voice', voices[1].id) # female

def sayIt(txt):
    speaker.say(txt)
    speaker.runAndWait()

def listenAndProcess():
    with speech_recognition.Microphone() as mediMic:
        print('Listening...')
        recognizer.pause_threshold = 0.6
        recognizer.adjust_for_ambient_noise(mediMic)
        audio = recognizer.listen(mediMic)

        try:
            print('Recognizing...')
            query = recognizer.recognize_google(audio, language ='en-in')
            query = query.lower()
            print('User said: '+ query)
            if 'medi' in query or 'medina' in query:
                sayIt('Oh, yes she definitely is.')
            elif 'thank you' in query:
                sayIt('You\'re welcome')
            elif 'hello' in query or 'hi' in query:
                sayIt("Hello!")
            elif 'open google' in query:
                webbrowser.open('google.com')
            elif 'open youtube' in query:
                webbrowser.open('youtube.com')
            elif 'joke' in query:
                joke = pyjokes.get_joke()
                print(joke)
                sayIt(joke)
            elif 'creator' in query or 'created' in query:
                sayIt('Medina Medi created me.')
            elif 'wikipedia' in query:
                query = query.replace('wikipedia', '')
                results = wikipedia.summary(query, sentences = 2)
                print(results)
                sayIt(results)
            elif 'exit' in query or 'bye' in query:
                exit()

        except Exception as e:
            print(e)
            print('I did not understand. Please repeat it.')
            return "None"



sayIt("Hi, how can I help you?")
while True:
    listenAndProcess()

