sdict = {
	'name' : 'servo',
	'version' : '0.0.1',
	'author' : 'Gauthier Monserand',
	'license' : 'GPL-3',
	'packages' : ['servo'],
	'scripts' : ["dxl-cm-toss", "dxl-dump-position", "dxl-dump-state", "dxl-load-position", "dxl-ping", "dxl-scan", "dxl-set-position", "dxl-torque-disable", "dxl-torque-enable", "dxl-wheel"]
}

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

setup(**sdict)

