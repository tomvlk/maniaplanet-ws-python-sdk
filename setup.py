import os
import re
from setuptools import setup, find_packages


def long_description():
	try:
		return open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
	except IOError:
		return None


def read_version():
	with open(os.path.join(os.path.dirname(__file__), 'maniaplanet', 'ws', '__init__.py')) as handler:
		return re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", handler.read(), re.M).group(1)


def read_requirements(filename):
	with open(os.path.join(os.path.dirname(__file__), filename), 'r') as handler:
		return [line for line in handler.readlines() if not line.startswith('-') and not len(line)]


PKG = 'maniaplanet-ws'
######
setup(
	name=PKG,
	version=read_version(),
	description='ManiaPlanet Webservice SDK for Python',
	long_description=long_description(),
	keywords='maniaplanet, sdk',
	license='GNU Lesser General Public License v3 (LGPLv3)',
	packages=find_packages(),
	package_data={
		'maniaplanet/ws/tests': ['maniaplanet/ws/tests/**.txt', 'maniaplanet/ws/tests/**.json']
	},
	install_requires=read_requirements('requirements.txt'),
	tests_require=read_requirements('requirements-test.txt'),
	test_suite='nose.collector',
	include_package_data=True,

	author='Tom Valk',
	author_email='tomvalk@lt-box.info',
	url='https://github.com/tomvlk/maniaplanet-ws-python-sdk',

	classifiers=[
		'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',

		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3 :: Only',

		'Development Status :: 1 - Planning',

		'Topic :: Internet :: WWW/HTTP',
		'Topic :: Software Development',

	],

	zip_safe=False,
)
