import os
import re
from setuptools import setup, find_packages


PKG = 'maniaplanet-ws-sdk'
VERSION_FILE = os.path.join('maniaplanet', 'ws', '__init__.py')
version = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", open(VERSION_FILE, 'rt').read(), re.M).group(1)

README_FILE = 'README.md'
readme = open(README_FILE).read()

REQUIREMENTS_FILE = 'requirements.txt'
requirements = open(REQUIREMENTS_FILE, 'rt').readlines()

TEST_REQUIREMENTS_FILE = 'requirements-test.txt'
test_requirements = open(TEST_REQUIREMENTS_FILE, 'rt').readlines()

######
setup(
	name=PKG,
	version=version,
	description='ManiaPlanet Webservice SDK for Python',
	long_description=readme,
	keywords='maniaplanet, sdk',
	license='GNU Lesser General Public License v3 (LGPLv3)',
	packages=find_packages(),
	package_data={
		'maniaplanet/ws/tests': ['maniaplanet/ws/tests/**.txt', 'maniaplanet/ws/tests/**.json']
	},
	install_requires=requirements,
	tests_require=test_requirements,
	test_suite='maniaplanet.sdk.tests',
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
