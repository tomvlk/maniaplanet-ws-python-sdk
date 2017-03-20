import unittest

from maniaplanet_ws import ManiaplanetWS


class ClientTestCase (unittest.TestCase):

	def __init__(self, *args, **kwargs):
		self.__client = None
		super(ClientTestCase, self).__init__(*args, **kwargs)

	@property
	def client(self, **kwargs):
		kwargs.setdefault('raw_responses', True)
		kwargs.setdefault('use_exceptions', False)

		if not self.__client:
			self.__client = ManiaplanetWS(**kwargs)
		return self.__client
