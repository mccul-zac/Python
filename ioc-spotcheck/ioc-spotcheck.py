path = r'test-logs.txt'
iocPath = r'test-iocs.txt'
iocPathLine = open(iocPath).readlines()
x = 0
y = 0
spot = iocPathLine[y]

while x < 5:
    for line in open(path):
        if spot in line:
            print (line)
            x += 1
            y += 1
            print (x)
            print (y)
