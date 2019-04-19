# Take IOC list (input OR file) and spit out a Splunk query
# Should include option to apply additional fields
# Edit print as necessary (include/exclude splunk fields)

with open(r"ioc.txt") as file:                        # requires full path to file
    ph = ' OR '.join(line.rstrip() for line in file)
    refang = ph.replace('[.]', '.')
    print(f'index=* AND ({refang})')

