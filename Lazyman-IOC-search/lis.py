# Authors: Ben G. & Zach M.
# 4/20/2019
# refang assumes syntax for fang is (badsite[.]com)
# There is a TLD lib but this assumes you are unable to install it
# Some issues currently present with curled TLD list, recommend saving file locally and remove title line


import os,re

fileName = 'ioc.txt'
#fileName = input('File Path: ')

domainList = []
finalEmailList = []
finalDomainList = []
MD5List = []
SHA1List = []
SHA256List = []
fullList = []
remainingList = []

'''
def curlTLD():
  if os.path.isfile('./tld.txt') == False:
    cmd = "curl -o tld.txt http://data.iana.org/TLD/tlds-alpha-by-domain.txt"
    os.system(cmd)
    with open('tld.txt', 'r') as fin:
        data = fin.read().splitlines(True)
    with open('tld.txt', 'w') as fout:
        fout.writelines(data[1:])
curlTLD()
'''

def removeNewline(myList):
  betterList = []
  [betterList.append(i.strip()) for i in myList]
  return betterList

def split_file(filename):
  done = list(filename.split('\n'))
  return done

def ip_format_search(iocList):
  ph = ' || ip.all = '.join(line.rstrip() for line in iocList)
  print(f'ip.all = {ph}')

def url_format_search(iocList):
  ph = ' || domain.dst = \"'.join(line.rstrip()+"\"" for line in iocList)
  print(f'domain.dst = \"{ph}')

def hash_format_search(iocList):
  ph = ' || checksum = \"'.join(line.rstrip()+"\"" for line in iocList)
  print(f'checksum = \"{ph}')

'''
def email_format_search(iocList):
  ph = ' || filename = \"'.join(line.rstrip()+"\"" for line in iocList)
  print(f'filename = \"{ph}')
'''

def file_format_search(iocList):
  ph = ' || filename = \"'.join(line.rstrip()+"\"" for line in iocList)
  print(f'filename = \"{ph}')

with open(fileName, 'r') as fanged:
    content = fanged.read()
refanged = re.sub('\[\.\]', r'.', content)
blah = open('live_ioc.txt', 'w')
blah.write(refanged)
blah.close()

refangedFile = open('live_ioc.txt', 'r')
prime = refangedFile.read()

regexIP = re.compile('(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])(?:$|\n)')
ipList = regexIP.findall(prime)
finalIPList = removeNewline(ipList)

filename = open('tld.txt').read()
qqq = split_file(filename)
for var in qqq: ###my TLD list loop
  regexDomain = re.compile(f'(?:.+\.{var}(?:$|\n))', re.IGNORECASE) ###regex for each tld 
  if len(regexDomain.findall(prime)) > 0:
    domainList.extend(regexDomain.findall(prime))
bigDomainList = removeNewline(domainList)
for r in bigDomainList:
  if '@' in r:
    finalEmailList.append(r)
  else:
    finalDomainList.append(r)

regexHash = re.compile('[a-f0-9]{32,64}(?:$|\n)', re.IGNORECASE)
hashList = regexHash.findall(prime)
finalHashList = removeNewline(hashList)
for hashVal in finalHashList:
  if len(hashVal) == 32:
    MD5List.append(hashVal) 
  elif len(hashVal) == 40:
    SHA1List.append(hashVal)
  elif len(hashVal) == 64:
    SHA256List.append(hashVal)
  else:
    pass

fullList.extend(hashList)
fullList.extend(domainList)
fullList.extend(ipList)

newFile = r'live_ioc.txt'
with open(newFile, 'r') as thisguy:
    content2 = thisguy.readlines()
    for line in content2:
      if line not in fullList:
        remainingList.append(line)
finalRemainingList = removeNewline(remainingList)

ip_format_search(finalIPList)
print('')
url_format_search(finalDomainList)
print('')
hash_format_search(finalHashList)
print('')
#email_format_search(finalEmailList)
#print('')
file_format_search(finalRemainingList)
