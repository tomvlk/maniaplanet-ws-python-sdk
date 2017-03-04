from ..base import ClientTestCase


class ManiaflashTest(ClientTestCase):
	def test_channel(self):
		res = self.client.maniaflash.channel(id='maniaplanet-news')
		self.assertEqual(res.status_code, 200)
		data = res.json()

		self.assertEqual(data['id'], 'maniaplanet-news')

	def test_messages(self):
		res = self.client.maniaflash.messages(id='maniaplanet-news', length=10)
		self.assertEqual(res.status_code, 200)
		data = res.json()
		self.assertEqual(len(data), 10)

		res = self.client.maniaflash.messages(hashtag='event', length=10)
		self.assertEqual(res.status_code, 200)
		data = res.json()
		self.assertIsInstance(data, list)
