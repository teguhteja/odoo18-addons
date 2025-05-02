# -*- coding: utf-8 -*-
{
    'name': "Web Systray",

    'summary': "Example Web Systray Module",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','web','sale_management','purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'assets': { 
        'web.assets_backend': [ 
            'ttm_web_systray/static/src/components/systray_dropdown.js', 
            'ttm_web_systray/static/src/components/systray_dropdown.xml', 
            ],
        },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

