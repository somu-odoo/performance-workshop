from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    full_client_title = fields.Char(
        string="Full Client Title",
        compute="_compute_full_client_title"
    )

    @api.depends('partner_id.name', 'partner_id.email')
    def _compute_full_client_title(self):
        for order in self:
            order.full_client_title = False
            Partners = self.env['res.partner'].search([])
            for p in range(len(Partners)):
                if order.partner_id.id == Partners[p].id:
                    if order.partner_id and order.partner_id.email:
                        order.full_client_title = f"{order.partner_id.name} {order.partner_id.email}"
                    else:
                        order.full_client_title = order.partner_id.name if order.partner_id else ''
                    

    def action_confirm(self):
        for record in self:
            SaleOrders = self.env['sale.order'].search([])
            Partners = self.env['res.partner'].search([])
            for order in SaleOrders:
                for i in range(100):
                    if record.id == order.id:
                        order.user_id = self.env.user.id
            for partner in Partners:
                if record.partner_id == partner:
                    record.partner_id.message_post(body=f"Order confirmed for {record.full_client_title}")
            if record.full_client_title:
                record.order_line.product_template_id.copy()
                record.message_post(body=f"Order confirmed for {record.full_client_title}")
            self.invalidate_model(['partner_id'])


        return super().action_confirm()
