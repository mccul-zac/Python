'''
# Authors: Ben G.& Zach M.
# 5/3/2019
'''

import os,re,subprocess,time,zipfile

# The below functions are for printing formatted searches for RSA Netwitness and Splunk

def removeNewline(myList):
  betterList = []
  [betterList.append(i.strip()) for i in myList]
  return betterList

def split_file(filename):
  done = list(filename.split('\n'))
  return done

def ip_format_search(iocList, searchSyntax):
  # outputs Netwitness syntax for IP addresses and appends to syntax file
    ph = ' || ip.all = '.join(line.rstrip() for line in iocList)
    if ph != '':
        print(f'ip.all = {ph}')
        searchSyntax.write("\n\n"f'ip.all = {ph} || ')
    else:
        return

def url_format_search(iocList, searchSyntax):
  # outputs Netwitness syntax for domain and appends to syntax file
    ph = ' || domain.dst = \"'.join(line.rstrip()+"\"" for line in iocList)
    if ph != '':
        print(f'domain.dst = \"{ph}')
        searchSyntax.write(f'domain.dst = \"{ph} || ')
    else:
        return

def hash_format_search(iocList, searchSyntax):
  # outputs Netwitness syntax for hashes and appends to syntax file
    ph = ' || checksum = \"'.join(line.rstrip()+"\"" for line in iocList)
    if ph != '':
        print(f'checksum = \"{ph}')
        searchSyntax.write(f'checksum = \"{ph} || ')
    else:
        return

def email_format_search(iocList, searchSyntax):
  # outputs Netwitness syntax for email addresses and appends to syntax file
    ph = ' || email.all = \"'.join(line.rstrip()+"\"" for line in iocList)
    if ph != '':
        print(f'email.all = \"{ph}')
        searchSyntax.write(f'email.all = \"{ph} || ')
    else:
        return

def file_format_search(iocList, searchSyntax):
  # outputs Netwitness syntax for files/extra "stuff" and appends to syntax file
    ph = ' || filename = \"'.join(line.rstrip()+"\"" for line in iocList)
    if ph != '':
        print(f'filename = \"{ph}')
        searchSyntax.write(f'filename = \"{ph}')
    else:
        return

def SplunkSearch(searchSyntax):
  # outputs Splunk syntax for all IOCs and appends to syntax file
    newFile = r'live_ioc.txt'
    with open(newFile, 'r') as liveIoc:
        ph = ' OR \"'.join(line.rstrip()+"\"" for line in liveIoc)
        print(f'index = * {ph}')
        searchSyntax.write("\n\n"f'index=* ("{ph}) earliest=-90d')

def curlTLD():
  '''
  checks if tld.txt exists in the current directory, if so, use that file.
  If not, pull the TLDs from IANA and store it in tld.txt
  '''
  if os.path.isfile('./tld.txt') == False:
        pro = subprocess.Popen(['powershell', '$tld = curl http://data.iana.org/TLD/tlds-alpha-by-domain.txt | Select-Object -Expand Content;$tld.split() | Out-File -Encoding ASCII tld.txt'])
        time.sleep(4.0)
        pro.kill()
        if os.path.isfile('./tld.txt') == True:
            with open('tld.txt', 'r') as fin:
                data = fin.read().splitlines(True)
                with open('tld.txt', 'w') as fout:
                    fout.writelines(data[12:])


if __name__ == '__main__':
    '''
    Input: ioc.txt
    Processing:
      Opens the IOC file, reads through each line and re-fangs the IOCs if they have been de-fanged
      Uses regex to look for IP addresses and add them to finalIPList
      Call CurlTLD function to look for the TLD file or create a new one, then look for domains with those TLDs
      Use regex to look for hash values of types MD5, SHA1, or SHA256 and add matches to respective lists
      Add previous findings to fullList
      Create file IOCsearchSyntax.txt
    Output:
      Send output of previously created lists to respective print functions and print RSA Netwitness formatted searches
      and Splunk searches, in addition to appending searches to IOCsearchSyntax.txt
      Finally, zip IOCsearchSyntax.txt
    '''
    fileName = 'ioc.txt'
    domainList = []
    finalEmailList = set()
    finalDomainList = []
    MD5List = []
    SHA1List = []
    SHA256List = []
    fullList = []
    remainingList = []

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
    refangedFile.close()

    curlTLD()
    filename = open('tld.txt').read()
    qqq = split_file(filename)
    for var in qqq: ###my TLD list loop
      regexDomain = re.compile(f'(?:.+\.{var}(?:$|\n))', re.IGNORECASE) ###regex for each tld
      if len(regexDomain.findall(prime)) > 0:
        domainList.extend(regexDomain.findall(prime))
    bigDomainList = removeNewline(domainList)
    for r in bigDomainList:
      if '@' in r:
        finalEmailList.add(r)
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
    iocOut = open(newFile, 'r')
    content2 = iocOut.readlines()
    for line in content2:
        if line not in fullList:
            remainingList.append(line)
    iocOut.close()
    finalRemainingList = removeNewline(remainingList)

    searchSyntax = 'IOCsearchSyntax.txt'
    with open(searchSyntax, 'a') as SiemSearch:
      SiemSearch.write("*"*10 + "   RSA Netwitness Searches   " + "*"*10+ "\n")
      print("*** RSA Netwitness Searches ***")
      ip_format_search(finalIPList, SiemSearch)
      print('')
      url_format_search(finalDomainList, SiemSearch)
      print('')
      hash_format_search(finalHashList, SiemSearch)
      print('')
      email_format_search(finalEmailList, SiemSearch)
      print('')
      file_format_search(finalRemainingList, SiemSearch)
      print('')
      print('*** Splunk Search ***\n')
      SiemSearch.write("\n\n" + "*"*10 + "   Splunk Search   " + "*"*10+ "\n")
      SplunkSearch(SiemSearch)
    # Zip the file for email purpose
    zipfile.ZipFile('IOCsearchSyntax.zip', mode='w').write(searchSyntax)

    # Delete the files created earlier except for the search syntax files
    if os.path.exists("live_ioc.txt"):
        os.remove("live_ioc.txt")
    else:
        print("The file does not exist")

    if os.path.exists("tld.txt"):
        os.remove("tld.txt")
    else:
        print("The file does not exist")
