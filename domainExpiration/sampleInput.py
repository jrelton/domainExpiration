import sourceFiles

# Create a list of sample domains that we can test
domainList = ["google.co.uk", "google.com", "yahoo.com", "www.facebook.com", "ddarko.pl", "incorrect.test", "facebook.ca"]

# Retrieve expiration date for each domain
for d in domainList:
	print('*' * 100) # Print division for formatting purposes

	# Remove www prefix
	if (d[0:3] == "www"):
		d = d[4:]

	result = sourceFiles.findTLD(d)
	print(result)
