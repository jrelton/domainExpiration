from .runQuery import findExpiration


def findTLD(d):

	dSplit = d.split('.')

	# Modify top level domain for certain cases
	if d.endswith('.co.jp'):
		tld = 'co_jp'
	elif d.endswith('.is'):
		tld = 'is_is'
	elif d.endswith('.xn--p1ai'):
		tld = 'ru_rf'
	elif d.endswith('.ac.uk') and len(d) > 2:
		tld = 'ac_uk'
	elif d.endswith('.name'):
		dSplit[0] = 'domain=' + dSplit[0]
		tld = dSplit[-1]
	elif d.endswith('.in'):
		tld = 'in_'
	elif d.endswith('.com.au'):
		tld = 'com_au'
	else:
		tld = dSplit[-1]

	result = findExpiration(dSplit, tld)
	return result
		
	