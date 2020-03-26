import requests
import os
import bs4
from PIL import Image

#Using the URL for Random post bar
url = 'http://zenpencils.com/?randompost'

#Using requests library and beautifulsoup to get relevant html header
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, features="html5lib")


#Get the <img> element under <div> id=comic
comicElem = soup.select('#comic img')
if comicElem == []:
	print('Could not find image')
else :
	comicUrl = comicElem[0].get('src')
	res = requests.get(comicUrl)
	res.raise_for_status()


#Downloading comic in ./img/ directory
comicName = os.path.basename(comicUrl)
print('Downloading comic named %s...' % comicName)
imageFile = open(os.path.join('img',os.path.basename(comicUrl)), 'wb')
for chunk in res.iter_content(1000000):
	imageFile.write(chunk)
imageFile.close()


#Opening image using xdg-open command which opens in default image viewer
im = 'xdg-open img/' + comicName
os.system(im)

print('Download complete !\nOpening image in default image viewer.')
