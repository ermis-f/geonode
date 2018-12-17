# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0028_auto_20180606_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='language',
            field=models.CharField(default=b'el', max_length=10, verbose_name='language', choices=[('af', 'Afrikaans'), ('ar', '\u0627\u0644\u0639\u0631\u0628\u064a\u0651\u0629'), ('ast', 'asturian'), ('az', 'Az\u0259rbaycanca'), ('bg', '\u0431\u044a\u043b\u0433\u0430\u0440\u0441\u043a\u0438'), ('be', '\u0431\u0435\u043b\u0430\u0440\u0443\u0441\u043a\u0430\u044f'), ('bn', '\u09ac\u09be\u0982\u09b2\u09be'), ('br', 'brezhoneg'), ('bs', 'bosanski'), ('ca', 'catal\xe0'), ('cs', '\u010desky'), ('cy', 'Cymraeg'), ('da', 'dansk'), ('de', 'Deutsch'), ('el', '\u0395\u03bb\u03bb\u03b7\u03bd\u03b9\u03ba\u03ac'), ('en', 'English'), ('en-au', 'Australian English'), ('en-gb', 'British English'), ('eo', 'Esperanto'), ('es', 'espa\xf1ol'), ('es-ar', 'espa\xf1ol de Argentina'), ('es-mx', 'espa\xf1ol de Mexico'), ('es-ni', 'espa\xf1ol de Nicaragua'), ('es-ve', 'espa\xf1ol de Venezuela'), ('et', 'eesti'), ('eu', 'Basque'), ('fa', '\u0641\u0627\u0631\u0633\u06cc'), ('fi', 'suomi'), ('fr', 'fran\xe7ais'), ('fy', 'frysk'), ('ga', 'Gaeilge'), ('gl', 'galego'), ('he', '\u05e2\u05d1\u05e8\u05d9\u05ea'), ('hi', 'Hindi'), ('hr', 'Hrvatski'), ('hu', 'Magyar'), ('ia', 'Interlingua'), ('id', 'Bahasa Indonesia'), ('io', 'ido'), ('is', '\xcdslenska'), ('it', 'italiano'), ('ja', '\u65e5\u672c\u8a9e'), ('ka', '\u10e5\u10d0\u10e0\u10d7\u10e3\u10da\u10d8'), ('kk', '\u049a\u0430\u0437\u0430\u049b'), ('km', 'Khmer'), ('kn', 'Kannada'), ('ko', '\ud55c\uad6d\uc5b4'), ('lb', 'L\xebtzebuergesch'), ('lt', 'Lietuvi\u0161kai'), ('lv', 'latvie\u0161'), ('mk', '\u041c\u0430\u043a\u0435\u0434\u043e\u043d\u0441\u043a\u0438'), ('ml', 'Malayalam'), ('mn', 'Mongolian'), ('mr', '\u092e\u0930\u093e\u0920\u0940'), ('my', '\u1019\u103c\u1014\u103a\u1019\u102c\u1018\u102c\u101e\u102c'), ('nb', 'norsk (bokm\xe5l)'), ('ne', '\u0928\u0947\u092a\u093e\u0932\u0940'), ('nl', 'Nederlands'), ('nn', 'norsk (nynorsk)'), ('os', '\u0418\u0440\u043e\u043d'), ('pa', 'Punjabi'), ('pl', 'polski'), ('pt', 'Portugu\xeas'), ('pt-br', 'Portugu\xeas Brasileiro'), ('ro', 'Rom\xe2n\u0103'), ('ru', '\u0420\u0443\u0441\u0441\u043a\u0438\u0439'), ('sk', 'slovensk\xfd'), ('sl', 'Sloven\u0161\u010dina'), ('sq', 'shqip'), ('sr', '\u0441\u0440\u043f\u0441\u043a\u0438'), ('sr-latn', 'srpski (latinica)'), ('sv', 'svenska'), ('sw', 'Kiswahili'), ('ta', '\u0ba4\u0bae\u0bbf\u0bb4\u0bcd'), ('te', '\u0c24\u0c46\u0c32\u0c41\u0c17\u0c41'), ('th', '\u0e20\u0e32\u0e29\u0e32\u0e44\u0e17\u0e22'), ('tr', 'T\xfcrk\xe7e'), ('tt', '\u0422\u0430\u0442\u0430\u0440\u0447\u0430'), ('udm', '\u0423\u0434\u043c\u0443\u0440\u0442'), ('uk', '\u0423\u043a\u0440\u0430\u0457\u043d\u0441\u044c\u043a\u0430'), ('ur', '\u0627\u0631\u062f\u0648'), ('vi', 'Ti\xea\u0301ng Vi\xea\u0323t'), ('zh-cn', '\u7b80\u4f53\u4e2d\u6587'), ('zh-hans', '\u7b80\u4f53\u4e2d\u6587'), ('zh-hant', '\u7e41\u9ad4\u4e2d\u6587'), ('zh-tw', '\u7e41\u9ad4\u4e2d\u6587')]),
        ),
    ]
