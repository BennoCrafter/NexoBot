from NexoActions import *
import os
from Intend import Intend
import languageSaver

# read the file
def read_intends(intend_filename):
    my_intends = []
    with open(intend_filename, newline='') as pfile:
        reader = csv.reader(pfile, delimiter=';')
        for row in reader:
            if row:
                i = Intend(row[0], row[1])
                if len(row) > 2:
                    i.action_param = row[2]
                my_intends.append(i)
    return my_intends


def respond(voice, intends):
    if voice:
        for intend in intends:
            if intend.match(voice):
                intend.execute(voice)
                return
        engine_speak(languageSaver.language["I'm sorry! I don't know this command yet or I didn't understand it!"])
        if not configs.developer_mode:
            print(voice)


def dialog_loop(intends):
    dialog_happened = True
    while True:
        voice_data = record_audio("", dialog_happened)  # get the voice input
        if voice_data:
            dialog_happened = True
        else:
            dialog_happened = False
        respond(voice_data, intends)


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


#########################
clearConsole()
intends = read_intends(configs.intend_filename)
dialog_loop(intends)

# MADE BY BENNO #
