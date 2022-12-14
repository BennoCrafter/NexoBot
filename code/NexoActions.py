import csv
import os
import sys
import webbrowser
import wikipedia
from random import randint
import pyttsx3
import pywhatkit as kit
from time import ctime
import speech_recognition as sr
import random
import pyjokes
from pyttsx3 import voice
import configs
from datetime import date
import locale
import training_module
import requests
import PrivateConfigs
import languageSaver
from time import sleep
from bs4 import BeautifulSoup
import pyperclip
from deep_translator import GoogleTranslator


####################
engine = pyttsx3.init()
r = sr.Recognizer()


def record_audio(ask="", dialog_happend=True):
    if configs.input_system:
        if ask:
            print(ask)
        if dialog_happend:
            show_logo()
            print("...")
        voice_data = input(":")  # listen for the audio via source
        if voice_data != "" and dialog_happend:
            print("✔️")
        if voice_data:
            print(voice_data.lower())
        return voice_data.lower()

    else:
        with sr.Microphone() as source:  # microphone as source
            if ask:
                engine_speak(ask)
            if dialog_happend:
                show_logo()
                print("...")
            audio = r.listen(source, 5, 5)  # listen for the audio via source
            voice_data = ""
            try:
                voice_data = r.recognize_google(audio, language=configs.pronouncing_language)  # convert audio to text
                if voice_data != "" and dialog_happend:
                    print("✔️")
            except sr.UnknownValueError:  # error: recognizer does not understand
                pass
            except sr.RequestError:
                pass
            if voice_data:
                print(voice_data.lower())
            return voice_data.lower()


def engine_speak(audio_string):
    if configs.say and not configs.developer_mode and not configs.pause:
        if configs.speak_variant == 0:
            os.system("say " + audio_string)
            print(configs.assis_name + ":", audio_string)
        if configs.speak_variant == 1:
            engine.say(audio_string)
            print(configs.assis_name + ":", audio_string)
    if not configs.say and not configs.pause and not configs.developer_mode:
        print(configs.assis_name + ":", audio_string)


def show_logo():
    if not configs.printed_header:
        for i in range(6):
            print(configs.ascii_art_pattern[i])
            sleep(0.1)
        hello(voice)
        configs.printed_header = True


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


# ACTIONS##########ACTIONS########ACTIONS#############
# ACTIONS##########ACTIONS########ACTIONS#############
# ACTIONS##########ACTIONS########ACTIONS#############
# ACTIONS##########ACTIONS#######ACTIONS#############


def play_song(voice):
    index = voice.index(languageSaver.language["play"]) + len(languageSaver.language["play"])
    search_term = voice[index:]
    kit.playonyt(search_term)
    engine_speak(
        languageSaver.language["You hear now the song"] + " " + search_term + " " + languageSaver.language["have fun!"])


def time(voice):
    t = ctime().split(" ")[3].split(":")[0:2]
    if t[0] == "00":
        hours = configs.hours
    else:
        hours = t[0]
    minutes = t[1]
    t = "Es ist " + hours + " Uhr " + minutes
    engine_speak(t)


def name(voice):
    engine_speak("Mein name ist " + configs.assis_name)


def hello(voice):
    greetings = ["hey, wie kann ich dir helfen? " + configs.name_of_user, "hey, was geht? " + configs.name_of_user,
                 "hallo " + configs.name_of_user, "hey " + configs.name_of_user]
    greet = greetings[random.randint(0, len(greetings) - 1)]
    engine_speak(greet)


def search_on_google(voice):
    search_term = voice.split("nach")[-1]
    url = "https://google.com/search?q=" + search_term
    webbrowser.get().open(url)
    engine_speak("Das habe ich gefunden nach " + search_term + "auf google")


def youtube(voice):
    search_term = voice.split("nach")[-1]
    url = "https://www.youtube.com/results?search_query=" + search_term
    webbrowser.get().open(url)
    engine_speak("Das habe ich auf youtube nach " + search_term + "gefunden")


def wiki(voice):
    wikipedia.set_lang(configs.pronouncing_language)
    definition = record_audio("Von was brauchst du eine Definition?")
    wiki_eintrag = wikipedia.summary(definition, sentences=configs.length_of_definitions)
    engine_speak(wiki_eintrag)


