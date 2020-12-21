# -*- coding: utf-8 -*-
# from odoo import http


# class PaytrailPaymentGateway(http.Controller):
#     @http.route('/paytrail_payment_gateway/paytrail_payment_gateway/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/paytrail_payment_gateway/paytrail_payment_gateway/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('paytrail_payment_gateway.listing', {
#             'root': '/paytrail_payment_gateway/paytrail_payment_gateway',
#             'objects': http.request.env['paytrail_payment_gateway.paytrail_payment_gateway'].search([]),
#         })

#     @http.route('/paytrail_payment_gateway/paytrail_payment_gateway/objects/<model("paytrail_payment_gateway.paytrail_payment_gateway"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('paytrail_payment_gateway.object', {
#             'object': obj
#         })
