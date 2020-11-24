# -*- coding: utf-8 -*-
# from odoo import http


# class WebsiteProductQuantity(http.Controller):
#     @http.route('/website_product_quantity/website_product_quantity/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/website_product_quantity/website_product_quantity/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('website_product_quantity.listing', {
#             'root': '/website_product_quantity/website_product_quantity',
#             'objects': http.request.env['website_product_quantity.website_product_quantity'].search([]),
#         })

#     @http.route('/website_product_quantity/website_product_quantity/objects/<model("website_product_quantity.website_product_quantity"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('website_product_quantity.object', {
#             'object': obj
#         })
