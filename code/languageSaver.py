import configs

# read language
language = {}
if configs.pronouncing_language == "de":
    list = open('../languages/de.txt').read().split("\n")
if configs.pronouncing_language == "en":
    list = open('../languages/eng.txt').read().split("\n")

for i in range(len(list)):
    spliting = list[i].split(":")
    key = spliting[0]
    value = spliting[1]
    language.update({key: value})

langauge = language
