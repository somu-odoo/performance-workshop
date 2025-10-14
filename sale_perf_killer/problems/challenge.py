from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    total_sales_count = fields.Integer(compute='_compute_total_sales_count', store=True, string="Total Sales Count")
    last_sale_date = fields.Date(compute='_compute_last_sale_date', store=True, string="Last Sale Date")
    first_purchase_date = fields.Date(compute='_compute_first_purchase_date', store=True, string="First Purchase Date")
    
    current_sale_value = fields.Float(compute='_compute_current_sale_value', string="Current Sale Value")

    @api.depends('sale_order_ids.state', 'sale_order_ids.amount_total')
    def _compute_total_sales_count(self):
        for rec in self:
            rec.total_sales_count = len(rec.sale_order_ids.filtered(lambda r: r.state == 'done'))

    @api.depends('sale_order_ids')
    def _compute_last_sale_date(self):
        for rec in self:
            if rec.sale_order_ids:
                rec.last_sale_date = max(rec.sale_order_ids.mapped('date_order'))
            else:
                rec.last_sale_date = False

    @api.depends('sale_order_ids.date_order')
    def _compute_first_purchase_date(self):
        for rec in self:
            if rec.sale_order_ids:
                rec.first_purchase_date = min(rec.sale_order_ids.mapped('date_order'))
            else:
                rec.first_purchase_date = False

    @api.depends('last_sale_date', 'first_purchase_date')
    def _compute_current_sale_value(self):
        for rec in self:
            # The complex logic...
            rec.current_sale_value = rec.total_sales_count * 100 + (rec.last_sale_date and 1 or 0) + (rec.first_purchase_date and 1 or 0)
