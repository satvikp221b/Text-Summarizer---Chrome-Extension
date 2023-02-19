import spacy
import requests
from bs4 import BeautifulSoup
url = "https://www.sciencedaily.com/releases/2023/01/230113112749.htm"
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text=True)
print(set([t.parent.name for t in text]))
output = ''
blacklist = [
    '[document]',
   'noscript',
    'header',
    'html',
    'meta',
    'head', 
    'input',
    'script',
    'img',
    'style',
    'label',
    'h1',
    'button',
    'a',
    'time',
    'b',
    'h2',
    'h4',
    'span',
    'div',
    'strong'
    
    # there may be more elements you don't want, such as "style", etc.
]

for t in text:
    if t.parent.name not in blacklist:
        output += '{} '.format(t)