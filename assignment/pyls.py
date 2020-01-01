#!usr/bin/python3
# this is made to accept all the arguments but can only work with 1 argument at a time
import os,sys,re
x = sys.argv[1:]
#print(type(x))
r = re.compile("-+.")
#if r.match(str(x[-1])):
#	print("it is not working")# debugging
if x == [] or r.match(str(x[-1])):
	x.append(os.getcwd()) # to get the correct path
arguments = list(filter(r.match, x)) # to get all the arguments
#print(x[-1])
arg =[]
for i in arguments: # to seperate the arguments
	for j in i:
		if j !='-':
			arg.append(j)
if arg == []:  # when there is no arguments 
	for f in os.listdir(str(x[-1])):
		if not f.startswith('.'):
			print(f)
for i in arg:
	if i == 'a':	# if we want hidden arguments
		print(os.listdir(str(x[-1])))		
