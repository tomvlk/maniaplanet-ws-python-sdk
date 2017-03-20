import unittest

from maniaplanet_ws import ManiaplanetWS


class ClientBasicTest(unittest.TestCase):
	def test_initialize(self):
		api = ManiaplanetWS()
		self.assertIsInstance(api, ManiaplanetWS)

		api = ManiaplanetWS(user_agent='test/1.0', username='', password='')
		self.assertIsInstance(api, ManiaplanetWS)
