dict = {}

logs = r'logs.txt'
iocs = r'iocs.txt'
logs = open(logs).readlines()
iocs = open(iocs).readlines()

for ioc in iocs:
    dict[ioc] = []

for ioc in dict.keys():
    for line in logs:
        if ioc in line:
            dict[ioc].append(line)

print(dict)
