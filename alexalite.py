from ctypes.wintypes import WORD
from time import strftime
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import random
import time
from PyDictionary import PyDictionary
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    #engine.say('thank you for asking')
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'rani' in command:
                command = command.replace('rani', '')
            print(command)

    except:
        pass
        #command = 'Try again'
        #print('Try again')
    return command


def run_rani():
    command = take_command()
    command = command.lower()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%S %p')
        print(time)
        talk('Current time is' + time)
    elif 'who is' in command:
        person = command.replace('Who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('yes, i want to date you')
    elif 'are you single' in command:
        talk('i am in a relationship with you')
    elif 'joke' in command:

        talk(pyjokes.get_joke())
    elif 'meaning of' in command:
        dict = PyDictionary()
        i = command.rindex(' ')
        meaning = dict.meaning(command[i:])
        print(meaning)
        talk(meaning)
    elif 'search for' in command:
        item = command.replace('search for', '')
        pywhatkit.search(item)
    elif 'take ss' in command:
        filename = random.randint(1000000000, 9999999999)
        talk("Screen shot will be taken in 5sec")
        talk("Five")
        # time.sleep(1)
        talk("Four")
        # time.sleep(1)
        talk("Three")
        # time.sleep(1)
        talk("Two")
        # time.sleep(1)
        talk("One")
        pywhatkit.take_screenshot(str(filename), 0)
    elif 'send message' in command:
        pywhatkit.sendwhatmsg("+91 79800 49070", 'Hello from pankaj', 18, 17)
        talk("Successfully Sent! ")
    else:
        talk('please say the command again.')


while True:
    run_rani()
