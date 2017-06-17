import urllib
from BeautifulSoup import *

url = raw_input('Enter the Website: ')

url_list = list()

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('span')

for tag in tags:
    url_list.append(int(tag.string))

print sum(url_list)
