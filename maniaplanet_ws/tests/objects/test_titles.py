from ..base import ClientTestCase


class TitlesTest(ClientTestCase):
	def test_title_detail(self):
		res = self.client.titles.detail(id='TMCanyon')
		self.assertEqual(res.status_code, 200)

		# Due to weird response, the invalid title can't be really tested.
		res = self.client.titles.detail(id='ThisTitleDoesntExist')
		self.assertEqual(res.status_code, 200)

		# TODO: Check contents
