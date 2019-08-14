'''
Purpose:
Removes lines containing specified 'tag' and stores the IP associated with said tag. Then removes all other lines containing the same IP and outputs a csv with the leftovers.

Usage syntax:
python tag_filter.py filename

Side Note:
*The script is currently configured to be run in the same directory as the input and output file.  
**In this example 'scan_ip' is the desired tag to be removed
'''


import os
import sys

scan_ip_list = set()
cwd = os.getcwd() + '/'


def sort_ip(filename):
	try:
	    with open(cwd + filename, 'r+') as fin:
		for line in fin:
		    split_line = line.split(',')
		    ip_from_line = split_line[0]
		    if 'scan_ip' in line:
			scan_ip_list.add(ip_from_line)
	except IOError:
	     print "failed at 1"

	try:
	    with open(cwd + filename, 'r+') as fin2:
	        with open(cwd + 'filtered_result.csv', 'w+') as fileout:
		    for line in fin2:
		        split_line = line.split(',')
			ip_from_line = split_line[0]
			if ip_from_line not in scan_ip_list:
			    fileout.write(line)
	except IOError:
		print "failed at 2"

if __name__ == "__main__":
    sort_ip(sys.argv[1])




