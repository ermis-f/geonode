# flake8: noqa
# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2016 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

##### Settings to be included last

###############################################
# Master Geosite settings
# These settings are called at/near the end of a GeoSite settings
# to finalize some derived settings
###############################################

# geonode local_settings
try:
    # load in local_settings from system installed geonode
    execfile(os.path.join(GEONODE_ROOT, 'local_settings.py'))
except:
    # there are no system geonode local_settings to import
    pass

# master local_settings
try:
    # load in local_settings (usually for setting SITEURL and DATABASES for production)
    execfile(os.path.join(SITE_ROOT, '../', 'local_settings.py'))
except:
    # there are no master local_settings to import
    pass

# site local_settings
try:
    # load in local_settings (usually for setting SITEURL and DATABASES for production)
    execfile(os.path.join(SITE_ROOT, 'local_settings.py'))
except:
    # there are no site local_settings to import
    pass

OGC_SERVER['default']['LOCATION'] = GEOSERVER_URL
#OGC_SERVER['default']['LOCATION'] = os.path.join(SITEURL, 'geoserver/')
OGC_SERVER['default']['PUBLIC_LOCATION'] = os.path.join(SITEURL, 'geoserver/')
CATALOGUE['default']['URL'] = '%scatalogue/csw' % SITEURL
PYCSW['CONFIGURATION']['metadata:main']['provider_url'] = SITEURL
LOCAL_GEOSERVER['source']['url'] = OGC_SERVER['default']['PUBLIC_LOCATION'] + 'ows'

#STATICFILES_DIRS.append(os.path.join(SITE_ROOT, "static/"))
#STATICFILES_DIRS.append(os.path.join(PROJECT_ROOT, "static/"))
STATICFILES_DIRS.append(os.path.join(GEONODE_ROOT, "static"))
STATICFILES_DIRS.append(os.path.join(PROJECT_ROOT, "static"))
STATICFILES_DIRS.append(os.path.join(SITE_ROOT, "static"))

# Directories to search for templates
#TEMPLATE_DIRS = (
#    os.path.join('/home/geo/Envs/geonode/src/geonode/geonode/contrib/geosites/lesvos/', 'templates/'),
#    os.path.join('/home/geo/Envs/geonode/src/geonode/geonode/contrib/geosites/', 'templates/'),
#    os.path.join('/home/geo/Envs/geonode/src/geonode/geonode/', 'templates/'),
#)
#TEMPLATES[0]['DIRS'].insert(0, '/home/geo/Envs/geonode/src/geonode/geonode/contrib/geosites/lesvos/templates/')
#TEMPLATES[0]['DIRS'].insert(0, '/home/geo/Envs/geonode/src/geonode/geonode/contrib/geosites/templates/')

TEMPLATES[0]['DIRS'].insert(0, '/home/geo/Envs/geonode/src/geonode/geonode/templates')
TEMPLATES[0]['DIRS'].insert(0, '/home/geo/Envs/geonode/src/geonode/geonode/contrib/geosites/templates')
TEMPLATES[0]['DIRS'].insert(0, '/home/geo/Envs/geonode/src/geonode/geonode/contrib/geosites/lesvos/templates')

loaders = TEMPLATES[0]['OPTIONS'].get('loaders') or ['django.template.loaders.filesystem.Loader','django.template.loaders.app_directories.Loader']
# loaders.insert(0, 'apptemplates.Loader')
TEMPLATES[0]['OPTIONS']['loaders'] = loaders
TEMPLATES[0].pop('APP_DIRS', None)

# Directories which hold static files
#STATICFILES_DIRS = (
#    os.path.join(SITE_ROOT, 'static/'),
#    os.path.join(PROJECT_ROOT, 'static/'),
#    os.path.join(GEONODE_ROOT, 'static/')
#)

#STATICFILES_DIRS.append(os.path.join(SITE_ROOT, "static/"))
#STATICFILES_DIRS.append(os.path.join(PROJECT_ROOT, "static/"))
#STATICFILES_DIRS.append(os.path.join(GEONODE_ROOT, "static/"))

