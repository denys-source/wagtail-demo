from .base import *

DEBUG = False

SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY", "$1hg342ms&mcoi=%2(a3t=xw&5#&qvl&gmg94e(b+q$8!dux62"
)

ALLOWED_HOSTS = ["35.184.160.126"]

try:
    from .local import *
except ImportError:
    pass
