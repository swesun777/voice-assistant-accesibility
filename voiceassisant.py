import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import random
import requests
import os
import bs4


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'ash' in command:
                command = command.replace('ash', '')
                print(command)
            else:
                os._exit(os.EX_OK)
    except:
        pass
    return command

def run_ash():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')

        talk('the current time is ' + time)
    elif 'how are you' in command:
        reply = ['I am fine, thank you for asking', 'never better. how about you?', 'i am all good. glad you asked']
        condition = random.choice(reply)
        print(condition)
        talk(condition)
    elif 'thank you' in command:
        ans = ['you are welcome', 'anytime', 'my pleasure']
        welcome = random.choice(ans)
        print(welcome)
        talk(welcome)
    elif 'where are you' or 'where do you live' in command:
        location = 'I live on the cloud, not possible by any human, is it? I am supernatural'
        talk(location)
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif 'tell me about' or 'what is' in command:
        thing = command.replace('tell me about' or 'what is', '')
        info = wikipedia.summary(thing, 3)
        print(info)
        talk(info)
    elif 'news' or 'headlines' in command:
        from bs4 import BeautifulSoup
        url = 'https://www.bbc.com/news'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find('body').find_all('h3')
        for x in headlines:
            talk(x.text.strip())
    elif 'story' in command:
        sentence_starter = ['About 100 years ago', ' In the 20 BC', 'Once upon a time']
        character = [' there lived a king.', ' there was a man named Jack.',
                     ' there lived a farmer.']
        time = [' One day', ' One full-moon night']
        story_plot = [' he was passing by', ' he was going for a picnic to ']
        place = [' the mountains', ' the garden']
        second_character = [' he saw a man', ' he saw a young lady']
        age = [' who seemed to be in late 20s', ' who seemed very old and feeble']
        work = [' searching something.', ' digging a well on roadside.']
        story = random.choice(sentence_starter) + random.choice(character) + random.choice(time) + random.choice(story_plot) + random.choice(place) + random.choice(second_character) + random.choice(age) + random.choice(work)
        print(story)
        talk(story)
    elif 'laugh' in command:
        laugh = 'ha ha ha he he he hu hu hu he he ha ha ha'
        talk(laugh)
    elif 'you are doing a bad job' or 'idiot' or 'dumb' or 'stupid' in command:
        answer = ['hey, that is not nice', 'i am doing my best here, i am sorry if i did anything wrong']
        aplg = random.choice(answer)
        talk(aplg)
    else:
        talk('i am not sure about that, i am still developing, please try asking something from the pamphlet '
             'provided, thank you!')
run_ash()




