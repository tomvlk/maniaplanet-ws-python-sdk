from ..base import ClientTestCase


class PlayerTest(ClientTestCase):
	def test_retrieval(self):
		res = self.client.request('players/tomvalk/')
		self.assertEqual(res.status_code, 200)
