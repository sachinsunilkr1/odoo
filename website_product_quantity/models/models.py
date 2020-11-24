# -*- coding: utf-8 -*-

# from odoo import models, fields, api
#
#
# class website_product_quantity(models.Model):
#     _inherit = "sale.order"
#     _name = 'website_product_quantity.website_product_quantity'
#     _description = 'website_product_quantity.website_product_quantity'
#
#     website_product_quantity = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
