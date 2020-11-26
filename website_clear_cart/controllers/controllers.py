from odoo import http
from odoo.http import request


class ClearCart(http.Controller):
    @http.route(["/shop/clear_cart"], type="json", auth="public", website=True)
    def clear_cart(self):
        order = request.website.sale_get_order()
        if order:
            for i in order.website_order_line:
                i.unlink()