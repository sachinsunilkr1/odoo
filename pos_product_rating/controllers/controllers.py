# -*- coding: utf-8 -*-
# from odoo import http


# class PosProductRating(http.Controller):
#     @http.route('/pos_product_rating/pos_product_rating/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_product_rating/pos_product_rating/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_product_rating.listing', {
#             'root': '/pos_product_rating/pos_product_rating',
#             'objects': http.request.env['pos_product_rating.pos_product_rating'].search([]),
#         })

#     @http.route('/pos_product_rating/pos_product_rating/objects/<model("pos_product_rating.pos_product_rating"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_product_rating.object', {
#             'object': obj
#         })
