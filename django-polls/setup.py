import os 
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
	README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup (
	name = 'django-polls',
	version = '0.1',
	packages = find_packages(),
	include_package_data = True,
	license = 'LGPL_V3',
	description = 'A simple Django app to conduct Web-based polls',
	long_description = README,
	url = 'http://127.0.0.1:8000/polls',
	author = 'yorlysoro',
	author_email = 'yorlysoro@gmail.com',
	classifiers=[
		'Envoriment ::  Web Envoriment',
		'Framework  ::  Django',
		'Framework  ::  Django :: 1.11',
		'Intended Aundence :: Developers',
		'License :: OSI Approved :: LGPL_V3',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.7.3',
		'Topic :: Internet :: WWW/HTTP',
		'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
		],

	)