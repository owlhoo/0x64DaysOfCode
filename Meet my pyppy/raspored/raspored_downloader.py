from bs4 import BeautifulSoup
import requests
import urllib.request

url = 'http://www.np.ac.rs/yu/raspored-predavanja-teh'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

container = soup.find_all('div', {'class': 'highslide-gallery'})[0]
links = container.find_all('a')

path = None

for link in links:
    if link.text == 'Softversko inženjersvo':
        path = link['href']

full_url = 'http://www.np.ac.rs' + path

with open("url.txt", "w") as file:
    file.write(full_url)

urllib.request.urlretrieve(full_url, 'raspored.pdf')
