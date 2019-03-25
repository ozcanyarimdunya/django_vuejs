import os

from .base import *

if os.getenv('MODE') == 'PRODUCTION':
    from .production import *
else:
    from .local import *