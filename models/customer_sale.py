from odoo import models, fields, api


class CustomerSale(models.Model):
    _inherit = "res.partner"

    sale_order_ids = fields.One2many("sale.order", "partner_id", string="Sale Orders")
    product_count = fields.Integer(compute='_compute_count')

    def get_products(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Products',
            'view_mode': 'tree',
            'res_model': 'sale.order.line',
            'domain': [('order_id.partner_id', '=', self.id)],
            'context': "{'create': False}"
        }

    def _compute_count(self):
        for record in self:
            record.product_count = self.env['sale.order.line'].search_count([('order_id.partner_id', '=', self.id)])
