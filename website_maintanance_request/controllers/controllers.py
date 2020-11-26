from odoo import http
from odoo.http import request
class PartnerForm(http.Controller):

    @http.route(['/maintanance/form'], type='http', auth="public", website=True)
    #mention a url for redirection.

    def partner_form(self, **post):
    #create method
    #this will load the form webpage
        return request.render("website_maintanance_request.tmp_customer_form", {})
    @http.route(['/maintanance/form/submit'], type='http', auth="public", website=True)
    #next controller with url for submitting data from the form#
    def customer_form_submit(self, **post):
        partner = request.env['res.partner'].create({
            'name': post.get('name'),
            'email': post.get('email'),
            'phone': post.get('phone')
        })
        vals = {
            'partner': partner,
        }
        #inherited the model to pass the values to the model from the form#
        return request.render("website_maintanance_request.tmp_customer_form_success", vals)
        #finally send a request to render the thank you page#