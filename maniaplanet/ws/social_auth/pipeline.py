"""
Social Auth pipeline for associating by username (login) of maniaplanet.
"""

USER_FIELDS = ['username', 'email']


def associate_by_username_or_create(strategy, details, backend, *args, **kwargs):
	"""
	Associate by username or create new user.

	:param strategy:
	:param details:
	:param backend:
	:param args:
	:param kwargs:
	:return:
	"""
	storage = strategy.storage
	is_new = False
	user = None

	if not storage.user.user_exists(username=details['username']):
		fields = dict(
			(name, kwargs.get(name, details.get(name)))
			for name in backend.setting('USER_FIELDS', USER_FIELDS)
		)
		if not fields:
			return

		user = strategy.create_user(
			username=details['username'],
			email=details['email']
		)
		is_new = True

	return {
		'is_new': is_new,
		'user': user
	}
