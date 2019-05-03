def curlTLD():
    if os.path.isfile('./tld.txt') == False:
        pro = subprocess.Popen(['powershell', '$tld = curl http://data.iana.org/TLD/tlds-alpha-by-domain.txt | Select-Object -Expand Content;$tld.split() | Out-File -Encoding ASCII tld.txt'])
        time.sleep(2.0)
        pro.kill()
        with open('tld.txt', 'r') as fin:
            data = fin.read().splitlines(True)
            with open('tld.txt', 'w') as fout:
                fout.writelines(data[12:])
