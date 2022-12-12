import re

texte = open('../txt/LateinVokabeln.txt').read().split("\n")
pattern = r"\w(\s+)\w"


for text in texte:
    deutsch = ""
    latein = ""
    match = re.search(pattern, text)
    if match:
        index = match.start()
        la = text[:index+1].strip()
        de = text[index+2:].strip()
        if ', ' in de:
            deutsch = re.split(', ', de)
        else:
            deutsch = [de]
        print(la, " <> ", str(deutsch))