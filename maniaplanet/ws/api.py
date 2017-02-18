import hashlib
import requests
import json

from . import __version__

API_URL = 'https://ws.maniaplanet.com'


class ManiaplanetWS(object):
	DEFAULT_USER_AGENT = 'maniaplanet-ws-python-sdk/{} requests/{}'.format(__version__, requests.__version__)
	DEFAULT_TIMEOUT = 10
	DEFAULT_RETRIES = 2
	DEFAULT_VERIFY = True

	def __init__(
		self,
		username=None, password=None,
		timeout=None, retries=None,
		user_agent=None,
		verify=None, cert=None,
		session=None,
	):
		self.username = username
		self.password = password

		self.timeout = timeout or self.DEFAULT_TIMEOUT
		self.retries = retries or self.DEFAULT_RETRIES
		self.user_agent = user_agent or self.DEFAULT_USER_AGENT
		self.verify = verify or self.DEFAULT_VERIFY
		self.cert = cert

		# Create or use the provided persistent storage for requests.
		self.session = session if isinstance(session, requests.Session) else requests.Session()

	def populate_session(self):
		"""
		This method will update the session with the class properties.
		"""
		self.session.auth = (self.username, self.password)
		self.session.headers.update({'User-Agent': self.user_agent})
		self.session.verify = self.verify
		self.session.cert = self.cert

	def request(
		self, path, args=None, data=None, method=None, files=None
	):
		"""
		Sending request to the API server with the given path. Will encode args and data (post/put) automatically.

		:param path: Path of the requesting resource. Don't add any get parameters! We will do that for you.
		:param args: Any get parameters.
		:param data: Dictionary or tuple data.
		:param method: Method of call, could be string: 'GET', 'POST', 'PUT', 'DELETE', and any other valid method.
		:param files: Any files to post.
		:type path: str
		:type args: dict, tuple
		:type data: dict, tuple
		:type method: str
		:type files: tuple, dict

		:return: Response object from requests module.
		:rtype: requests.Response

		.. seealso:: http://docs.python-requests.org/en/master/user/advanced/#request-and-response-objects
		"""
		# Updating session storage with new user/pass and other data.
		self.populate_session()

		# Normalize some variables.
		if not path.startswith('/'):
			path = '/' + path

		# Prepare request
		req = requests.Request(
			method=method or 'GET',
			url=API_URL + path,
			params=args,
			data=data,
			files=files,
		).prepare()

		# Execute call
		res = self.session.send(req)

		return res
