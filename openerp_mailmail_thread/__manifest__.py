# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'OpenERP - Mail Thread on Mail',
    'version': '1.3',
    'category': 'Tools',
    'summary': 'Allow Mail Thread on Mail',
    'description': ['static/description/index.html'],
    'author': "MAIN INFORMATICA GANDIA SL",
    'website': "http://www.main-informatica.com",
    'depends': ['mail'],
    'installable': True,
    'application': False,
    'auto_install': True,
    'post_load': 'post_load',
    'images': ['static/description/openerp_mailmail_thread.png'],
}
