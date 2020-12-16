# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class pos_order_history(models.Model):
#     _name = 'pos_order_history.pos_order_history'
#     _description = 'pos_order_history.pos_order_history'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
