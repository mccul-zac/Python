# Authors: Ben G. & Zach M. 
# 4/20/2019


def ip(iocList):
  ph = ' || ip.all = '.join(line.rstrip() for line in iocList)
  print(f'ip.all = {ph}')
  return

def url(iocList):
  ph = ' || domain.dst = \"'.join(line.rstrip()+"\"" for line in iocList)
  print(f'domain.dst = \"{ph}')
  return

def iocHash(iocList):
  ph = ' || checksum = \"'.join(line.rstrip()+"\"" for line in iocList)
  print(f'checksum = \"{ph}')
  return

def fileName(iocList):
  ph = ' || filename = \"'.join(line.rstrip()+"\"" for line in iocList)
  print(f'filename = \"{ph}')
  return

def splunk():

  return

if __name__ == "__main__":
  # instantiate list and prompt user for file name(must be in directory with python file)
  refangList = []
  fileName = input("Enter the name of the IOC file (i.e. ioc_list.txt): ")
  #siemSelect = input("Splunk or RSA?: ")
  print (" 1 = IP\n","2 = URL\n","3 = Hash\n","4 = File Name")

  with open(fileName, 'r') as infile:
    for line in infile:
      refang = line.replace('[.]', '.')
      refangList.append(refang.rstrip('\n'))

  # user input
  iocSelection = int(input("\nSelect a type of IOC in your file(1, 2 ,3, 4): "))

  # menu and calling functions
  if iocSelection == 1:
    ip(refangList)
  elif iocSelection == 2:
    url(refangList)
  elif iocSelection == 3:
    iocHash(refangList)
  elif iocSelection == 4:
    fileName(refangList)
  else:
    print ("Error you make a valid selection...try again")
    
    
    
    
  ###########################
  
  # refang assumes syntax for fang is (badsite[.]com)
# There is a TLD lib but this assumes you are unable to install it

import os,re


fileName = 'ioc.txt'
#fileName = input('File Path: ')


def curlTLD():
  if os.path.isfile('./tld.txt') == False:
    cmd = "curl -o tld.txt http://data.iana.org/TLD/tlds-alpha-by-domain.txt"
    os.system(cmd)
    with open('tld.txt', 'r') as fin:
        data = fin.read().splitlines(True)
    with open('tld.txt', 'w') as fout:
        fout.writelines(data[1:])

curlTLD()

def removeNewline(myList):
  betterList = []
  [betterList.append(i.strip()) for i in myList]
  return betterList


def split_file(filename):
  done = list(filename.split('\n'))
  return done




with open(fileName, 'r') as fanged:
    content = fanged.read()
refanged = re.sub('\[\.\]', r'.', content)
blah = open('live_ioc.txt', 'w')
blah.write(refanged)
blah.close()


refangedFile = open('live_ioc.txt', 'r')
#print(refangedFile.read())
prime = refangedFile.read()




########################################

regexIP = re.compile('(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])(?:$|\n)')
ipList = regexIP.findall(prime)
finalIPList = removeNewline(ipList)


########################################




########################################



filename = open('tld.txt').read()
qqq = split_file(filename)

domainList = []
#def domain_regex():
for var in qqq: ###my TLD list loop
  regexDomain = re.compile(f'(?:.+\.{var}(?:$|\n))', re.IGNORECASE) ###regex for each tld 
  if len(regexDomain.findall(prime)) > 0:
    domainList.extend(regexDomain.findall(prime))





bigDomainList = removeNewline(domainList)


finalEmailList = []
finalDomainList = []

for r in bigDomainList:
  if '@' in r:
    finalEmailList.append(r)
  else:
    finalDomainList.append(r)



########################################

MD5List = []
SHA1List = []
SHA256List = []

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

fullList = []
fullList.extend(hashList)
fullList.extend(domainList)
fullList.extend(ipList)



remainingList = []
newFile = r'live_ioc.txt'

with open(newFile, 'r') as thisguy:
    content2 = thisguy.readlines()
    for line in content2:
      if line not in fullList:
        remainingList.append(line)

finalRemainingList = removeNewline(remainingList)




print(finalIPList)
print('')
print(finalHashList)
print('')
print(finalDomainList)
print('')
print(finalEmailList)
print('')
print(finalRemainingList)









