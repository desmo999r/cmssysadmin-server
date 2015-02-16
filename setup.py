#!/usr/bin/env python

#from distutils.core import setup
from setuptools import setup,find_packages

setup(
		name='python-cmsracklayout',
		version='0.2',
		description='CMS Sysadmin Django applications',
		author='Jean-Marc ANDRE',
		author_email='jm.andre@cern.ch',
		include_package_data=True,
		url='https://github.com/desmo999r/cmssysadmin',
#		packages=['cmsracklayout', 'cmsracklayout.api', 'cmsracklayout.racklayout'],
		packages=find_packages(),
		package_data = {
			'':  ['*.example'],
		},
)
