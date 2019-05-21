import requests
from gtts import gTTS
from googletrans import Translator
from bs4 import BeautifulSoup
import wave
import contextlib
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

tts = gTTS(text, lang = langlib.get(lang))
tts.save('sound.wav')

textwURL = sp.tokenize_urls(sp.get_urls(soup).split(' '))
og = sp.get_content(soup)
temprop = ie.extract(textwURL, key, og, stem)

sum = 0
for temp in temprop:
    sum += temp

audioLen = 0
with contextlib.closing(wave.open('sound.wav','r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    audioLen = frames / float(rate)

tempTrue = []
for temp in temprop:
    tempTrue.append(audioLen*(temp/sum))



#Processing the intro section into a mp3 file