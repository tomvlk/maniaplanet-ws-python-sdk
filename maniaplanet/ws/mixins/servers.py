from . import WebserviceSubject, WebserviceMixin, WebserviceMethods


class Methods(WebserviceMethods):
	def get(self, login):
		"""
		Get single server details by login of server.

		:param login: Login of the server.
		:type login: str
		:return: server response
		:rtype: requests.Response, dict
		"""
		return self._client.request('/servers/{:s}/'.format(login))


#
#####
#

class ServersMixin(WebserviceMixin):
	def __init__(self):
		self.servers = Methods(self)

		super().__init__()
