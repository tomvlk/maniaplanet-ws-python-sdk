from ..base import ClientTestCase


class ZonesTest(ClientTestCase):
	def test_id(self):
		res = self.client.zones.id(path='World|Europe|France')
		self.assertEqual(res.status_code, 200)
		self.assertEqual(int(res.json()), 2)

	def test_details(self):
		# By Path
		res = self.client.zones.detail(path='World|Europe|France')
		self.assertEqual(res.status_code, 200)
		data = res.json()

		self.assertEqual(int(data['id']), 2)
		self.assertEqual(data['name'], 'France')

		# By ID
		res = self.client.zones.detail(id=2)
		self.assertEqual(res.status_code, 200)
		data = res.json()

		self.assertEqual(int(data['id']), 2)
		self.assertEqual(data['name'], 'France')

	def test_children(self):
		# By Path
		res = self.client.zones.children(path='World|Europe|France')
		self.assertEqual(res.status_code, 200)
		data = res.json()

		self.assertEqual(len(data), 23)

		# By ID
		res = self.client.zones.children(id=2)
		self.assertEqual(res.status_code, 200)
		data = res.json()

		self.assertEqual(len(data), 23)

	def test_list(self):
		res = self.client.zones.all()
		self.assertEqual(res.status_code, 200)
		data = res.json()

		self.assertEqual(len(data), 100)

		res = self.client.zones.all(length=5)
		self.assertEqual(res.status_code, 200)
		data = res.json()

		self.assertEqual(len(data), 5)

	def test_population(self):
		res = self.client.zones.population(path='World|Europe|France')
		self.assertEqual(res.status_code, 200)
		data = res.json()
		self.assertGreater(int(data), 300000)

		res = self.client.zones.population(id=2)
		self.assertEqual(res.status_code, 200)
		data = res.json()
		self.assertGreater(int(data), 300000)
