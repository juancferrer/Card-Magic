#!/usr/bin/env python

from distutils.core import setup

setup(name='Card-Magic',
      version='1.0',
      description='The best card and decks ever',
      author='Juan Carlos Ferrer',
      author_email='juan.carlos@micronixsolutions.com',
      packages=['cardmagic', 'cardmagic.tests'],
      package_data = {
          'cardmagic': [
              'translations/en/LC_MESSAGES/*', 
              'translations/es/LC_MESSAGES/*'],
                },
     )
