import re

f = open('05.txt', 'r')
count = 0

# for line in f:
# 	if re.search(r'((\w)\2)', line):
# 		if re.search('[aeiou].*[aeiou].*[aeiou]', line):
# 			if re.search('ab|cd|pq|xy', line):
# 				continue
# 			else:
# 				count += 1
# 				print line,


for line in f:
	if re.search(r'((([a-z][a-z]).*)\3)', line):
		if re.search(r'(([a-z]).\2)', line):
			count += 1
			print line,

print count