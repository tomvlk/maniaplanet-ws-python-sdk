from . import WebserviceMixin, WebserviceMethods


class Methods(WebserviceMethods):
	"""
	Zones Methods.
	"""
	def detail(self, id=None, path=None):
		"""
		Get single zone information on ID or Path.

		:param id: ID of the zone.
		:param path: Path of the zone.
		:type id: int
		:type path: str
		:return: server response
		:rtype: requests.Response, dict
		"""
		if id is not None and not path:
			return self._client.request('/zones/id/{:d}/'.format(id))
		elif path and id is None:
			return self._client.request('/zones/path/{:s}/'.format(path))
		else:
			raise Exception('Can only get a zone by id or path. You must provide one of the two.')

	def children(self, id=None, path=None, sort=None, order=None, offset=0, length=100):
		"""
		Get children of a specified zone on ID or Path.

		:param id: ID of the zone.
		:param path: Path of the zone.
		:param sort: Sort on specific column, like 'id', 'name'
		:param order: 1 or -1
		:param offset: Offset of list.
		:param length: Length of list.
		:type id: int
		:type path: str
		:type sort: str
		:type order: int
		:type offset: int
		:type length: int
		:return: server response
		:rtype: requests.Response, dict
		"""
		args = dict(sort=sort, order=order)
		if id is not None and not path:
			return self._client.request('/zones/id/{:d}/children/'.format(id), args=args, offset=offset, length=length)
		elif path and id is None:
			return self._client.request('/zones/path/{:s}/children/'.format(path), args=args, offset=offset,
										length=length)
		else:
			raise Exception('Can only get children of a zone by id or path. You must provide one of the two.')

	def all(self, sort=None, order=None, offset=0, length=100):
		"""
		Get list of all zones.
		:param sort: Sort on specific column, like 'id', 'name'
		:param order: 1 or -1
		:param offset: Offset of list, defaults to 0.
		:param length: Length of list, defaults to 100
		:type sort: str
		:type order: int
		:type offset: int
		:type length: int
		:return: server response
		:rtype: requests.Response, dict
		"""
		return self._client.request('/zones/all/', args=dict(sort=sort, order=order), offset=offset, length=length)

	def population(self, id=None, path=None):
		"""
		Get details about the population from a zone id or path.
		:param id: Zone ID
		:param path: Zone Path.
		:type id: int
		:type path: str
		:return: server response
		:rtype: requests.Response, dict
		"""
		if id is not None and not path:
			return self._client.request('/zones/id/{:d}/population/'.format(id))
		elif path and id is None:
			return self._client.request('/zones/path/{:s}/population/'.format(path))
		else:
			raise Exception('Can only get population of a zone by id or path. You must provide one of the two.')

	def id(self, path):
		"""
		Get ID of zone by path.
		:param path: Zone Path.
		:type path: str
		:return: server response
		:rtype: requests.Response, dict
		"""
		return self._client.request('/zones/path/{:s}/id/'.format(path))


#
#####
#

class ZonesMixin(WebserviceMixin):
	"""
	Zones mixin.
	"""
	def __init__(self):
		self.zones = Methods(self)

		super().__init__()
