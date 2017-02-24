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

from .api import ManiaplanetWS
