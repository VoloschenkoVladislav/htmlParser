from urllib.request import urlopen
from bs4 import BeautifulSoup
from typing import List

def getTextFromHtml(
    urls: List[str],
    filename: str,
    divider: str = ';'
):
    '''
    Getting text from page by url
    ---
    ---
    Arguments:
    * ulrs: List[str] - url of the page from which the data will be received
    * filename: str - name of file to which data will be written
    * divider: str = ';' - divider of .csv file (';' by default)
    '''

    file = open('{}.csv'.format(filename), 'w', encoding="utf-8")
    for url in urls:
        html = urlopen(url).read()
        soup = BeautifulSoup(html, features="html.parser")
        try:
            text = soup.body.get_text(divider, strip=True)
        except AttributeError:
            continue
        file.write(url + ':' + divider + text + '\n')

    file.close()
    