import urllib
from BeautifulSoup import *

url = raw_input('Enter the Website: ')
count = int(raw_input('Enter the count: '))
position = int(raw_input('Enter the position: '))

name_list = list()

while count > 0:
	print(url )
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)

	tags = soup('a')
	last_name = tags[position-1].string
	name_list.append(last_name)

	#Reassign the URL to the latest URL and reduce count
	url = tags[position-1].get('href',None)
	count = count - 1

print name_list[-1]
