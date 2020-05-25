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
from django import forms
from django.forms import widgets as w
from django.conf import settings

from autocomplete_light.widgets import MultipleChoiceWidget

import autocomplete_light
import logging
import traceback

logger = logging.getLogger(__name__)

class MultiThesauriWidget(w.MultiWidget):
    def __init__(self, attrs=None):
        widget_list = []
        #logger.error("MULTITHESAURUSWIDGET")
        for el in settings.THESAURI:
        #if hasattr(settings, 'THESAURI') and settings.THESAURI:
        #    el = settings.THESAURI
        #    widget_name=el['name']   
            cleaned_name = el['name'].replace("-", " ").replace("_", " ").title()
            #logger.error(cleaned_name)
            widget_list.append(
                autocomplete_light.widgets.MultipleChoiceWidget(
                #w.SelectMultiple(
                    'thesaurus_' + el['name'],
                    attrs={'placeholder': '%s - Start typing for suggestions' % cleaned_name},
                    extra_context={'thesauri_title': cleaned_name}))
        widgets = tuple(widget_list)
        #logger.error(widgets)
        super(MultiThesauriWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        logger.error("DECOMPRESWIDJET")
        logger.error(value)
        if value:
            return [map(int, value.split(','))]
        return [None, None, None]

    def compress(self, data_list):
        logger.error("COMPRESSWIDGET")
        logger.error(data_list)
        if data_list:
            return '%s' % (data_list[0])
        return None

    def format_output(self, rendered_widgets):
        return u'\n'.join(rendered_widgets)
	#    super(MultiThesauriWidget, self).__init__(
	#	'thesaurus_' + widget_name,
	#	 attrs={'placeholder': '%s - Start typing for suggestions' % cleaned_name},
	#	 extra_context={'thesauri_title': cleaned_name})
        #else:
        #   super(MultiThesauriWidget, self).__init__([], attrs)
