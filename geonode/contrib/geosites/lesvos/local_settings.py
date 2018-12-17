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

###############################################
# Geosite local settings
###############################################
import os

# Outside URL
#SITEURL = 'http://$DOMAIN'
SITEURL = 'http://lesvos-ermis-floods-dev.aegean.gr'
SITE_HOST_NAME = os.getenv('SITE_HOST_NAME', 'lesvos-ermis-floods-dev.aegean.gr')
SITE_HOST_PORT = os.getenv('SITE_HOST_PORT', "80")

SITEURL = os.getenv('SITEURL', "http://%s:%s/" % (SITE_HOST_NAME, SITE_HOST_PORT))


# add trailing slash to site url. geoserver url will be relative to this
if not SITEURL.endswith('/'):
    SITEURL = '{}/'.format(SITEURL)

# databases unique to site if not defined in site settings
"""
SITE_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, '../development.db'),
    },
}
"""
