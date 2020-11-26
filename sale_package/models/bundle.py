from odoo import models, fields, api


# sequence no generation


class bundle(models.Model):
    _name = 'package.bundle'
    _rec_name = 'sequence_no'

    sequence_no = fields.Char(string="Bundle Number", required=True, readonly=True, copy=False, default='New')
    sale_order_name = fields.Char(string="Order Number", readonly=True)
    sale_order_date = fields.Datetime(string="Order Date")
    sale_order_expected_date = fields.Datetime(string="Expected Date")
    sale_order_partner = fields.Many2one('res.partner', string="Customer")
    sale_person = fields.Char(string="Sales Person")
    sale_order_line = fields.Many2many('sale.order.line')

    @api.model
    def create(self, values):
        if values.get('sequence_no', 'New') == 'New':
            values['sequence_no'] = self.env['ir.sequence'].next_by_code(
                'package.bundle') or 'New'
        result = super(bundle, self).create(values)
        return result