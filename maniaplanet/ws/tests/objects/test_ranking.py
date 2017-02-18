from ..base import ClientTestCase


class RankingTest(ClientTestCase):
	def test_retrieval(self):
		res = self.client.request('canyon/rankings/multiplayer/zone/', args=dict(
			offset=0,
			length=100,
			title='TMCanyon'
		))

		self.assertEqual(res.status_code, 200)