# Update databases if site has own database
if SITE_DATABASES:
    DATABASES.update(SITE_DATABASES)

# Update apps if site has own apps
if SITE_APPS:
	INSTALLED_APPS += SITE_APPS

# Put static files in root
STATIC_ROOT = os.path.join(SERVE_PATH, 'static_root/lesvos/')

# Put media files in root
MEDIA_ROOT = os.path.join(SERVE_PATH, 'uploaded')

#OGC_SERVER['default']['LOCATION'] = os.path.join(GEOSERVER_URL, 'geoserver/')
#STATIC_URL = os.path.join(SITEURL,'static/')

# add datastore if defined
if DATASTORE in DATABASES.keys():
    OGC_SERVER['default']['DATASTORE'] = DATASTORE


# If using nginx/gunicorn this should be added
# add gunicorn logging
# LOGGING['handlers']['gunicorn'] = {
#     'level': 'DEBUG',
#     'class': 'logging.handlers.RotatingFileHandler',
#     'formatter': 'verbose',
#     'filename': '/geo/logs/gunicorn.errors',
# }
# LOGGING['loggers']['gunicorn'] = {
#     'level': 'DEBUG',
#     'handlers': ['gunicorn'],
#     'propagate': True,
# }

# DEBUG_TOOLBAR can interfere with Django - keep it off until needed
if DEBUG_TOOLBAR:
    DEBUG_TOOLBAR_PATCH_SETTINGS = False
    def show_if_superuser(request):
        return True if request.user.is_superuser else False
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INSTALLED_APPS += ('debug_toolbar',)
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
        'SHOW_TOOLBAR_CALLBACK': 'cdesign.settings.show_if_superuser',
    }

GEOSERVER_LOCATION = os.getenv(
    'GEOSERVER_LOCATION', 'http://lesvos-ermis-floods-dev.aegean.gr/geoserver/'
)

GEOSERVER_PUBLIC_HOST = os.getenv(
    'GEOSERVER_PUBLIC_HOST', 'lesvos-ermis-floods-dev.aegean.gr'
)

GEOSERVER_PUBLIC_PORT = os.getenv(
    'GEOSERVER_PUBLIC_PORT', 80
)

GEOSERVER_PUBLIC_LOCATION = os.getenv(
    'GEOSERVER_PUBLIC_LOCATION', 'http://{}:{}/geoserver/'.format(GEOSERVER_PUBLIC_HOST, GEOSERVER_PUBLIC_PORT)
)

OGC_SERVER_DEFAULT_USER = os.getenv(
    'GEOSERVER_ADMIN_USER', 'admin'
)

OGC_SERVER_DEFAULT_PASSWORD = os.getenv(
    'GEOSERVER_ADMIN_PASSWORD', 'geoserver'
)

# OGC (WMS/WFS/WCS) Server Settings
OGC_SERVER = {
    'default': {
        'BACKEND': 'geonode.geoserver',
        'LOCATION': GEOSERVER_LOCATION,
        'LOGIN_ENDPOINT': 'j_spring_oauth2_geonode_login',
        'LOGOUT_ENDPOINT': 'j_spring_oauth2_geonode_logout',
        # PUBLIC_LOCATION needs to be kept like this because in dev mode
        # the proxy won't work and the integration tests will fail
        # the entire block has to be overridden in the local_settings
        'PUBLIC_LOCATION': GEOSERVER_PUBLIC_LOCATION,
        'USER': OGC_SERVER_DEFAULT_USER,
        'PASSWORD': OGC_SERVER_DEFAULT_PASSWORD,
        'MAPFISH_PRINT_ENABLED': True,
        'PRINT_NG_ENABLED': True,
        'GEONODE_SECURITY_ENABLED': True,
        'GEOFENCE_SECURITY_ENABLED': True,
        'GEOGIG_ENABLED': False,
        'WMST_ENABLED': False,
        'BACKEND_WRITE_ENABLED': True,
        'WPS_ENABLED': False,
        'LOG_FILE': '%s/geoserver/data/logs/geoserver.log' % os.path.abspath(os.path.join(PROJECT_ROOT, os.pardir)),
        # Set to dictionary identifier of database containing spatial data in DATABASES dictionary to enable
        'DATASTORE': 'datastore',
        'PG_GEOGIG': False,
        'TIMEOUT': 60  # number of seconds to allow for HTTP requests
    }
}

