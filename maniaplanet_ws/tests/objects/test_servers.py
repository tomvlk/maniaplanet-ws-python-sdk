from ..base import ClientTestCase


class ServersTest(ClientTestCase):
	def test_retrieval(self):
		request_res = self.client.request('/servers/droppie666/')
		self.assertEqual(request_res.status_code, 200)

		# Retrieve with the subject classes.
		subject_res = self.client.servers.detail(login='droppie666')
		self.assertEqual(subject_res.status_code, 200)

		# Compare the native and the subject responses.
		self.assertEqual(request_res.headers.get('Content-Size'), subject_res.headers.get('Content-Size'))

	def test_single_server(self):
		# Should give 404 as we don't provide the login.
		res = self.client.servers.detail(login='thisserverdoesntexists')
		self.assertEqual(res.status_code, 404)

		res = self.client.servers.detail(login='droppie666')
		self.assertEqual(res.status_code, 200)

	# TODO: Check contents

	def test_online_players(self):
		res = self.client.servers.online_players('droppie666')
		self.assertEqual(res.status_code, 200)
		self.assertIsInstance(res.json(), list, 'Returned json should be a list.')

	def test_favorited_count(self):
		res = self.client.servers.favorite_count('droppie666')
		self.assertEqual(res.status_code, 200)
		res_count = int(res.json())
		self.assertIsInstance(res_count, int, 'Returned data should be an integer')

	def test_report_abuses(self):
		res = self.client.servers.reported_abuses('droppie666')
		self.assertEqual(res.status_code, 400, 'Request is not done with authentication.')

	def test_server_list(self):
		res = self.client.servers.list()
		self.assertEqual(res.status_code, 200)
		self.assertIsInstance(res.json(), list)

		# Test length filtering.
		res = self.client.servers.list(length=10)
		self.assertEqual(res.status_code, 200)
		json = res.json()
		self.assertIsInstance(json, list)
		self.assertEqual(len(json), 10)

		# Test filtering on title
		res = self.client.servers.list(title='TMCanyon', length=10)
		self.assertEqual(res.status_code, 200)
		json = res.json()
		self.assertIsInstance(json, list)
		for entry in json:
			self.assertEqual(entry['title']['idString'], 'TMCanyon')
