from . import WebserviceSubject, WebserviceMixin, WebserviceMethods


def get_title_endpoint(title):
	mapping = {
		'SMStorm': 'storm',
		'TMCanyon': 'canyon',
		'SMStormRoyal@nadeolabs': 'royal',
		'TMStadium': 'stadium',
		'SMStormElite@nadeolabs': 'elite',
		'TMValley': 'valley'
	}
	if title in mapping:
		return mapping[title]
	return 'titles'


class Methods(WebserviceMethods):

	def __init__(self, client, section, specific=None):
		self.__section = section
		self.__specific = specific

		super().__init__(client)

	def __ranking_request(
		self,
		title,
		login='',
		path='',
		challenge='',

		url_post='',

		**kwargs
	):
		"""
		You should never call this, this is a private method inside of the rankings methods structure.

		:param title:
		:param login:
		:param path:
		:param challenge:
		:param url_post:
		:param kwargs:
		:return:
		:rtype: requests.Response
		"""
		title_endpoint = get_title_endpoint(title)

		if self.__specific == 'challenge':
			url_post = 'challenge'

		url = '/{title_endpoint}/rankings/{section}/{post}'.format(
			title_endpoint=title_endpoint,
			section=self.__section,
			post=url_post.format(
				login=login,
				path=path,
				challenge=challenge,
			)
		)

		return self._client.request(path=url, **kwargs)

	def world(self, **kwargs):
		"""
		Get world ranking.
		Make sure you give the right parameters, such as 'title' and if required 'login', 'path' and 'challenge' too.

		:param title: TitleID, like TMCanyon
		:type title: str

		:param kwargs:
		:rtype: requests.Response
		:return:
		"""
		kwargs.update({'url_post': 'zone/'})
		return self.__ranking_request(**kwargs)

	def player(self, **kwargs):
		"""
		Get player ranking
		Make sure you give the right parameters, such as 'title' and if required 'login', 'path' and 'challenge' too.

		:param title: TitleID, like TMCanyon
		:type title: str

		:param login: Player login.
		:type login: str

		:param kwargs:
		:rtype: requests.Response
		:return:
		"""
		kwargs.update({'url_post': 'player/{login}/'})
		return self.__ranking_request(**kwargs)

	def zone(self, **kwargs):
		"""
		Get player ranking
		Make sure you give the right parameters, such as 'title' and if required 'login', 'path' and 'challenge' too.

		:param title: TitleID, like TMCanyon
		:type title: str

		:param path: Path to select.
		:type path: str

		:param kwargs:
		:rtype: requests.Response
		:return:
		"""
		kwargs.update({'url_post': 'zone/{path}/'})
		return self.__ranking_request(**kwargs)


class SoloMethods(Methods):
	def __init__(self, client, section):
		self.challenge = Methods(client, 'solo', 'challenge')
		super().__init__(client, section)


#
#####
#

class Subject(WebserviceSubject):

	def __init__(self, client):
		self.solo = SoloMethods(client, 'solo')
		self.multiplayer = Methods(client, 'multiplayer')

		super().__init__(client)


class RankingsMixin(WebserviceMixin):
	def __init__(self):
		self.rankings = Subject(self)

		super().__init__()
