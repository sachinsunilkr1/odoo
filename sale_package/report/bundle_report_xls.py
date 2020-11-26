from odoo import models
from odoo.exceptions import UserError

#template for package bundle report excel
class BundleReportXlsx(models.AbstractModel):
    _name = 'report.sale_package.bundle_report_xls'
    _inherit = 'report.odoo_report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        format1 = workbook.add_format({'font_size': 9, 'valign': 'vcenter',
                                       'align': 'center', 'bold': True, 'bg_color': '#CCCCCC'})
        sequence_format = workbook.add_format({'font_size': 9, 'align': 'vcenter',
                                   'bold': True, 'bg_color': '#EEEEEE'})
        wizard_data = workbook.add_format({'font_size': 8, 'align': 'vcenter', 'bold': True, })
        heading = workbook.add_format({'font_size': 13, 'valign': 'vcenter',
                                       'align': 'center', 'bold': 2,
                                       'underline': True, })
        format2 = workbook.add_format({'font_size': 8, 'valign': 'vcenter', 'text_wrap': True})
        company = workbook.add_format({'font_size': 8, 'align': 'vcenter', 'bg_color': '#EEEEEE'})
        sheet = workbook.add_worksheet('Package Bundle Report')

        sheet.set_column(3, 3, 50)
        sheet.set_column(2, 2, 15)
        sheet.set_column(4, 4, 12)
        sheet.set_column(5, 5, 12)
        sheet.set_column(6, 6, 12)
        sheet.set_column(7, 7, 12)
        sheet.set_column(8, 8, 12)
        sheet.set_row(10, 25)

        if data['date_from'] and data['date_to'] and data['sale_person_id']:
            sheet.write(5, 3, 'Package Bundle Report', heading)
            sheet.write(6, 1, 'date_from:', wizard_data)
            sheet.write(7, 1, 'date_to:', wizard_data)
            sheet.write(8, 1, 'Partner:', wizard_data)
            sheet.write(6, 2, data['date_from'], wizard_data)
            sheet.write(7, 2, data['date_to'], wizard_data)
            sheet.write(8, 2, data['sale_person'], wizard_data)
        elif data['sale_person_id']:
            sheet.write(6, 3, 'Package Bundle Report', heading)
            sheet.write(8, 1, 'Partner:', wizard_data)
            sheet.write(8, 2, data['sale_person'], wizard_data)

        elif data['date_from'] and data['date_to']:
            sheet.write(6, 3, 'Package Bundle Report', heading)
            sheet.write(7, 1, ' date_from:', wizard_data)
            sheet.write(8, 1, 'date_to:', wizard_data)
            sheet.write(7, 2, data['date_from'], wizard_data)
            sheet.write(8, 2, data['date_to'], wizard_data)

        else:
            sheet.write(7, 3, 'Package Bundle Report', heading)

        sheet.write(10, 1, 'Sl.No', format1)
        sheet.write(10, 2, 'Package Name', format1)
        sheet.write(10, 3, 'Product Name', format1)
        sheet.write(10, 4, 'Quantity', format1)
        sheet.write(10, 5, 'Package Width', format1)
        sheet.write(10, 6, 'Package height', format1)
        sheet.write(10, 7, 'Package weight', format1)

        def bundle_report(bundle):
            sl_no = 1
            count = 11
            for dat in bundle:
                rows = (dat['sequence_no'])
                sheet.write(count, 1, sl_no, sequence_format)
                sheet.merge_range(count, 2, count, 7, rows, sequence_format)
                count = count + 1
                sl_no = sl_no + 1
                self.env.cr.execute("""SELECT a.sequence_no,b.name AS product_name,b.product_uom_qty,b.order_id,c.name AS package_name,
                                    c.width,c.height,c.max_weight 
                                    FROM sale_order_line b LEFT JOIN package_bundle_sale_order_line_rel d 
                                    ON d.sale_order_line_id = b.id LEFT JOIN package_bundle a
                                    ON d.package_bundle_id = a.id LEFT JOIN sale_package_sale_package c
                                    ON c.id = b.package_name
                                    WHERE a.sequence_no IS NOT NULL
                                    AND a.sequence_no = %s """,
                                    ([rows]))
                details = self.env.cr.dictfetchall()
                sl1 = sl_no - 1
                sl2 = sl1 + 0.1
                for dats in details:
                    sheet.write(count, 1, sl2, format2)
                    sheet.write(count, 2, dats['package_name'], format2)
                    sheet.write(count, 3, dats['product_name'], format2)
                    sheet.write(count, 4, dats['product_uom_qty'], format2)
                    sheet.write(count, 5, dats['width'], format2)
                    sheet.write(count, 6, dats['height'], format2)
                    sheet.write(count, 7, dats['max_weight'], format2)
                    count = count + 1
                    sl2 = sl2 + 0.1

        if data['date_from'] and data['date_to'] and data['sale_person_id']:
            temp = (data['sale_person_id'])
            date_from = (data['date_from'])
            date_to = (data['date_to'])
            self.env.cr.execute("""SELECT sequence_no 
                                    FROM package_bundle
                                    WHERE Cast(sale_order_date AS date) >= %s 
                                    AND Cast(sale_order_date AS date) <= %s
                                    AND sale_order_partner = %s """, (date_from, date_to, temp))
            bundle = self.env.cr.dictfetchall()
            return bundle_report(bundle)
        elif data['date_from'] and data['date_to']:
            date_from = (data['date_from'])
            date_to = (data['date_to'])
            self.env.cr.execute("""SELECT sequence_no 
                                    FROM package_bundle
                                    WHERE Cast(sale_order_date AS date) >= %s 
                                    AND Cast(sale_order_date AS date) <= %s""", (date_from, date_to))
            bundles = self.env.cr.dictfetchall()
            return bundle_report(bundles)
        elif data['sale_person_id']:
            temp = (data['sale_person_id'])
            self.env.cr.execute("""SELECT sequence_no 
                                    FROM package_bundle
                                    WHERE sale_order_partner = %s """, ([temp]))
            bundles = self.env.cr.dictfetchall()
            return bundle_report(bundles)


        else:
            raise UserError("Enter Required Input")










