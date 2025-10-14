from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    partner_name = fields.Char(related='partner_id.name', string="Customer Name")
