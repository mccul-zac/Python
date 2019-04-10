logs = r'logs.txt'                          #full path to logs
iocs = r'iocs.txt'                          #full path to iocs
logs = open(logs).readlines()
iocs = open(iocs).readlines()

for ioc in iocs:
    for line in logs:
        if ioc in line:
            print (f'______________________\nIOC:\n{ioc}\nLogs:\n{line}')