def send_messages_dc(voice):
    to_user_name = record_audio("An wen soll die Nachricht gesendet werden?")
    to_user = PrivateConfigs.contacts[to_user_name]
    message = record_audio("Was willst du " + to_user_name + " senden?")
    payload = {"content": message}
    header = {'authorization': PrivateConfigs.authorization}
    requests.post(to_user, data=payload, headers=header)
    engine_speak("Ich habe " + to_user_name + " " + message + " gesendet")


def make_todo(voice):
    # todo Mache Todo command
    pass


def game(voice):
    voice_data = record_audio("Entscheide zwischen Papier, Schere oder Stein")
    moves = ["stein", "papier", "schere"]

    cmove = random.choice(moves)
    pmove = voice_data

    engine_speak("Ich hab mich für " + cmove + " entschieden")
    if pmove == cmove:
        engine_speak("Unentschieden")
    elif pmove == "stein" and cmove == "schere":
        engine_speak("Du hast gewonnen")
    elif pmove == "stein" and cmove == "papier":
        engine_speak("Ich habe gewonnen")
    elif pmove == "papier" and cmove == "stein":
        engine_speak("Du hast gewonnen")
    elif pmove == "papierr" and cmove == "schere":
        engine_speak("Ich habe gewonnen")
    elif pmove == "schere" and cmove == "papier":
        engine_speak("Du hast gewonnen")
    elif pmove == "schere" and cmove == "stein":
        engine_speak("Ich habe gewonnen")


def coding_help(voice):
    voice_data = record_audio("Bei was brauchst du coding hilfe?")
    url = "https://stackoverflow.com/questions/tagged/" + voice_data
    webbrowser.get().open(url)


def joke(voice):
    joke = pyjokes.get_joke(language=configs.joke_language, category=configs.joke_art)
    engine_speak(joke)


def rechnung(voice):
    opr = voice.split()[1]

    if opr == '+':
        engine_speak(int(voice.split()[0]) + int(voice.split()[2]))
    elif opr == '-':
        engine_speak(int(voice.split()[0]) - int(voice.split()[2]))
    elif opr == 'mal' or 'x':
        engine_speak(int(voice.split()[0]) * int(voice.split()[2]))
    elif opr == 'geteilt':
        engine_speak(int(voice.split()[0]) / int(voice.split()[2]))
    else:
        engine_speak("Falscher Operator!")


def boring(voice):
    url = "https://theuselessweb.com"
    webbrowser.get().open(url)
    engine_speak("Diese Website vertreibt dir die langweile.")


def open_discord(voice):
    pass


def toss(voice):
    moves = ["kopf", "zahl"]
    cmove = random.choice(moves)
    engine_speak("Die Münze war " + cmove)


def weather(voice):
    API_key = PrivateConfigs.weather_api_key

    lon = PrivateConfigs.lon
    lat = PrivateConfigs.lat

    request_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"
    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        weather_description = data["weather"][0]["description"]
        tempreature = round(data["main"]["temp"] - 273.15)
        engine_speak("Das Wetter ist " + weather_description + ". Und die Temperatur beträgt " + str(
            tempreature) + " Grad Celcius")
    else:
        engine_speak("Ich konnte keine Daten auslesen!")


def quit(voice):
    engine_speak("Bis zum nächsten mal!")
    exit()


def calender_eintrag(voice):
    voice_data = record_audio("Welches Ereignis willst du hinzufügen?")
    new_event = str(voice_data)
    voice_data = record_audio("Wann soll dies Stattfinden?")
    date_of_new_event = str(voice_data)
    match = [x for x in configs.months if x in date_of_new_event]
    # etwas "schickschnack"
    if not match:
        engine_speak("Das ist kein gültiges Datum!")
        return
    else:
        match = match[0]
    month = str(configs.months.index(match) + 1)
    i = date_of_new_event.split('.')
    day = i[0]
    characters = configs.alphabet

    for x in range(len(characters)):
        day = day.replace(characters[x], "")
    finish_calender = str(configs.year + "-" + month + "-" + day + ";" + new_event)
    with open(configs.calender_filename, 'w') as f:
        for line in finish_calender:
            f.write(line)
        f.write('\n')
    print(finish_calender)
    engine_speak("Das Ereignis " + new_event + "wurde hinzugefügt!")


