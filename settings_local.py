from django.conf import settings
"""
Local settings for the project.

These settings complement (and override) those in ``settings.py``.
"""

# Assuming that by default we're having a development environment.
DEBUG = True
TEMPLATE_DEBUG = DEBUG
LOG_LEVEL = logging.DEBUG

#EMAIL_HOST = ''
#EMAIL_HOST_USER = ''
#EMAIL_HOST_PASSWORD = ''
#EMAIL_USE_TLS = True
#EMAIL_PORT = 587

#SCRATCH_DIR = os.path.join('/tmp', 'scratchdir')

INSTALLED_APPS += ['django_evolution',]

#Disable use of authopenid app and fall back to simple auth:
#INSTALLED_APPS.remove('django_authopenid')
#INSTALLED_APPS += ['simpleauth']

# To enable the use of the notification app on your system:
#ENABLE_NOTICES = True
#TEMPLATE_CONTEXT_PROCESSORS += ["notification.context_processors.notification",]
