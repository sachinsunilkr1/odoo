# -*- coding: utf-8 -*-

from odoo import models, fields, api

#package details
class sale_package(models.Model):
    _name = 'sale_package.sale_package'
    _description = 'sale_package.sale_package'

    name = fields.Char(string="Name", required="True")
    width = fields.Float(string="Width")
    height = fields.Float(string="Height")
    length = fields.Float(string="Length")
    max_weight = fields.Float(string="Maximum Weight")



class sale_order_inherit(models.Model):
    _inherit = 'sale.order'
    package_name = fields.Many2many('sale_package.sale_package', string='Package')
    package_info = fields.Many2many('sale_package.sale_package', related="package_name", string='package info')



#bundle creation on confirm button click

    def create_bundles(self):
        order_line = []
        for order in self:
            for sale_order_line_details in order.order_line:
                if sale_order_line_details.package_name.id:
                    order_line.append(sale_order_line_details.id)
        if len(order_line) != 0:
            vals= {
                'sale_order_partner': self.partner_id.id,
                'sale_order_date': self.date_order,
                'sale_order_expected_date': self.expected_date,
                'sale_order_name': self.name,
                'sale_order_line': order_line

            }
            if self.env['package.bundle'].search([('sale_order_name', '=', self.name)]):
                self.env['package.bundle'].search([('sale_order_name', '=', self.name)]).write(vals)
            else:
                self.env['package.bundle'].sudo().create(vals)



#showing package bundle details on smart button
    def show_package_bundle(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Package Bundle',
            'view_mode': 'tree,form',
            'res_model': 'package.bundle',
            'domain': [('sale_order_name', '=', self.name)],
            'context': "{'create':False}"
        }
#write fun for overriding the confirm button action
    def write(self, vals):
        result = super(sale_order_inherit, self).write(vals)
        self.create_bundles()
        return result

class sale_order_line(models.Model):
    _inherit = 'sale.order.line'
    package_name = fields.Many2one('sale_package.sale_package', string='Package')

    width_package = fields.Float('Width', related='package_name.width')
    height_package = fields.Float('Height', related ='package_name.height')
    length_package = fields.Float('Length', related='package_name.length')
    weight_package = fields.Float('Weight', related='package_name.max_weight')