def calender_auslesen(voice):
    todays_ereignisse = 0
    calender_ereignisse = []
    z = 0
    # read the calender_db.txt file
    with open(configs.calender_filename, newline='') as pfile:
        reader = csv.reader(pfile, delimiter=';')
        for row in reader:
            if row:
                i = (row[0], row[1])
                calender_ereignisse.append(i)
    # todays day
    today = str(date.today())
    today = today.split("-")
    year = today[0]
    month = today[1]
    day = today[2]
    month = month.replace("0", "")
    day = day.replace("0", "")
    today = year + "-" + month + "-" + day
    # check date with calender_db.txt
    for i in range(len(calender_ereignisse)):
        object = list(calender_ereignisse[z])
        ereignis_datum = object[0]
        if today == ereignis_datum:
            todays_ereignisse += 1
            if todays_ereignisse > 1:
                engine_speak("und " + object[1])
            else:
                engine_speak("Heute steht im Kalender " + object[1])
        z += 1
    return calender_ereignisse


def help(voice):
    r = randint(0, len(configs.help_asks))
    print(r)
    help_ask = configs.help_asks[r]
    engine_speak(help_ask)


def say_datum(voice):
    locale.setlocale(locale.LC_TIME, locale.normalize("de"))
    today = date.today()
    engine_speak(today.strftime("Es ist %A der %d.%B %Y"))


def training_math(voice):
    engine_speak('Jetzt wird Mathe trainiert.')
    q_a = training_module.get_question_math()
    voice_data = record_audio('Was ist: ' + q_a[0])
    solution = q_a[1]
    if voice_data == solution:
        engine_speak("Richtig!")
    else:
        engine_speak("Die Lösung war " + q_a[1])


def training_latin(voice):
    engine_speak('Jetzt wird Latein trainiert.')
    for i in range(4):
        q_a = training_module.get_question_latin()
        voice_data = record_audio('Was heißt: ' + q_a[0])
        solution = q_a[1]
        if voice_data == solution:
            engine_speak("Richtig!")
        else:
            engine_speak("Die Lösung war " + q_a[1])


def input_system():
    if configs.input_system:
        print("True")
    else:
        print("False")


def say_word(voice):
    speak_word = str(voice.split("sage"))
    speak_word = str(speak_word.replace(",", ""))
    engine_speak(str(speak_word))


def joke_sad(voice):
    engine_speak("Ich empfinde keine Gefühle aber vieleicht heitert dich ein witz auf!")
    joke = pyjokes.get_joke(language=configs.joke_language, category=configs.joke_art)
    engine_speak(joke)


def search_on_frag_caeser(voice):
    search_term = voice.split("latein")[-1]
    url = "https://www.frag-caesar.de/lateinwoerterbuch/" + search_term + "-uebersetzung.html"
    webbrowser.get().open(url)
    engine_speak("Das habe ich gefunden! Ich hoffe es hilft dir weiter!")


def translate_latin_voc_with_frag_caeser(voice):
    print("Suche...")
    search_term = voice.split("übersetze")[-1]
    url = f'https://www.frag-caesar.de/lateinwoerterbuch/%20{search_term}-uebersetzung.html'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    tds = soup.find_all('td', class_="eh2")
    if tds:
        td = tds[0]
        siblings = td.find_next_siblings('td')
        count = 0
        for s in siblings:
            if count == 3:
                uebersetzungen = s.get_text(strip=True, separator='###').split('###')
                print("Alle Übersetzungen: " + str(uebersetzungen))
                engine_speak(search_term + " heißt unter anderem " + uebersetzungen[0])
            count += 1
    else:
        engine_speak("Es tut mir Leid ich konnte dazu nichts finden oder ich habe es nicht korekkt verstanden.")


def show_clipboard(voice):
    # Paste text from the clipboard
    text = pyperclip.paste()
    print(text)
    engine_speak("In deinem Clipboard steht:" + text)


def translate_clipboard(voice):
    text = pyperclip.paste()
    translated = GoogleTranslator(source='auto', target=configs.pronouncing_language).translate(text)
    engine_speak("Es heißt:" + translated)


def restart(voice):
    os.execl(sys.executable, sys.executable, *sys.argv)

# MADE BY BENNO #
