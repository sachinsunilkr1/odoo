# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductRating(models.Model):
    _inherit = 'product.template'

    product_ratings = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'), ], string="Product Rating", help="Rate the Product out Of 5", default='5')