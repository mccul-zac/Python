# Dom E. & Zach M.
# 4/26/2019
# run strings on PDF file and search txt for the following:


import re

#fileName = input('File Path: ')
# OR
fileName = 'pdfStrings.txt'


newList = []
finalDstIPList = []

regexIP = re.compile('ip.dst=(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])')
ipList = regexIP.findall(open(fileName, 'r').read())

for i in ipList:
  if i not in newList:
    newList.append(i)

for item in newList:
  q = item.strip('ip.dst=')
  finalDstIPList.append(q)


print('Total External IP Addresses:', len(ipList), '\n\nTotal unique IP Addresses:', len(finalDstIPList), '\n')

print('IPs to search:')
for item in finalDstIPList:
    print(item)

print('')
