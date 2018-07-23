import os, sys, re, fileinput
s = input('Defang the following: \n')
replaced = re.sub(r'\.', '[.]', s)
print ('\n\n')
print ('Defanged Version:')
print (replaced)
print ('\n')


input()     #Left this here to make the file 'Clickable'
