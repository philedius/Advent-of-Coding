import re
light_grid = [[0 for x in range(1000)] for x in range(1000)]
f = open('06.txt', 'r')

def turn_on(start, end):

	for i in range(start[0], end[0]+1):
		for j in range(start[1], end[1]+1):
			light_grid[i][j] = 1

	print 'turn on ' + str(start) + ' to ' + str(end)

def turn_off(start, end):

	for i in range(start[0], end[0]+1):
		for j in range(start[1], end[1]+1):
			light_grid[i][j] = 0

	print 'turn off ' + str(start) + ' to ' + str(end)

def toggle(start, end):

	for i in range(start[0], end[0]+1):
		for j in range(start[1], end[1]+1):
			if light_grid[i][j] == 0:
				light_grid[i][j] = 1
			elif light_grid[i][j] == 1:
				light_grid[i][j] = 0

	print 'toggle ' + str(start) + ' to ' + str(end)

def get_values(line):
		operation = line[0:7].strip()
		if operation == 'turn of':
			operation += 'f'
		numbers = [int(s) for s in re.findall(r'\d+', line)]
		start = (numbers[0], numbers[1])
		end = (numbers[2], numbers[3])
		return operation, start, end


def follow_instructions():
	for line in f:
		operation, start, end = get_values(line)
		
		if operation == 'turn on':
			turn_on(start, end)

		if operation == 'turn off':
			turn_off(start, end)

		if operation == 'toggle':
			toggle(start, end)

	lit_count = 0
			
	for i in range(1000):
		for j in range(1000):
			if light_grid[i][j] == 1:
				lit_count += 1

	print lit_count


follow_instructions()