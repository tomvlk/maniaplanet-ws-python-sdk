import requests
import netrc

from . import (
	__version__,
	API_URL,
	API_HOST,
	mixins
)


class ManiaplanetWS(
	mixins.RankingsMixin,
	mixins.ServersMixin,
	mixins.TitlesMixin,
	mixins.ZonesMixin,
	object
):
	__DEFAULT_USER_AGENT = 'maniaplanet-ws-python-sdk/{} requests/{}'.format(__version__, requests.__version__)
	__DEFAULT_TIMEOUT = 10
	__DEFAULT_VERIFY = True

	def __init__(
		self,
		username=None, password=None,
		timeout=None,
		user_agent=None,
		verify=None, cert=None,
		session=None,
		raw_responses=False,
		use_exceptions=True,
	):
		"""
		Initiate the Maniaplanet Webservice SDK.

		:param username: username of the webservice account.
		:param password: password of the webservice account.
		:param timeout: maximum timeout in seconds (optional).
		:param user_agent: customize the user-agent used to communicate with the webservice.
		:param verify: override default enabled SSL/TLS verify process.
		:param cert: override default certificate checking against (SSL/TLS).
		:param session: give a custom requests.Session instance to use.
		:param raw_responses: override and set to True to get back requests.Response instead of parsed dictionaries.
		:param use_exceptions: 	override and set to False to disable exception throws on response errors.
								Not raising on 404 errors!

		:type username: str
		:type password: str
		:type timeout: int
		:type user_agent: str
		:type verify: bool
		:type cert: str
		:type session: requests.Session
		:type raw_responses: bool
		:type use_exceptions: bool
		"""

		self.__username = username
		self.__password = password

		self.__timeout = timeout or self.__DEFAULT_TIMEOUT
		self.__user_agent = user_agent or self.__DEFAULT_USER_AGENT
		self.__verify = verify or self.__DEFAULT_VERIFY
		self.__cert = cert

		# Public behaviour variables that could be changed later on.
		self.raw_responses = bool(raw_responses)
		self.use_exceptions = bool(use_exceptions)

		# Create or use the provided persistent storage for requests.
		self.session = session if isinstance(session, requests.Session) else requests.Session()

		# Initiate super classes.
		super(ManiaplanetWS, self).__init__()

	def __populate_session(self):
		"""
		This method will update the session with the class properties.
		"""
		if self.__username and self.__password:
			self.session.auth = (self.__username, self.__password)
		else:
			# Try to get credentials from .netrc file.. This should do requests automatically, but didn't work so far.
			auth = netrc.netrc().authenticators(API_HOST)
			if auth and len(auth) == 3 and auth[0] and auth[2]:
				self.session.auth = (auth[0], auth[2])
			else:
				self.session.auth = None

		self.session.headers.update({'User-Agent': self.__user_agent})

		self.session.verify = self.__verify
		self.session.cert = self.__cert

	def request(
		self, path, args=None, data=None, method=None, files=None,
		**kwargs
	):
		"""
		Sending request to the API server with the given path. Will encode args and data (post/put) automatically.

		:param path: Path of the requesting resource. Don't add any get parameters! We will do that for you.
		:param args: Any get parameters.
		:param data: Dictionary or tuple data.
		:param method: Method of call, could be string: 'GET', 'POST', 'PUT', 'DELETE', and any other valid method.
		:param files: Any files to post.

		:type path: str
		:type args: dict
		:type data: dict, tuple
		:type method: str
		:type files: tuple, dict

		:return: Response object from requests module.
		:rtype: requests.Response, dict

		.. seealso:: http://docs.python-requests.org/en/master/user/advanced/#request-and-response-objects
		"""
		# Updating session storage with new user/pass and other data.
		self.__populate_session()

		# Pop some abstract parameters
		if not args or not type(args) is dict:
			args = dict()

		if not 'offset' in args or type(args['offset']) is not int:
			args['offset'] = kwargs.pop('offset', 0)
		if not 'length' in args or type(args['length']) is not int:
			args['length'] = kwargs.pop('length', 100)

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
			auth=self.session.auth,
		).prepare()

		# Execute call
		res = self.session.send(
			req,
			timeout=self.__timeout,
		)

		if self.raw_responses:
			return res

		# TODO: Implement some kind of parsing. But don't parse away the response status_code.
		# TODO: Find some nice error/exception flow based on the response status_code.
		return res
