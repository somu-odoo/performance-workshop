def generate_invoices(self):
    for order in self.search([('state', '=', 'done')]):
        if order.amount_total > 500:
            invoices_count = self.env['account.move'].search_count([('invoice_origin', '=', order.name)])
            if invoices_count == 0:
                self.env['account.move'].create({
                    'partner_id': order.partner_id.id,
                    'invoice_origin': order.name,
                    'move_type': 'out_invoice',
                    'invoice_line_ids': [
                        (0, 0, {'product_id': line.product_id.id, 'quantity': line.product_uom_qty})
                        for line in order.order_line
                    ],
                })