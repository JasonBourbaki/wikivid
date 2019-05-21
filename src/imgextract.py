from sklearn.feature_extraction.text import TfidfVectorizer
from bs4 import BeautifulSoup
import wikipedia
import requests
import random
import pyphen
import os
from urllib import request
from PIL import Image
import spice as sp

textwURL = ['Napoléon', 'Bonaparte', 'was', 'a', 'French', 'statesman', 'and', 'military', 'leader', 'of', '<a href="/wiki/Italians" title="Italians"> Italian </a>', 'descent', 'who', 'rose', 'to', 'prominence', 'during', 'the', '<a href="/wiki/French_Revolution" title="French Revolution"> French Revolution </a>', 'and', 'led', '<a class="mw-redirect" href="/wiki/Napoleon_Bonaparte%27s_battle_record" title="Napoleon Bonaparte\'s battle record"> several successful campaigns </a>', 'during', 'the', '<a href="/wiki/French_Revolutionary_Wars" title="French Revolutionary Wars"> French Revolutionary Wars </a>.', 'He', 'was', '<a href="/wiki/Emperor_of_the_French" title="Emperor of the French"> Emperor of the French </a>', 'as', 'Napoleon', 'I', 'from', '1804', 'until', '1814', 'and', 'again', 'briefly', 'in', '1815', 'during', 'the', '<a href="/wiki/Hundred_Days" title="Hundred Days"> Hundred Days </a>.', 'Napoleon', 'dominated', 'European', 'and', 'global', 'affairs', 'for', 'more', 'than', 'a', 'decade', 'while', 'leading', 'France', 'against', 'a', 'series', 'of', 'coalitions', 'in', 'the', '<a href="/wiki/Napoleonic_Wars" title="Napoleonic Wars"> Napoleonic Wars </a>.', 'He', 'won', 'most', 'of', 'these', 'wars', 'and', 'the', 'vast', 'majority', 'of', 'his', 'battles,', 'building', 'a', '<a href="/wiki/First_French_Empire" title="First French Empire"> large empire </a>', 'that', 'ruled', 'over', 'much', 'of', 'continental', 'Europe', 'before', 'its', 'final', 'collapse', 'in', '1815.', 'He', 'is', 'considered', 'one', 'of', 'the', 'greatest', 'commanders', 'in', 'history,', 'and', 'his', 'wars', 'and', 'campaigns', 'are', 'studied', 'at', 'military', 'schools', 'worldwide.', "Napoleon's", 'political', 'and', 'cultural', 'legacy', 'has', 'endured', 'as', 'one', 'of', 'the', 'most', 'celebrated', 'and', 'controversial', 'leaders', 'in', 'human', 'history.', 'He', 'was', 'born', 'in', '<a href="/wiki/Corsica" title="Corsica"> Corsica </a>', 'to', 'a', 'relatively', 'modest', 'family', 'of', '<a href="/wiki/Italians" title="Italians"> Italian </a>', 'origin', 'from', 'minor', '<a href="/wiki/Nobility_of_Italy" title="Nobility of Italy"> nobility </a>.', 'He', 'was', 'serving', 'as', 'an', 'artillery', 'officer', 'in', 'the', 'French', 'army', 'when', 'the', 'French', 'Revolution', 'erupted', 'in', '1789.', 'He', 'rapidly', 'rose', 'through', 'the', 'ranks', 'of', 'the', 'military,', 'seizing', 'the', 'new', 'opportunities', 'presented', 'by', 'the', 'Revolution', 'and', 'becoming', 'a', 'general', 'at', 'age', '24.', 'The', '<a href="/wiki/French_Directory" title="French Directory"> French Directory </a>', 'eventually', 'gave', 'him', 'command', 'of', 'the', '<a href="/wiki/Army_of_Italy_" title="Army of Italy "> Army of Italy </a>', 'after', 'he', 'suppressed', 'a', '<a href="/wiki/13_Vend%C3%A9miaire" title="13 Vendémiaire"> revolt against the government </a>', 'from', 'royalist', 'insurgents.', 'At', 'age', '26,', 'he', 'began', 'his', '<a href="/wiki/Italian_campaigns_of_the_French_Revolutionary_Wars" title="Italian campaigns of the French Revolutionary Wars"> first military campaign </a>', 'against', 'the', 'Austrians', 'and', 'the', 'Italian', 'monarchs', 'aligned', 'with', 'the', 'Habsburgs—winning', 'virtually', 'every', 'battle,', 'conquering', 'the', 'Italian', 'Peninsula', 'in', 'a', 'year', 'while', 'establishing"', '<a href="/wiki/Sister_republic" title="Sister republic"> sister republics </a>"', 'with', 'local', 'support,', 'and', 'becoming', 'a', 'war', 'hero', 'in', 'France.', 'In', '1798,', 'he', 'led', 'a', '<a href="/wiki/French_campaign_in_Egypt_and_Syria" title="French campaign in Egypt and Syria"> military expedition to Egypt </a>', 'that', 'served', 'as', 'a', 'springboard', 'to', 'political', 'power.', 'He', 'orchestrated', 'a', '<a href="/wiki/Coup_of_18_Brumaire" title="Coup of 18 Brumaire"> coup in November 1799 </a>', 'and', 'became', '<a href="/wiki/French_Consulate" title="French Consulate"> First Consul </a>', 'of', 'the', 'Republic.', "Napoleon's", 'ambition', 'and', 'public', 'approval', 'inspired', 'him', 'to', 'go', 'further,', 'and', 'he', 'became', 'the', 'first', 'Emperor', 'of', 'the', 'French', 'in', '1804.', 'Intractable', 'differences', 'with', 'the', 'British', 'meant', 'that', 'the', 'French', 'were', 'facing', 'a', '<a href="/wiki/War_of_the_Third_Coalition" title="War of the Third Coalition"> Third Coalition </a>', 'by', '1805.', 'Napoleon', 'shattered', 'this', 'coalition', 'with', 'decisive', 'victories', 'in', 'the', '<a href="/wiki/Ulm_Campaign" title="Ulm Campaign"> Ulm Campaign </a>', 'and', 'a', 'historic', 'triumph', 'over', 'the', '<a href="/wiki/Russian_Empire" title="Russian Empire"> Russian Empire </a>', 'and', '<a href="/wiki/Austrian_Empire" title="Austrian Empire"> Austrian Empire </a>', 'at', 'the', '<a href="/wiki/Battle_of_Austerlitz" title="Battle of Austerlitz"> Battle of Austerlitz </a>', 'which', 'led', 'to', 'the', '<a href="/wiki/Dissolution_of_the_Holy_Roman_Empire" title="Dissolution of the Holy Roman Empire"> dissolution of the Holy Roman Empire </a>.', 'In', '1806,', 'the', '<a href="/wiki/War_of_the_Fourth_Coalition" title="War of the Fourth Coalition"> Fourth Coalition </a>', 'took', 'up', 'arms', 'against', 'him', 'because', '<a href="/wiki/Kingdom_of_Prussia" title="Kingdom of Prussia"> Prussia </a>', 'became', 'worried', 'about', 'growing', 'French', 'influence', 'on', 'the', 'continent.', 'Napoleon', 'quickly', 'defeated', 'Prussia', 'at', 'the', '<a href="/wiki/Battle_of_Jena%E2%80%93Auerstedt" title="Battle of Jena–Auerstedt"> battles of Jena and Auerstedt </a>,', 'then', 'marched', 'his', '<a href="/wiki/Grande_Arm%C3%A9e" title="Grande Armée"> Grande Armée </a>', 'deep', 'into', '<a href="/wiki/Eastern_Europe" title="Eastern Europe"> Eastern Europe </a>', 'and', 'annihilated', 'the', 'Russians', 'in', 'June', '1807', 'at', 'the', '<a href="/wiki/Battle_of_Friedland" title="Battle of Friedland"> Battle of Friedland </a>.', 'France', 'then', 'forced', 'the', 'defeated', 'nations', 'of', 'the', 'Fourth', 'Coalition', 'to', 'sign', 'the', '<a href="/wiki/Treaties_of_Tilsit" title="Treaties of Tilsit"> Treaties of Tilsit </a>', 'in', 'July', '1807,', 'bringing', 'an', 'uneasy', 'peace', 'to', 'the', 'continent.', 'Tilsit', 'signified', 'the', 'high-water', 'mark', 'of', 'the', 'French', 'Empire.', 'In', '1809,', 'the', 'Austrians', 'and', 'the', 'British', 'challenged', 'the', 'French', 'again', 'during', 'the', '<a href="/wiki/War_of_the_Fifth_Coalition" title="War of the Fifth Coalition"> War of the Fifth Coalition </a>,', 'but', 'Napoleon', 'solidified', 'his', 'grip', 'over', 'Europe', 'after', 'triumphing', 'at', 'the', '<a href="/wiki/Battle_of_Wagram" title="Battle of Wagram"> Battle of Wagram </a>', 'in', 'July.', 'Napoleon', 'then', 'invaded', 'the', '<a href="/wiki/Iberian_Peninsula" title="Iberian Peninsula"> Iberian Peninsula </a>,', 'hoping', 'to', 'extend', 'the', '<a href="/wiki/Continental_System" title="Continental System"> Continental System </a>', 'and', 'choke', 'off', 'British', 'trade', 'with', 'the', 'European', 'mainland,', 'and', 'declared', 'his', 'brother', '<a href="/wiki/Joseph_Bonaparte" title="Joseph Bonaparte"> Joseph Bonaparte </a>', 'the', '<a class="mw-redirect" href="/wiki/King_of_Spain" title="King of Spain"> King of Spain </a>', 'in', '1808.', 'The', 'Spanish', 'and', 'the', 'Portuguese', 'revolted', 'with', 'British', 'support.', 'The', '<a href="/wiki/Peninsular_War" title="Peninsular War"> Peninsular War </a>', 'lasted', 'six', 'years,', 'featured', 'extensive', '<a href="/wiki/Guerrilla_warfare" title="Guerrilla warfare"> guerrilla warfare </a>,', 'and', 'ended', 'in', 'victory', 'for', 'the', 'Allies', 'against', 'Napoleon.', 'The', 'Continental', 'System', 'caused', 'recurring', 'diplomatic', 'conflicts', 'between', 'France', 'and', 'its', 'client', 'states,', 'especially', 'Russia.', 'The', 'Russians', 'were', 'unwilling', 'to', 'bear', 'the', 'economic', 'consequences', 'of', 'reduced', 'trade', 'and', 'routinely', 'violated', 'the', 'Continental', 'System,', 'enticing', 'Napoleon', 'into', 'another', 'war.', 'The', 'French', 'launched', 'a', 'major', '<a href="/wiki/French_invasion_of_Russia" title="French invasion of Russia"> invasion of Russia </a>', 'in', 'the', 'summer', 'of', '1812.', 'The', 'campaign', 'destroyed', 'Russian', 'cities,', 'but', 'did', 'not', 'yield', 'the', 'decisive', 'victory', 'Napoleon', 'wanted.', 'It', 'resulted', 'in', 'the', 'collapse', 'of', 'the', 'Grande', 'Armée', 'and', 'inspired', 'a', 'renewed', 'push', 'against', 'Napoleon', 'by', 'his', 'enemies.', 'In', '1813,', 'Prussia', 'and', 'Austria', 'joined', 'Russian', 'forces', 'in', 'the', '<a href="/wiki/War_of_the_Sixth_Coalition" title="War of the Sixth Coalition"> War of the Sixth Coalition </a>', 'against', 'France.', 'A', 'lengthy', 'military', 'campaign', 'culminated', 'in', 'a', 'large', 'Allied', 'army', 'defeating', 'Napoleon', 'at', 'the', '<a href="/wiki/Battle_of_Leipzig" title="Battle of Leipzig"> Battle of Leipzig </a>', 'in', 'October', '1813,', 'but', 'his', 'tactical', 'victory', 'at', 'the', 'minor', '<a href="/wiki/Battle_of_Hanau" title="Battle of Hanau"> Battle of Hanau </a>', 'allowed', 'retreat', 'onto', 'French', 'soil.', 'The', 'Allies', 'then', '<a class="mw-redirect" href="/wiki/1814_campaign_in_France" title="1814 campaign in France"> invaded France </a>', 'and', 'captured', 'Paris', 'in', 'the', 'spring', 'of', '1814,', 'forcing', 'Napoleon', 'to', 'abdicate', 'in', 'April.', 'He', 'was', 'exiled', 'to', 'the', 'island', 'of', '<a href="/wiki/Elba" title="Elba"> Elba </a>', 'off', 'the', 'coast', 'of', '<a href="/wiki/Tuscany" title="Tuscany"> Tuscany </a>,', 'and', 'the', '<a class="mw-redirect" href="/wiki/Bourbon_dynasty" title="Bourbon dynasty"> Bourbon dynasty </a>', 'was', '<a href="/wiki/Bourbon_Restoration" title="Bourbon Restoration"> restored to power </a>.', 'Napoleon', 'escaped', 'from', 'Elba', 'in', 'February', '1815', 'and', 'took', 'control', 'of', 'France', 'once', 'again.', 'The', 'Allies', 'responded', 'by', 'forming', 'a', '<a class="mw-redirect" href="/wiki/War_of_the_Seventh_Coalition" title="War of the Seventh Coalition"> Seventh Coalition </a>', 'which', 'defeated', 'him', 'at', 'the', '<a href="/wiki/Battle_of_Waterloo" title="Battle of Waterloo"> Battle of Waterloo </a>', 'in', 'June.', 'The', 'British', 'exiled', 'him', 'to', 'the', 'remote', 'island', 'of', '<a href="/wiki/Saint_Helena" title="Saint Helena"> Saint Helena </a>', 'in', 'the', 'South', 'Atlantic,', 'where', 'he', 'died', 'six', 'years', 'later', 'at', 'the', 'age', 'of', '51.', "Napoleon's", 'influence', 'on', 'the', 'modern', 'world', 'brought', 'liberal', 'reforms', 'to', 'the', 'numerous', 'territories', 'that', 'he', 'conquered', 'and', 'controlled,', 'such', 'as', 'the', '<a href="/wiki/Low_Countries" title="Low Countries"> Low Countries </a>,', '<a href="/wiki/Switzerland" title="Switzerland"> Switzerland </a>,', 'and', 'large', 'parts', 'of', 'modern', '<a href="/wiki/Italy" title="Italy"> Italy </a>', 'and', '<a href="/wiki/Germany" title="Germany"> Germany </a>.', 'He', 'implemented', 'fundamental', 'liberal', 'policies', 'in', 'France', 'and', 'throughout', 'Western', 'Europe.', 'His', '<a href="/wiki/Napoleonic_Code" title="Napoleonic Code"> Napoleonic Code </a>', 'has', 'influenced', 'the', 'legal', 'systems', 'of', 'more', 'than', '70', 'nations', 'around', 'the', 'world.', 'British', 'historian', '<a href="/wiki/Andrew_Roberts_" title="Andrew Roberts "> Andrew Roberts </a>', 'states:', '"The', 'ideas', 'that', 'underpin', 'our', 'modern', 'world—meritocracy,', 'equality', 'before', 'the', 'law,', 'property', 'rights,', 'religious', 'toleration,', 'modern', 'secular', 'education,', 'sound', 'finances,', 'and', 'so', 'on—were', 'championed,', 'consolidated,', 'codified', 'and', 'geographically', 'extended', 'by', 'Napoleon.', 'To', 'them', 'he', 'added', 'a', 'rational', 'and', 'efficient', 'local', 'administration,', 'an', 'end', 'to', 'rural', 'banditry,', 'the', 'encouragement', 'of', 'science', 'and', 'the', 'arts,', 'the', 'abolition', 'of', 'feudalism', 'and', 'the', 'greatest', 'codification', 'of', 'laws', 'since', 'the', '<a class="mw-redirect" href="/wiki/Fall_of_the_Roman_Empire" title="Fall of the Roman Empire"> fall of the Roman Empire </a>', '".', '']

