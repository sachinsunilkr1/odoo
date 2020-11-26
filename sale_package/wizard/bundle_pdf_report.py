# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError

#python class for wizard

class bundle_report(models.TransientModel):
    _name = 'bundle.report'
    date_from = fields.Date(string="Date From")
    date_to = fields.Date(string="Date To")
    sale_person = fields.Many2one('res.partner', string="Salesman")

#Print PDF Report Function
    def print_report(self):
        #condition 1
        if self.date_from and self.date_to and self.sale_person:
            self.env.cr.execute("""SELECT sequence_no 
            FROM package_bundle
            WHERE Cast(sale_order_date AS date) >= %s 
            AND Cast(sale_order_date AS date) <= %s
            AND sale_order_partner = %s """,
                               (self.date_from, self.date_to,self.sale_person.id))
            sequence_data = self.env.cr.dictfetchall()
            return self.print_report_data(sequence_data)
        elif self.date_from and self.date_to:
            self.env.cr.execute("""SELECT sequence_no 
                        FROM package_bundle
                        WHERE Cast(sale_order_date AS date) >= %s 
                        AND Cast(sale_order_date AS date) <= %s""",
                                (self.date_from, self.date_to))
            sequence_data = self.env.cr.dictfetchall()
            print('condition2')
            return self.print_report_data(sequence_data)

        elif self.date_from:
            self.env.cr.execute("""SELECT sequence_no 
            FROM package_bundle
            WHERE Cast(sale_order_date AS date) >= %s """,(self.date_from,))
            sequence_data = self.env.cr.dictfetchall()
            print('condition3')
            return self.print_report_data(sequence_data)

        elif self.sale_person:
            self.env.cr.execute("""SELECT sequence_no 
            FROM package_bundle
            WHERE sale_order_partner = %s """,(self.sale_person.id,))
            sequence_data = self.env.cr.dictfetchall()
            print('condition4')
            return self.print_report_data(sequence_data)
        else:
            raise UserError("Enter Valid Data")




    def print_report_data(self,sequence_data):
        raw = []
        for seq_no in sequence_data:
            sequence = [seq_no['sequence_no']]
            print('sequence_data', sequence)
            print('ids', seq_no)
            self.env.cr.execute("""SELECT a.sequence_no,b.name AS product_name,b.product_uom_qty,b.order_id,c.name AS package_name,
                                    c.width,c.height,c.max_weight 
                                    FROM sale_order_line b LEFT JOIN package_bundle_sale_order_line_rel d 
                                    ON d.sale_order_line_id = b.id LEFT JOIN package_bundle a
                                    ON d.package_bundle_id = a.id LEFT JOIN sale_package_sale_package c
                                    ON c.id = b.package_name
                                    WHERE a.sequence_no IS NOT NULL
                                    AND a.sequence_no = %s """, sequence)
            bundle_data = self.env.cr.dictfetchall()
            print('bundle_data', bundle_data)
            value = []

            for pack in bundle_data:
                value.append({
                    'sequence_no': pack['sequence_no'],
                    'product': pack['product_name'],
                    'quantity': pack['product_uom_qty'],
                    'package_name': pack['package_name'],
                    'package_width': pack['width'],
                    'package_height': pack['height'],
                    'package_weight': pack['max_weight'],
                })
                print('value', value)
            raw.append({
                'seq': seq_no['sequence_no'],
                'value': value
                })

        data = {
            'ids': self.ids,
            'model': 'bundle.report',
            'vals': raw,
            'date_from': self.date_from,
            'date_to': self.date_to,
            'sale_person': self.sale_person.name
        }
        return self.env.ref('sale_package.report_bundle').report_action(self, data=data)
#('sale_package.report_bundle')=module_name.report_id in the xml file

#Excel report functions

    def print_report_xls(self):
        if self.date_from and self.date_to and self.sale_person:
            self.env.cr.execute("""SELECT sequence_no 
            FROM package_bundle
            WHERE Cast(sale_order_date AS date) >= %s 
            AND Cast(sale_order_date AS date) <= %s
            AND sale_order_partner = %s """,
                               (self.date_from, self.date_to,self.sale_person.id))
            sequence_data = self.env.cr.dictfetchall()
            return self.excel_report_data(sequence_data)
        elif self.date_from and self.date_to:
            self.env.cr.execute("""SELECT sequence_no 
                        FROM package_bundle
                        WHERE Cast(sale_order_date AS date) >= %s 
                        AND Cast(sale_order_date AS date) <= %s""",
                                (self.date_from, self.date_to))
            sequence_data = self.env.cr.dictfetchall()
            print('condition2')
            return self.excel_report_data(sequence_data)

        elif self.date_from:
            self.env.cr.execute("""SELECT sequence_no 
            FROM package_bundle
            WHERE Cast(sale_order_date AS date) >= %s """,(self.date_from,))
            sequence_data = self.env.cr.dictfetchall()
            print('condition3')
            return self.excel_report_data(sequence_data)

        elif self.sale_person:
            self.env.cr.execute("""SELECT sequence_no 
            FROM package_bundle
            WHERE sale_order_partner = %s """,(self.sale_person.id,))
            sequence_data = self.env.cr.dictfetchall()
            print('condition4')
            return self.excel_report_data(sequence_data)

        else:
            raise UserError("Enter Valid Data")

    def excel_report_data(self, sequence_data):
        if sequence_data:
            doc = {
                'ids': self.ids,
                'model': 'bundle.report',
                'date_from': self.date_from,
                'date_to': self.date_to,
                'sale_person': self.sale_person.name,
                'sale_person_id' : self.sale_person.id
            }
        print('doc', doc)
        return self.env.ref('sale_package.excel_report_bundle').report_action(self, doc)



