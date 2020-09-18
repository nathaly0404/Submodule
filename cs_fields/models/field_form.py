# -*- coding: utf-8 -*-
#############################################################################


from odoo import api, models


class FieldAccountMove(models.Model):
    _inherit = 'account.move'

    original = fields.Integer(help="Campo para verificar script de migración", string="Original")     


class FieldAccountMoveLine(models.Model):
    _inherit =  'account.move.line'

    original_linea = fields.Integer(help="Campo para verificar script de migración", string="Original Linea")
    
