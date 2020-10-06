import subprocess
import re

def findExpiration(d, tld):
	domain = '.'.join(d)

	# Create a new subprocess and pipe the output of the whois command into this script
	p = subprocess.Popen(['whois', domain], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

	# Retrieve results and decode the unicode result
	r = p.communicate()
	r = r[0].decode()
	

	# Condense the output string
	whois_str = r.split("source:       IANA")
	if len(whois_str) == 2:
		whois_str = whois_str[1]
	else:
		return None

	whois_str = r[r.find('Domain Name:'):]
	return whois_str
