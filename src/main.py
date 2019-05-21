import requests
from gtts import gTTS
from googletrans import Translator
from bs4 import BeautifulSoup
import spice as sp
import imgextract as ie

translator = Translator()
htp = 'https://'
root = '.wikipedia.org'
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
stem = htp + langlib.get(lang) + root
link = stem + '/wiki/' + key.replace(" ", "_")

response = requests.get(link)
soup = BeautifulSoup(response.text, 'lxml')
text = sp.textify(BeautifulSoup(sp.get_urls(soup), 'lxml'))
textwURL = sp.tokenize_urls(sp.get_urls(soup).split(' '))
og = sp.get_content(soup)
segments = ie.segmentize(textwURL, langlib.get(lang)).get('urls')
print(segments)
relevURL = ie.relev(segments, og, stem)
# imgs = ie.extract(textwURL)

#Processing the intro section into a mp3 file
tts = gTTS(text, lang = langlib.get(lang))
tts.save('sound.mp3')