SECTION = 55
vect = TfidfVectorizer(min_df=1)

# Split the tokenized list of wikipedia content into segments of roughly SECTION number of syllables
# and group the urls within each segment together
def segmentize (linkList, lang):
    urls = []
    nums = []

    tStamp = []
    n = 0

    alt = lang + '_' + lang.upper()
    try:
        hyphenator = pyphen.Pyphen(lang = lang)
    except:
        hyphenator = pyphen.Pyphen(lang=alt)

    for token in linkList:
        if '</a>' in token:
            aktvToken = BeautifulSoup(token, 'lxml')
            link = aktvToken.find('a')['href']
            tStamp.append(link)
            text = aktvToken.text
            for word in text:
                n += hyphenator.inserted(word).count('-') + 1
        else:
            n += hyphenator.inserted(token).count('-') + 1
        if n >= SECTION and not tStamp == []:
            nums.append(n)
            n = 0
            urls.append(tStamp)
            tStamp = []
    segments = {'urls': urls, 'nums': nums}
    return segments

# Find the most relevant url in each segment
def relev(segments, og, stem):
    processedKeys = []
    for seg in segments:
        mx = 0
        if len(seg) == 1:
            pass
        else:
            indices = []
            for key in seg:
                link = stem + key
                response = requests.get(link)
                soup = BeautifulSoup(response.text, 'lxml')
                txt = sp.get_content(soup)
                tfidf = vect.fit_transform([og, txt])
                cosim = (tfidf * tfidf.T).A[0][1]
                indices.append(cosim)
            mx = indices.index(max(indices))
        key = seg[mx][6:].replace('_', ' ')
        processedKeys.append(key)
    return processedKeys

def download(imgLinks):
    id = 0
    for link in imgLinks:
        title = str(id)+link[link.rfind('.'):]
        request.urlretrieve(link, '../img/'+title)
        original = Image.open('../img/'+title)
        os.remove('../img/'+title)
        original.save('../img/'+str(id)+'jpeg')
        id += 1

def extract(linkList, ogk, ogt, stem):
    ogp = wikipedia.page(ogk)
    selected = []
    ogAlbum = ogp.images
    album = [ogAlbum[0]]
    segments = segmentize(linkList, stem[8:10])
    linkSeg = segments.get('urls')[1:]
    processedKeys = relev(linkSeg, ogt, stem)
    for key in processedKeys:
        page = wikipedia.page(key)
        if not page.images == []:
            album.append(page.images[0])
        else:
            it = True
            while(it):
                rad = random.randint(len(ogAlbum))
                if rad not in selected:
                    album.append(ogAlbum[rad])
                    selected.append(rad)
                    it = False
    download(album)
    return segments.get('nums')

