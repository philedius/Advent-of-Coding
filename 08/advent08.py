import re

f = open('08.txt', 'r')
code_strings = []
actual_strings = []
stringified_strings = []
total_code_char = 0
total_actual_char = 0
total_stringified_char = 0

for line in f:
	line = line.strip('\n')
	actual_strings.append(eval(line))
	code_strings.append(line)
	stringified_strings.append(re.escape(line))

for string in code_strings:
	for char in string:
		total_code_char += 1

for string in actual_strings:
	for char in string:
		total_actual_char += 1

# Super cheesed
for string in stringified_strings:
	total_stringified_char += 2
	for char in string:
		total_stringified_char += 1

print 'Solution (a) is: ' + str(total_code_char - total_actual_char)
print 'Solution (b) is: ' + str(total_stringified_char - total_code_char)