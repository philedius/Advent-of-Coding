import re
f = open('07.txt', 'r')
variables = {}
circuit = []

for command in f:
	temp = command
	temp = temp.strip('\n')
	temp = temp.replace('AND', '&')
	temp = temp.replace('OR', '|')
	temp = temp.replace('NOT', '~')
	temp = temp.replace('LSHIFT', '<<')
	temp = temp.replace('RSHIFT', '>>')
	circuit.append(temp)

circuit.sort()
circuit.sort(key=len)
count = 0
while len(circuit) > 0:
	count += 1
	for command in circuit:
		assigned = command[-2:]
		assigned = assigned.strip()
		temp = command[:-5]
		temp = temp.strip('-')
		command_split = temp.split()

		if len(command_split) == 1:
			var1 = command_split[0]
			if var1 in variables:
				variables[assigned] = variables[var1]
				circuit.remove(command)
			elif var1.isdigit():
				variables[assigned] = var1
				circuit.remove(command)

		if len(command_split) == 2:
			operator, var1 = command_split
			if var1 in variables:
				variables[assigned] = eval(operator + str(variables[var1]))
				circuit.remove(command)


		if len(command_split) == 3:
			var1, operator, var2 = command_split
			if var1 in variables and var2 in variables:
				variables[assigned] = eval(str(variables[var1]) + operator + str(variables[var2]))
				circuit.remove(command)
			elif var1 in variables and var2.isdigit():
				variables[assigned] = eval(str(variables[var1]) + operator + var2)
				circuit.remove(command)
			elif var2 in variables and var1.isdigit():
				variables[assigned] = eval(var1 + operator + str(variables[var2]))
				circuit.remove(command)
			elif var1 in variables:
				if operator.strip() == '<<':
					variables[assigned] = eval(str(variables[var1]) + operator + var2)
					circuit.remove(command)
				elif operator.strip() == '>>':
					variables[assigned] = eval(str(variables[var1]) + operator + var2)
					circuit.remove(command)

print variables['a']