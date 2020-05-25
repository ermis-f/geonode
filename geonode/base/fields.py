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

import logging
import traceback

from django.forms import widgets
#from autocomplete_light.fields import MultipleChoiceField
from django.forms.fields import ChoiceField, MultiValueField, MultipleChoiceField
from .widgets import MultiThesauriWidget
from django.conf import settings

from geonode.base.models import Thesaurus

#logger = logging.getLogger("geonode.base.fields")
logger = logging.getLogger(__name__)


class MultiThesauriField(MultiValueField):
    def __init__(self, label=None, required=True, help_text=None, widget=None):
        fields_list = []
        for el in settings.THESAURI:
    
    #widget=widgets.SelectMultiple

    #def __init__(self, *args, **kwargs):
    #     super(MultiThesauriField, self).__init__(*args, **kwargs)
    #     self.require_all_fields = kwargs.pop('require_all_fields', True)

    #     if hasattr(settings, 'THESAURI') and settings.THESAURI:
            #el=settings.THESAURI
            choices_list = []
            #fields_list=[]
            thesaurus_name = el['name']
            #logger.error("MULTITHESAURIFIELD")
            #logger.error(thesaurus_name)
            try:
                t = Thesaurus.objects.get(identifier=thesaurus_name)
                for tk in t.thesaurus.all():
                    tkl = tk.keyword.filter(lang='en')
                    choices_list.append((tkl[0].id, tkl[0].label))
                    logger.error(tkl[0].label)
                    #logger.error(tkl[0].id)
                fields_list.append(MultipleChoiceField(choices=tuple(choices_list)))
                #logger.error(choices_list)
                #self.fields += (MultipleChoiceField(choices=tuple(choices_list)), )
                #logger.error(self.fields)              
            except BaseException:
                tb = traceback.format_exc()
                logger.error(tb)

        fields = tuple(fields_list)
        #fields=self.fields
        logger.error("FIELD")
        #logger.error(len(fields))

        super(MultiThesauriField, self).__init__(fields, required, widget, label)

    def compress(self, data_list):
        logger.error("Compress")
        logger.error(data_list) 
        if data_list:
            logger.error("COMPRESS")
            logger.error(data_list)
            logger.error(data_list[0])
            return '%s' % (data_list[0])
        return None

    #     for f in self.fields:
#		f.error_messages.setdefault('incomplete',
 #                                              self.error_messages['incomplete'])
  #              if self.require_all_fields:
   #             	f.required=False

