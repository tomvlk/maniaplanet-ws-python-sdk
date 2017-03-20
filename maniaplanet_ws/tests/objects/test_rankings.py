from ..base import ClientTestCase


class RankingsTest(ClientTestCase):
	def test_retrieval(self):
		request_res = self.client.request('canyon/rankings/multiplayer/zone/', args=dict(
			offset=0,
			length=100,
			title='TMCanyon'
		))
		self.assertEqual(request_res.status_code, 200)

		# Retrieve with the subject classes.
		subject_res = self.client.rankings.solo.player(title='TMCanyon', login='tomvalk')
		self.assertEqual(subject_res.status_code, 200)

		# Compare the native and the subject responses.
		self.assertEqual(request_res.headers.get('Content-Size'), subject_res.headers.get('Content-Size'))

	def test_solo_player(self):
		res = self.client.rankings.solo.player(title='TMCanyon', login='tomvalk')
		self.assertEqual(res.status_code, 200)

		# Should give 404 as we don't provide the login.
		res = self.client.rankings.solo.player(title='TMCanyon')
		self.assertEqual(res.status_code, 404)

		# TODO: Check contents

	def test_solo_world(self):
		res = self.client.rankings.solo.world(title='TMCanyon')
		self.assertEqual(res.status_code, 200)

		# TODO: Check contents

	def test_solo_zone(self):
		res = self.client.rankings.solo.zone(title='TMCanyon', path='World|Europe|Netherlands')
		self.assertEqual(res.status_code, 200)

		# TODO: Check contents

	def test_solo_challenge_player(self):
		res = self.client.rankings.solo.challenge.player(title='TMCanyon', challenge='doesn\'t exists', login='tomvalk')
		self.assertEqual(res.status_code, 404)


	def test_multiplayer_player(self):
		res = self.client.rankings.multiplayer.player(title='TMCanyon', login='tomvalk')
		self.assertEqual(res.status_code, 200)

		# TODO: Check contents

	def test_multiplayer_zone(self):
		res = self.client.rankings.multiplayer.zone(title='TMCanyon', path='World|Europe|Netherlands')
		self.assertEqual(res.status_code, 200)

		# TODO: Check contents

	def test_multiplayer_world(self):
		res = self.client.rankings.multiplayer.world(title='TMCanyon')
		self.assertEqual(res.status_code, 200)

		# TODO: Check contents
