Purpose:
 - Turn file containing mixed IOCs into Netwitness/Splunk queries  

FYI:
 - Refang assumes syntax for defang is (badsite[.]com)
 - There is a TLD lib but this assumes you are unable to install it

To Do:
 - [ ] Add Splunk usage
 - [X] New list for each IOC type
 - [X] Add check to determine IOC (regex?)
 - [ ] ~~List[0]+ (through each list item check what type of IOC)~~
 - [x] Curl TLD list (http://data.iana.org/TLD/tlds-alpha-by-domain.txt) and save file (rather than local)
