"""
Maniaplanet Webservice SDK Library for Python 3.4+.
Copyright Tom Valk. Please see LICENSE file in root of project.

This module provides a python interface for communicating with the Maniaplanet Webservice.
For this module to work you need to have a Maniaplanet account and Webservice credentials. The Webservice credentials
can be retrieved from the player page:
https://player.maniaplanet.com
"""
__version__ = '0.0.1'
__author__ = 'Tom Valk'

API_URL = 'https://ws.maniaplanet.com'
API_HOST = 'ws.maniaplanet.com'

API_OAUTH_AUTHORIZATION_URL = API_URL + '/oauth2/authorize/'
API_OAUTH_ID_KEY = 'id'

API_OAUTH_REFRESH_TOKEN_URL = API_URL + '/oauth2/token/'
API_OAUTH_REFRESH_TOKEN_METHOD = 'POST'
API_OAUTH_ACCESS_TOKEN_URL = API_URL + '/oauth2/token/'
API_OAUTH_ACCESS_TOKEN_METHOD = 'POST'

######################################################################################
from .api import ManiaplanetWS

__all__ = [
	'ManiaplanetWS',
	
	'__author__',
	'__version__',
	'API_URL',
	'API_HOST',
	'API_OAUTH_AUTHORIZATION_URL',
	'API_OAUTH_ID_KEY',
	'API_OAUTH_REFRESH_TOKEN_URL',
	'API_OAUTH_REFRESH_TOKEN_METHOD',
	'API_OAUTH_ACCESS_TOKEN_URL',
	'API_OAUTH_ACCESS_TOKEN_METHOD',
]
