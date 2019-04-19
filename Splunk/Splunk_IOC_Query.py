# Take IOC list (input OR file) and spit out a Splunk query
# Should include option to apply additional fields

blah = []

for ioc in list:
  blah.append(f"{ioc} OR ") 

here = "".join(blah)

print(f"index=* AND ({here})")




