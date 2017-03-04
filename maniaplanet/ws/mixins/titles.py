from . import WebserviceMixin, WebserviceMethods


class Methods(WebserviceMethods):
	"""
	Titles Methods.
	"""
	def detail(self, id):
		"""
		Get single server details by login of server.

		:param id: ID of the title (in string format, like TMCanyon).
		:type id: str
		:return: server response
		:rtype: requests.Response, dict
		"""
		return self._client.request('/titles/{:s}/'.format(id))


#
#####
#

class TitlesMixin(WebserviceMixin):
	"""
	Titles mixin
	"""
	def __init__(self):
		self.titles = Methods(self)

		super().__init__()
