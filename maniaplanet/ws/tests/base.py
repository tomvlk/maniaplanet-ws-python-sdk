import unittest

from .. import ManiaplanetWS


class ClientTestCase (unittest.TestCase):

	def __init__(self, *args, **kwargs):
		self.__client = None
		super(ClientTestCase, self).__init__(*args, **kwargs)

	@property
	def client(self):
		if not self.__client:
			self.__client = ManiaplanetWS()
		return self.__client
