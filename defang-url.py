import os, sys, re, fileinput
s = input('Defang the following: \n')
replaced = re.sub(r'\.', '[.]', s)
print ('\n\n')
print ('Defanged Version:')
print (replaced)
print ('\n')


input()     #Left this here to make the file 'Clickable'


#for line in fileinput.input(sys.argv[1:]):
#   x = re.sub(r'\.', '[.]', line)
#  print (x)

