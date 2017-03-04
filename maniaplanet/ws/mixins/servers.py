from . import WebserviceMixin, WebserviceMethods


class Methods(WebserviceMethods):
	def detail(self, login):
		"""
		Get single server details by login of server.

		:param login: Login of the server.
		:type login: str
		:return: server response
		:rtype: requests.Response, dict
		"""
		return self._client.request('/servers/{:s}/'.format(login))

	def online_players(self, login):
		"""
		Get online players on specific server by login.

		:param login: Login of the server.
		:type login: str
		:return: server players response
		:rtype: requests.Response, dict
		"""
		return self._client.request('/servers/{:s}/players/'.format(login))

	def favorite_count(self, login):
		"""
		Get favorite count of a server by login.

		:param login: Login of the server.
		:type login: str
		:return: server favorite count response
		:rtype: requests.Response, dict
		"""
		return self._client.request('/servers/{:s}/favorited/'.format(login))

	def reported_abuses(self, login):
		"""
		Get abuse reports for a server by login.
		THIS METHOD IS NOT YET FULLY IMPLEMENTED, IT SHOULD SEND AN AUTHENTICATED REQUEST.

		:param login: Login of the server.
		:type login: str
		:return: server abuse reports response
		:rtype: requests.Response
		"""
		# TODO: THIS METHOD IS NOT YET FULLY IMPLEMENTED, IT SHOULD SEND AN AUTHENTICATED REQUEST.
		return self._client.request('/report-abuse/list/{:s}/'.format(login))

	def list(
		self,
		environment=None, title=None, players_min=None, players_max=None, hide_full=None, hide_empty=None,
		visibility=None, zone=None, mode=None, ladder_limit_min=None, ladder_limit_max=None,
		offset=0, length=100
	):
		"""
		Get server list with optional advanced filters.
		Explaination of the filters is done within the parameters. Look at the examples for more information.

		:param environment: Environment: Canyon, Storm, etc. (? unclear what exactly)
		:param title: TitleID, String ID of the title.
		:param players_min: Minimum number of players.
		:param players_max: Maximum number of players.
		:param hide_full: Hide full servers with no player places left.
		:param hide_empty: Hide empty servers.
		:param visibility: Filter on visibility: all, public, private
		:param zone: Zone: example: 'World|Europe'
		:param mode: Gamemode name, can be: -1: all, -2: official, -3: custom OR: name itself: TimeAttack, Melee, etc.
		:param ladder_limit_min: Minimum ladderpoints limit.
		:param ladder_limit_max: Maximum ladderpoints limit.
		:param offset: Offset of returned list.
		:param length: Length of returned list.

		:type environment: str
		:type title: str
		:type players_min: int
		:type players_max: int
		:type hide_full: bool
		:type hide_empty: bool
		:type visibility: str
		:type zone: str
		:type mode: int, str
		:type ladder_limit_min: int
		:type ladder_limit_max: int
		:type offset: int
		:type length: int

		:return: Response or data which contain the list of servers.
		:rtype: requests.Response, dict
		"""
		# Call the internal used api call so we can use the **kwargs while still using real parameter names
		# for several IDEs to understand the call.
		return self.__list(
			environment=environment, titleUids=title, playersMin=players_min, playersMax=players_max,
			hideFull=hide_full, hideEmpty=hide_empty, visibility=visibility, zone=zone, mode=mode, length=length,
			ladderLimitMin=ladder_limit_min, ladderLimitMax=ladder_limit_max, offset=offset
		)

	def __list(self, **kwargs):
		"""
		Internal used get_list.
		:param kwargs:
		:return: Response
		"""
		# Map the correct arguments.
		args = dict()
		for key, val in kwargs.items():
			if val is not None:
				args[key] = val

		# Pop length and offset.
		offset = args.pop('offset', None)
		length = args.pop('length', None)

		# Execute the call itself.
		return self._client.request('/servers/', args=args, offset=offset, length=length)


#
#####
#

class ServersMixin(WebserviceMixin):
	def __init__(self):
		self.servers = Methods(self)

		super().__init__()
