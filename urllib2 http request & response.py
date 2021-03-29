#
# Alien Signal API listening on http://127.0.0.1:8082
# Use HTTP GET with x-api-key header to get signal
# We have narrowed down the key to be in the range of 5500 to 5600
# Note: The script can timeout if this occurs try narrowing
# down your search
#

import urllib2

# Then you need to open the URL:
response = urllib2.urlopen("http://127.0.0.1:8082")
html = response.read()

for i in range(5500, 5601):
	request = urllib2.Request("http://127.0.0.1:8082", headers={"x-api-key" : str(i)})
	print(urllib2.urlopen(request).read())
  

# Now you just need to read the contents of the response:
