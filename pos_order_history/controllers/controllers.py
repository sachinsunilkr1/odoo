# -*- coding: utf-8 -*-
# from odoo import http


# class PosOrderHistory(http.Controller):
#     @http.route('/pos_order_history/pos_order_history/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_order_history/pos_order_history/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_order_history.listing', {
#             'root': '/pos_order_history/pos_order_history',
#             'objects': http.request.env['pos_order_history.pos_order_history'].search([]),
#         })

#     @http.route('/pos_order_history/pos_order_history/objects/<model("pos_order_history.pos_order_history"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_order_history.object', {
#             'object': obj
#         })
