import re

def rmv_parens(text):
    n = 1
    while n:
        text, n = re.subn(r'\([^()]*\)', '', text)
    text = ' '.join(text.split())
    text = re.sub(r'\s([?.,!"](?:\s|$))', r'\1', text)
    return text

def get_urls(soup):
    textwURL = ''
    body = soup.find('div', {'class': 'mw-parser-output'})
    list = body.findAll(['p','div'], recursive=False)
    for tag in list:
        if tag.name == 'p' and not tag.has_attr('class'):
            for sup in tag.findAll('sup'):
                sup.extract()
            for ele in tag.findAll():
                if ele.name != 'a':
                    ele.replaceWithChildren()
            text = rmv_parens(tag.prettify())
            textwURL += text + ' '
        elif tag.find('div', {'class': 'toctitle'}) != None:
            break
    return textwURL

def tokenize_urls(list):
    urlList = []
    link = ''
    for word in list:
        if '<a' in word or '<a' in link:
            link += word + ' '
            if '</a>' in link:
                urlList.append(link.strip())
                link = ''
            continue
        elif not ('<p>' in word or '</p>' in word or '<b>' in word or '</b>' in word):
            urlList.append(word)
        else:
            pass
    return urlList

def textify(tag):
    for a in tag.findAll('a'):
        a.replaceWithChildren()
    return rmv_parens(tag.getText())