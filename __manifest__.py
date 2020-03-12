# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'CRM Survey',
    'version': '1.0',
    'category': 'Sales/CRM',
    'sequence': 5,
    'summary': 'Link Survey with CRM',
    'description': "",
    'website': 'https://www.odoo.com/page/crm',
    'depends': [
        'crm',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_survey.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
