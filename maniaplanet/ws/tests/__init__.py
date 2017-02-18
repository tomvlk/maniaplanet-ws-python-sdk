try:
	import http.client as http_client
except ImportError:
	# Python 2
	import httplib as http_client
http_client.HTTPConnection.debuglevel = 1