UPLOADER = {
    # 'BACKEND': 'geonode.rest',
    'BACKEND': 'geonode.importer',
    'OPTIONS': {
        'TIME_ENABLED': False,
        'MOSAIC_ENABLED': False,
        'GEOGIG_ENABLED': False,
    },
    'SUPPORTED_CRS': [
        'EPSG:4326',
        'EPSG:3785',
        'EPSG:3857',
        'EPSG:32647',
        'EPSG:32736'
	'EPSG:2100'
    ],
    'SUPPORTED_EXT': [
        '.shp',
        '.csv',
        '.kml',
        '.kmz',
        '.json',
        '.geojson',
        '.tif',
        '.tiff',
        '.geotiff',
        '.gml',
        '.xml'
    ]
}

#ACCOUNT_LOGIN_URL= 'http://lesvos-ermis-floods-dev.aegean.gr'
# Use kombu broker by default
# REDIS_URL = 'redis://localhost:6379/1'
# BROKER_URL = REDIS_URL
# CELERY_RESULT_BACKEND = REDIS_URL
CELERYD_HIJACK_ROOT_LOGGER = True
CELERYD_CONCURENCY = 1
# Set this to False to run real async tasks
CELERY_ALWAYS_EAGER = True
CELERYD_LOG_FILE = None
CELERY_REDIRECT_STDOUTS = True
CELERYD_LOG_LEVEL = 1

# Additional settings
CORS_ORIGIN_ALLOW_ALL = True

GEOIP_PATH = "/usr/local/share/GeoIP"

# add following lines to your local settings to enable monitoring
MONITORING_ENABLED = False

if MONITORING_ENABLED:
    if 'geonode.contrib.monitoring' not in INSTALLED_APPS:
        INSTALLED_APPS += ('geonode.contrib.monitoring',)
    if 'geonode.contrib.monitoring.middleware.MonitoringMiddleware' not in MIDDLEWARE_CLASSES:
        MIDDLEWARE_CLASSES += \
            ('geonode.contrib.monitoring.middleware.MonitoringMiddleware',)
    MONITORING_CONFIG = None
    MONITORING_HOST_NAME = os.getenv("MONITORING_HOST_NAME", HOSTNAME)
    MONITORING_SERVICE_NAME = 'geonode'

# Advanced Security Workflow Settings
SKIP_PERMS_FILTER = False
REGISTRATION_OPEN = False
ACCOUNT_APPROVAL_REQUIRED = True
CLIENT_RESULTS_LIMIT = 20
API_LIMIT_PER_PAGE = 1000
FREETEXT_KEYWORDS_READONLY = False
RESOURCE_PUBLISHING = False
ADMIN_MODERATE_UPLOADS = False
GROUP_PRIVATE_RESOURCES = False
GROUP_MANDATORY_RESOURCES = False
MODIFY_TOPICCATEGORY = True
USER_MESSAGES_ALLOW_MULTIPLE_RECIPIENTS = True
DISPLAY_WMS_LINKS = True

ACCOUNT_OPEN_SIGNUP = False
#ACCOUNT_APPROVAL_REQUIRED = False
ACCOUNT_EMAIL_CONFIRMATION_EMAIL = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = True

#DEFAULT_WORKSPACE = os.getenv('DEFAULT_WORKSPACE', 'geonode_lesvos')
#CASCADE_WORKSPACE = os.getenv('CASCADE_WORKSPACE', 'geonode_lesvos')

AUTH_LDAP_REQUIRE_GROUP = "cn=aeguni,ou=geonode,dc=ermis-floods-dev,dc=aegean,dc=gr"
