# -*- coding: utf-8 -*-

from odoo import models, fields


class UomCategory(models.Model):
    _inherit = 'uom.category'

    active = fields.Boolean(string='Active', default=True)

    def write(self, vals):
        res = super(UomCategory, self).write(vals)
        if 'active' in vals:
            self.env['uom.uom'].search([('active', 'in', [True, False]), ('category_id', 'in', self.ids)]).write(
                {'active': vals['active']})
        return res
