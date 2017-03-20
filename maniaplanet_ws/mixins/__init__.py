"""
Maniaplanet Webservice SDK for Python.
"""


class WebserviceMixin(object):
	"""
	Mixin base class.
	"""
	pass


class WebserviceSubject(object):
	"""
	Subject base class.
	"""
	def __init__(self, client):
		"""
		Initiate the subject class.
		:param client:
		:type client: maniaplanet.ws.ManiaplanetWS
		"""
		self._client = client


class WebserviceMethods(WebserviceSubject):
	"""
	Methods base class.
	"""
	pass


from .rankings import RankingsMixin
from .servers import ServersMixin
from .titles import TitlesMixin
from .zones import ZonesMixin
from .maniaflash import ManiaflashMixin
