from urllib.request import urlopen
from bs4 import BeautifulSoup
import typing

def getTextFromHtml(
    url: str,
    filename: str,
    orientationColumn: bool = True 
):
    '''
    Getting text from page by url
    ---
    ---
    Arguments:
    * ulr: str - url of the page from which the data will be received
    * filename: str - name of file to which data will be written
    * orientationColumn: bool = True - if True, the data will be written in a column, otherwise in a row
    '''
    file = open('{}.csv'.format(filename), 'w', encoding="utf-8")
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")
    text = soup.body.get_text()
    
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    divider = '\n' if orientationColumn else ';'
    for l in chunks:
        if l: file.write(l + divider)

    file.close()
    