import re
hand = open('assign.txt')
numlist = list()
for line in hand:
	line = line.rstrip()
	stuff = re.findall('[0-9]+',line)
	stuff = map(int,stuff)
	stuff_sum = sum(stuff)
	numlist.append(stuff_sum)

print sum(numlist)
