def run_update_script(self):
    self.env['sale.order'].search([('state', '=', 'draft')]).write({'state': 'sent'})
    
    self.env.cr.execute("""
        UPDATE sale_order
        SET state = 'done'
        WHERE date_order < NOW() - INTERVAL '30 days'
    """)
    
    orders = self.env['sale.order'].search([('state', '=', 'done')])
    print(f"Number of 'done' orders found: {len(orders)}")