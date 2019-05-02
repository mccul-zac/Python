import re, sys

pdfFileObjx = open('pdfStrings.txt', 'rb').read()
pdfFileObj = pdfFileObjx.decode('ASCII')

newList = []
finalDstIPList = []
ipList = []

ipList = re.findall('ip.dst=(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])', pdfFileObj)

for i in ipList:
    if i not in newList:
        newList.append(i)

for item in newList:
    q = item.strip('ip.dst=')
    finalDstIPList.append(q)

for item in finalDstIPList:
    print(item)

print('\n\nTotal External IP Addresses:', len(ipList), '\n\nTotal unique IP Addresses:', len(finalDstIPList))
