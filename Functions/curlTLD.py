def curlTLD():
  if os.path.isfile('./tld.txt') == False:
    cmd = "curl -o tld.txt http://data.iana.org/TLD/tlds-alpha-by-domain.txt"
    os.system(cmd)
    with open('tld.txt', 'r') as fin:
        data = fin.read().splitlines(True)
    with open('tld.txt', 'w') as fout:
        fout.writelines(data[1:])
