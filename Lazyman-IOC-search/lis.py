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
