import environ
import os

from .setting_base import *

### Reading .env file ###
# Set the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Set environment variable initial values
env = environ.Env()

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

### Secret and Debug ###
SECRET_KEY = env.str('SECRET_KEY', default='PleasePutSecretInENV')
DEBUG = env.bool('DEBUG', default=True) # Set True when in development mode

### Allowed Hosts ###
ALLOWED_HOSTS = tuple(env.list('ALLOWED_HOSTS', default=[]))

### Databases ###
DATABASES = {
    'default': env.db(),
    'extra': env.db_url(
        'SQLITE_URL',
        default='sqlite:////tmp/my-tmp-sqlite.db'
    )
}

TIME_INPUT_FORMAT = [
    '$I:%M:%S %p',
    '$I:%M %p',
    '$I %p',
    '%H:%M:%S',
    '%H:%M:%S.$f',
    '%H:%M',
]
    