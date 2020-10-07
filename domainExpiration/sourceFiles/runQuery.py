import subprocess
import re

def findExpiration(d, tld):
	domain = '.'.join(d)

	# Create a new subprocess and pipe the output of the whois command into this script
	p = subprocess.Popen(['whois', domain], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

	# Retrieve results and decode the unicode result
	r = p.communicate()[0]
	r = r.decode()
	
	# Condense the output string
	whois_str = r.split("source:       IANA")

	if len(whois_str) == 2:
		whois_str = whois_str[1]

	# Further parsing for some common domains
	if tld.lower() == "com":
		whois_str = whois_str[whois_str.find('Registry Expiry Date:'):whois_str.find('Registrar:')]
	if tld.lower() == "org":
		whois_str = whois_str[whois_str.find('Registrar Registration Expiration Date: '):whois_str.find('Registrar: MarkMonitor, Inc')]
	if tld.lower() == "net":
		whois_str = whois_str[whois_str.find('Registry Expiry Date:'):whois_str.find('Registrar:')]




	return whois_str
