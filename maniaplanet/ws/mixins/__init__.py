
class WebserviceMixin(object):
	pass


class WebserviceSubject(object):
	def __init__(self, client):
		"""
		Initiate the subject class.
		:param client:
		:type client: maniaplanet.ws.ManiaplanetWS
		"""
		self._client = client


class WebserviceMethods(WebserviceSubject):
	pass


from .rankings import RankingsMixin
from .servers import ServersMixin
from .titles import TitlesMixin
from .zones import ZonesMixin
