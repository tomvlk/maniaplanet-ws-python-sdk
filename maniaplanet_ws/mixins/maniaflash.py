from . import WebserviceMixin, WebserviceMethods


class Methods(WebserviceMethods):
	"""
	Maniaflash Methods.
	"""
	def channel(self, id):
		"""
		Get channel information based on the string identifier.

		:param id: String identifier of the channel.
		:type id: str
		:return: server response
		:rtype: requests.Response, dict
		"""
		return self._client.request('/maniaflash/channels/{:s}/'.format(id))

	def messages(self, id=None, hashtag=None, offset=0, length=100):
		"""
		Get messages by channel id or by hashtag.
		:param id: Channel identifier.
		:param hashtag: Hashtag to search for.
		:param offset: List offset.
		:param length: List max length.
		:return: server response
		:rtype: requests.Response, dict
		"""
		if id and not hashtag:
			return self._client.request('/maniaflash/channels/{:s}/messages/'.format(id), offset=offset, length=length)
		elif hashtag and not id:
			return self._client.request('/maniaflash/hashtags/{:s}/messages/'.format(hashtag), offset=offset, length=length)
		else:
			raise Exception('Can only get messages by channel ID or hashtag. You must provide one of the two.')


#
#####
#

class ManiaflashMixin(WebserviceMixin):
	"""
	Maniaflash mixin.
	"""
	def __init__(self):
		self.maniaflash = Methods(self)

		super().__init__()
