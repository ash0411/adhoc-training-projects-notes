#!usr/bin/python3
import os,sys,re
x = sys.argv[1:]
#print(type(x))
r = re.compile("-+.")
#if r.match(str(x[-1])):
#	print("it is not working")# debugging
if x == [] or r.match(str(x[-1])):
	x.append(os.getcwd())
arguments = list(filter(r.match, x))
#print(x[-1])
arg =[]
for i in arguments:
	for j in i:
		if j !='-':
			arg.append(j)
if arg == []:
	for f in os.listdir(str(x[-1])):
		if not f.startswith('.'):
			print(f)
for i in arg:
	if i == 'a':
		print(os.listdir(str(x[-1])))		
