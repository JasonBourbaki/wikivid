import requests
from gtts import gTTS
from googletrans import Translator
from bs4 import BeautifulSoup
import spice as sp

SECTION_LEN = 30
translator = Translator()
htp = 'https://'
urlstem = '.wikipedia.org/wiki/'
langlib = {
    'english': 'en',
    'french': 'fr',
    'german': 'de',
    'portuguese': 'pt',
    'spanish': 'es',
    'italian': 'it'
}

lang = translator.translate(input('Enter language here: '), dest='en').text.lower()
key = translator.translate(input('Enter keyword here: '), dest=langlib.get(lang)).text.title()
link = htp + langlib.get(lang) + urlstem + key.replace(" ", "_")

response = requests.get(link)
soup = BeautifulSoup(response.text, 'lxml')
text = sp.textify(BeautifulSoup(sp.get_urls(soup), 'lxml'))
textwURL = sp.tokenize_urls(sp.get_urls(soup).split(' '))

print(textwURL)

#Processing the intro section into a mp3 file
tts = gTTS(text, lang = langlib.get(lang))
tts.save('sound.mp3')
