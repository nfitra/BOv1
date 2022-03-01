# -*- coding: utf-8 -*-
{
    'name': "Booking Order Your Name",
    'summary': "Booking Order Your Name",
    'description': "Booking Order Your Name",

    'author': "Hashmicro",
    'website': "http://www.hashmicro.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.0',

    # any module necessary for this one to work correctly
    'depends': [
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/model_name_views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
