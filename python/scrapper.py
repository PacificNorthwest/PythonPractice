from bs4 import BeautifulSoup as soup
import urllib.request
import shutil

def predicate(src):
    return 'prototypodesign' in src

with open('page.html', 'r') as file:
    dom = soup(file.read(), features='html5lib')
    images = dom.find_all('img', { 'src': predicate })
    images = [i['src'] for i in images]

    for img in images:
        print(f'Processing {img}')
        with urllib.request.urlopen(img) as response, open(f'./images/{img[img.rfind("/") + 1:]}', 'wb') as file:
            shutil.copyfileobj(response, file)