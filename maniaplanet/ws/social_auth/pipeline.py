
USER_FIELDS = ['username', 'email']


def associate_by_username_or_create(strategy, details, backend, *args, **kwargs):
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
