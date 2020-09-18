# -*- coding: utf-8 -*-
#############################################################################


from odoo import api, models, fields


class FieldAccountMove(models.Model):
    _inherit = 'account.move'

    original = fields.Integer(help="Campo para verificar script de migración", string="Original")     


class FieldAccountMoveLine(models.Model):
    _inherit =  'account.move.line'

    original = fields.Integer(help="Campo para verificar script de migración", string="Original Linea")

class PartnerOriginal(models.Model):
	_inherit = 'res.partner'

	original = fields.Integer(string="Original")
