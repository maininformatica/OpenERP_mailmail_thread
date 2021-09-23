# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, SUPERUSER_ID
## from .hooks import pre_init_hook, post_init_hook, uninstall_hook, post_load
## from .hooks import pre_init_hook
from odoo.exceptions import UserError, AccessError, ValidationError
from openerp.tools import config
from . import models
import os, fnmatch
import shutil


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


def post_load():
    mydir = config['data_dir'] 
    root_ids = find('odoo-bin', '/')
    initfile_ids = find('patch_mail_init.py', '/')
    mailfile_ids = find('patch_mail_mail.py', '/')
    threadfile_ids = find('patch_mail_thread.py', '/')
    ROOT = ""
    for initfiles in initfile_ids:
        initfile = str(initfiles)
    for mailfiles in mailfile_ids:
        mailfile = str(mailfiles)
    for threadfile in threadfile_ids:
        threadfile = str(threadfiles)
    for rootdir in root_ids:
        ROOT += str(rootdir).replace('odoo-bin','addons/mail/models/')

    source1 = str(initfile)
    destination1 = ROOT + "__init__.py"
    destination1b = ROOT + "__init__.py_BKP"

    source2 = str(mailfile)
    destination2 = ROOT + "mail_mail.py"
    destination2b = ROOT + "mail_mail.py_BKP"

    source3 = str(threadfile)
    destination3 = ROOT + "mail_thread.py"
    destination3b = ROOT + "mail_thread.py_BKP"

    ## BACKUP    
    shutil.copy(destination1, destination1b)    
    shutil.copy(destination2, destination2b)
    shutil.copy(destination3, destination3b)

    ## PATCH
    shutil.copy(source1, destination1)
    shutil.copy(source2, destination2)
    shutil.copy(source3, destination3)
    