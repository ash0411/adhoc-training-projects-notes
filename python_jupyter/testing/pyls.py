 #!/usr/bin/python3
# this is a prototype not to be used
import sys,os,re
command = sys.argv[1:]
#print(type(command))
if command[-1] == [] or re.match(-.+,command[-1]):
	path = os.getcwd()
else:
	path = command[-1]
arguments = []
for i in command:
	if re.match(-.+):
		arguments.append(i[1:])
if 'a' in arguments:
	os.listdir(str(path))
if arguments == []:
		for i in os.listdir(str(path)):
			if i.startswith != '.':
				print(i)

