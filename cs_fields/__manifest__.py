# -*- coding: utf-8 -*-
#############################################################################
{
    'name': 'Agrega Campo Original',
    'version': '13.0.1.2.0',
    'summary': 'Agrega Campo Original a modelos de account. move y account.move.line',
    'category': 'Contabilidad',
    'author': 'Quilsoft',
    'maintainer': 'Quilsoft',
    'company': 'Quilsoft',
    'depends': ['accunt.move', 'account.move.line'],
    'data': [
        'views/fields_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
