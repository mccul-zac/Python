Purpose:
 - Turn file containing mixed IOCs into Netwitness/Splunk queries  
 
Requirements:
 - Python 3
 - ioc.txt must contain only one IOC per line

FYI:
 - Refang assumes syntax for defang is similair to: badsite[.]com
 - Uncomment/Comment curlTLD() environment as appropriate (default is windows/powershell)
 - There is a TLD lib but this assumes you are unable to install it
 - RSA metakeys may vary based on env
 - Expect script to output 4 files (live_ioc.txt, tld.txt, IOCsearchSyntax.txt, IOCsearchSyntax.zip)
 - Option to zip the IOCsearchSyntax.txt added
 - Separate Hash lists are available for MD5, SHA1, and SHA256 (current output does not separate them) 
 - "file" output is actually the remaining IOCs that are not IP, Hash, Domain, or Email  

To Do:
 - [x] Add Splunk usage
 - [X] New list for each IOC type
 - [X] Add check to determine IOC (regex?)
 - [ ] ~~List[0]+ (through each list item check what type of IOC)~~
 - [x] Curl TLD list (http://data.iana.org/TLD/tlds-alpha-by-domain.txt) and save file (rather than local)
 - [ ] Explicitly differentiate files from other IOCs 
 - [ ] Turn lists to sets (to avoid dupes)
 - [ ] Replace append to IOCsearchSyntax.txt (continues to append if running script consecutively)
 - [x] Remove null IOCs from output
 - [ ] ~~Breakdown Splunk search~~
 - [ ] PEP-8 format
