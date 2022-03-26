import requests
import pyttsx3

wordinp = input(str("Word:\n")).lower()
converter = pyttsx3.init()
voices = converter.getProperty('voices')
converter.setProperty('rate', 125)
converter.setProperty('volume', 100)
converter.setProperty('voice', voices[0].id)
try:
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/" + wordinp

    response = requests.get(url)

    meaning = response.json()[0]["meanings"][0]["definitions"][0]["definition"]
    converter.say(meaning)
    converter.runAndWait()
    print(meaning)

except KeyError:
    print("Sorry, the word is not in the dictionary. Please check the spelling")
    converter.say("Sorry, the word is not in the dictionary. Please check the spelling")
    converter.runAndWait()