import unittest

from .. import ManiaplanetWS


class ClientRequestTest(unittest.TestCase):

	def setUp(self):
		self.client = ManiaplanetWS(username='wrong', password='wrong', raw_responses=True, use_exceptions=False)

	def test_notfound_request(self):
		response = self.client.request('test')
		self.assertEqual(response.status_code, 404)

		response = self.client.request('adisufashiuashiu', args=dict(any=True))
		self.assertEqual(response.status_code, 404)

	def test_unauthorized_request(self):
		response = self.client.request('players/tomvalk/')
		self.assertEqual(response.status_code, 401)
