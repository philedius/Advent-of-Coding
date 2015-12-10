def look_and_say(number):
	new_number = ''
	count = 0
	current_number = ''
	for n in str(number):
		if n != current_number:
			if count != 0:
				new_number += str(count) + current_number
			current_number = n
			count = 1
		else:
			count += 1

	new_number += str(count) + current_number
	
	return new_number

number = 1113222113

for i in range(50):
	number = look_and_say(number)

print len(str(number))