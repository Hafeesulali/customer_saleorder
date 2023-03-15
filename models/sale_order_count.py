from odoo import models, fields, api


class SaleOrderCount(models.Model):
    _inherit = "product.template"

    sale_count = fields.Integer(compute='_compute_count')

    def _compute_count(self):
        for record in self:
            record.sale_count = self.env['sale.order'].search_count(
                [('order_line.product_template_id.id', '=', self.id)])

    @api.constrains("list_price")
    def change_list_price(self):
        sale = self.env['sale.order.line'].search([('order_id.state', '=', 'draft')])
        for record in sale:
            if record.product_template_id.id == self.id:
                print("hi")
                record.price_unit = self.list_price
