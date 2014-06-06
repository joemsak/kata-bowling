try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Bowling Game',
    'author': 'Joe Sak',
    'url': 'https://github.com/joemsak/kata-bowling/tree/master/python',
    'download_url': 'https://github.com/joemsak/kata-bowling/tree/master/python',
    'author_email': 'joe@joesak.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['game'],
    'scripts': [],
    'name': 'bowlinggame'
}

setup(**config)
