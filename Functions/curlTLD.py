# Not really curl (Invoke-WebRequest)
# Need to remove title line (currently title line is separated into 11 lines...)
# With open...phase does not work (maybe subprocess is still open?)

import subprocess, os

def curlTLD():
    if os.path.isfile('./tld.txt') == False:
        subprocess.Popen(['powershell', '$tld = curl http://data.iana.org/TLD/tlds-alpha-by-domain.txt | Select-Object -Expand Content;$tld.split() | Out-File -Encoding ASCII tld.txt'])
        with open('tld.txt', 'r') as fin:
            data = fin.read().splitlines(True)
            with open('tld.txt', 'w') as fout:
                fout.writelines(data[12:])


