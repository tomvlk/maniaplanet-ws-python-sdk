from social_core.backends.oauth import BaseOAuth2

from .. import *


class ManiaConnectOAuth2(BaseOAuth2):
	"""
	ManiaConnect ManiaPlanet OAuth2 Backend.
	"""
	name = 'maniaconnect'
	AUTHORIZATION_URL = API_OAUTH_AUTHORIZATION_URL
	ID_KEY = API_OAUTH_ID_KEY

	REFRESH_TOKEN_URL = API_OAUTH_REFRESH_TOKEN_URL
	REFRESH_TOKEN_METHOD = API_OAUTH_REFRESH_TOKEN_METHOD
	ACCESS_TOKEN_URL = API_OAUTH_ACCESS_TOKEN_URL
	ACCESS_TOKEN_METHOD = API_OAUTH_ACCESS_TOKEN_METHOD

	SCOPE_SEPARATOR = ' '
	RESPONSE_TYPE = 'code'
	STATE_PARAMETER = False
	DEFAULT_SCOPE = ['basic', 'email']

	def get_user_details(self, response):
		return {
			'username': response.get('login'),
			'mp_login': response.get('login'),
			'mp_path': response.get('path'),
			'mp_id': response.get('id'),
			'mp_nickname': response.get('nickname'),
			'email': response.get('email'),
		}

	def user_data(self, access_token, *args, **kwargs):
		"""
		Get user data from ManiaPlanet WS.
		:param access_token:
		:param args:
		:param kwargs:
		:return:
		"""
		# TODO: Use WS class.
		headers = {
			'Authorization': 'Bearer {}'.format(access_token),
			'Accept': 'application/json',
		}

		details = self.get_json('https://ws.maniaplanet.com/player/', headers=headers)
		if 'email' in self.get_scope():
			details['email'] = self.get_json('https://ws.maniaplanet.com/player/email/', headers=headers)

		return details
