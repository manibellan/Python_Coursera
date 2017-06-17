import urllib
import xml.etree.ElementTree as ET

count_list = list()

url = raw_input('Enter the URL :')

page = urllib.urlopen(url)

tree = ET.parse(page)

comments = tree.findall('comments/comment')

for comment in comments:
	count_list.append(int(comment.find('count').text))

print sum(count_list)
