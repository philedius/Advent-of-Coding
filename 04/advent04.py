import hashlib

is_valid = False
number = 0

while is_valid == False:
	m = hashlib.md5()
	m.update('iwrupvqb')
	m.update(str(number))
	if m.hexdigest()[0:6] == '000000':
		print m.hexdigest()
		print number
		is_valid = True
	number += 1