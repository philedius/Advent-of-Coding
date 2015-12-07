def number_of_houses_visited():
	count = 0
	x = 0
	y = 0
	visited = [[0 for i in range(1000)] for i in range(1000)]
	f = open('03.txt', 'r')
	for line in f:
		for d in line:
			visited[x][y] += 1
			if d == '^':
				y += 1
				continue
			if d == 'v':
				y -= 1
				continue
			if d == '<':
				x -= 1
				continue
			if d == '>':
				x += 1
				continue

	visited[x][y] += 1


	for x in visited:
		for y in x:
			if y > 0:
				count += 1

	print count


def robo_santa():
	count = 0
	turn = 0
	x = 0
	y = 0
	robo_x = 0
	robo_y = 0
	visited = [[0 for i in range(1000)] for i in range(1000)]
	f = open('03.txt', 'r')
	for line in f:
		for d in line:
			visited[x][y] += 1
			visited[robo_x][robo_y] += 1

			if turn % 2 == 0: # Santa
				turn += 1
				if d == '^':
					y += 1
					continue
				if d == 'v':
					y -= 1
					continue
				if d == '<':
					x -= 1
					continue
				if d == '>':
					x += 1
					continue
			else: #Robo Santa
				turn += 1
				if d == '^':
					robo_y += 1
					continue
				if d == 'v':
					robo_y -= 1
					continue
				if d == '<':
					robo_x -= 1
					continue
				if d == '>':
					robo_x += 1
					continue
				


	visited[x][y] += 1
	visited[robo_x][robo_y] += 1


	for x in visited:
		for y in x:
			if y > 0:
				count += 1

	print count

robo_santa()