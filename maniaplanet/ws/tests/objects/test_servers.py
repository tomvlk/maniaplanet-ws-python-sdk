from ..base import ClientTestCase


class ServersTest(ClientTestCase):
	def test_retrieval(self):
		request_res = self.client.request('/servers/droppie666/')
		self.assertEqual(request_res.status_code, 200)

		# Retrieve with the subject classes.
		subject_res = self.client.servers.get(login='droppie666')
		self.assertEqual(subject_res.status_code, 200)

		# Compare the native and the subject responses.
		self.assertEqual(request_res.headers.get('Content-Size'), subject_res.headers.get('Content-Size'))

	def test_single_server(self):
		# Should give 404 as we don't provide the login.
		res = self.client.servers.get(login='thisserverdoesntexists')
		self.assertEqual(res.status_code, 404)

		res = self.client.servers.get(login='droppie666')
		self.assertEqual(res.status_code, 200)

		# TODO: Check contents
