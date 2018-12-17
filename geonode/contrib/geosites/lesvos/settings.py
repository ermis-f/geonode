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
# Geosite settings
###############################################

import os
from geonode.contrib import geosites

# Directory of master site
GEOSITES_ROOT = os.path.dirname(geosites.__file__)
SITE_ROOT = os.path.dirname(__file__)

try:
    # read in project pre_settings
    execfile(os.path.join(SITE_ROOT, '../', 'pre_settings.py'))
except:
    # if not available, read in GeoSites pre_settings
    execfile(os.path.join(GEOSITES_ROOT, 'pre_settings.py'))

SITE_ID = 2  # flake8: noqa
SITE_NAME = 'lesvos'
# Should be unique for each site
SECRET_KEY = "fbk3Ctrw3N6jt1AU9mGIcI"

# site installed apps
SITE_APPS = ()

# Site specific databases
SITE_DATABASES = {}

# Overrides

# Below are some common GeoNode settings that might be overridden for site

# base urls for all sites
# ROOT_URLCONF = 'projectname.urls'

# admin email
# THEME_ACCOUNT_CONTACT_EMAIL = ''

# Have GeoServer use this database for this site
# DATASTORE = ''i
# Where should newly created maps be focused?
DEFAULT_MAP_CENTER = (26.15, 39.15)

# How tightly zoomed should newly created maps be?
# 0 = entire world;
# maximum zoom is between 12 and 15 (for Google Maps, coverage varies by area)
DEFAULT_MAP_ZOOM = 10

# Allow users to register
# REGISTRATION_OPEN = True

# Read in GeoSites post_settings
try:
    # read in project pre_settings
    execfile(os.path.join(SITE_ROOT, '../', 'post_settings.py'))
except:
    # if not available, read in GeoSites pre_settings
    execfile(os.path.join(GEOSITES_ROOT, 'post_settings.py'))
