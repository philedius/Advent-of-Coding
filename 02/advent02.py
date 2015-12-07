f = open('02a.txt')

def paper():

	total_square_feet = 0

	for line in f:
		sizes = line.split('x')
		
		for i in range(3):
			sizes[i] = int(sizes[i])

		areas = [sizes[0] * sizes[1], sizes[1] * sizes[2], sizes[2] * sizes[0]]
		square_feet = (2 * areas[0]) + (2 * areas[1]) + (2 * areas[2]) + min(areas)
		
		total_square_feet += square_feet

	print total_square_feet


def ribbons():
	total_feet = 0

	for line in f:
		sizes = line.split('x')
		
		for i in range(3):
			sizes[i] = int(sizes[i])

		feet = 0

		bow = reduce(lambda x, y: x*y, sizes)

		sizes.remove(max(sizes))

		ribbon = sizes[0] * 2 + sizes[1] * 2

		feet = bow + ribbon
		total_feet += feet
	print total_feet

ribbons()