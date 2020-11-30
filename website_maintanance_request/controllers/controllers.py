from odoo import http
from odoo.http import request
# from werkzeug.utils import redirect


class MaintenanceForm(http.Controller):

    @http.route(['/maintenance'], type='http', auth="public", website=True)
    def maintenance_form(self, **post):
        maintenance_requests = request.env['maintenance.equipment'].sudo().search([])
        maintenance_team = request.env['maintenance.team'].sudo().search([])
        user = request.env.user.id
        print('user_data',user)
        employee = request.env['hr.employee'].sudo().search([('user_id', '=', user)])
        print('employee_data',employee)
        dict = []
        team = []
        for record in maintenance_requests:
            name = record.name
            dict.append({'id': record.id, 'name': name})
        for record in maintenance_team:
            name = record.name
            team.append({'id': record.id, 'name': name})
        # if employee:
        return http.request.render("website_maintanance_request.maintenance_form", {
                'equipment_selection': dict,
                'team_selection': team,
        })
        # return request.render("website_maintanance_request.maintenance_form", {})

    @http.route(['/maintenance/form'], type='http', auth="public", website=True)
    def maintenance_form_submit(self, **post):
        user = request.env.user.id
        employee = request.env['hr.employee'].sudo().search([('user_id', '=', user)])
        print(user)
        if employee:
            values = {
                'name': post['subject'],
                'maintenance_team_id': int(post['teams']),
                'equipment_id': int(post['equipment']),
                'description': post['details'],
                'priority': post['stars'],
                'employee_id': employee.id

            }
            print("values", values)
            # requests = super(MaintenanceRequest, self).create(vals)
            request_id = request.env['maintenance.request'].sudo().create(values)

        return request.render("website_maintanance_request.maintenance_form_success")










