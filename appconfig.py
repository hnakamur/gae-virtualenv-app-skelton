#-*- encoding: utf-8 -*-

from google.appengine.api import lib_config

import os

# some of contant values are overrided in appengine_config.py
_config = lib_config.register('app', {
    'DEBUG': os.environ['SERVER_SOFTWARE'].startswith('Development')
    })
