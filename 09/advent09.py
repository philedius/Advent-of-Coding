from itertools import permutations

distances = {}
places = []
shortest_distance = 100000
longest_distance = 0
lines = open('09.txt').read().splitlines()

for line in lines:
	distance = line.split()
	distance[4] = int(distance[4])
	
	if distance[0] not in distances:
		distances[distance[0]] = {}
	distances[distance[0]][distance[2]] = distance[4]
	
	if distance[2] not in distances:
		distances[distance[2]] = {}
	distances[distance[2]][distance[0]] = distance[4]

	if distance[2] not in places:
		places.append(distance[2])
	if distance[0] not in places:
		places.append(distance[0])


for item in list(permutations(places)):
	distance = 0
	for i in range(len(places) - 1):
		distance += distances[item[i]][item[i+1]]

	if distance < shortest_distance:
		shortest_distance = distance

	if distance > longest_distance:
		longest_distance = distance

print 'Shortest distance:', shortest_distance
print 'Longest distance:', longest_distance