# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    _inherit = "product.template"

    height = fields.Float(string='Height')
    height_uom_id = fields.Many2one('uom.uom', string="Height Unit of Measure",
                                    default=lambda self: self.env.ref('uom.product_uom_millimeter'))
    width = fields.Float(string='Width')
    width_uom_id = fields.Many2one('uom.uom', string="Width unit of Measure",
                                   default=lambda self: self.env.ref('uom.product_uom_millimeter'))
    thickness = fields.Float(string='Thickness')
    thickness_uom_id = fields.Many2one('uom.uom', string="Thickness Unit of Measure",
                                       default=lambda self: self.env.ref('uom.product_uom_millimeter'))