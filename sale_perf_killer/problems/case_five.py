class MyModel(models.Model):
    _name = 'my.model'
    _parent_name = 'parent_id'
    
    name = fields.Char()
    parent_id = fields.Many2one('my.model')

    total_sub_items = fields.Integer(compute='_compute_total_sub_items', string="Total Sub-Items", store=False)
    
    def _compute_total_sub_items(self):
        for rec in self:
            count = 0
            if rec.child_ids:
                count = len(rec.child_ids) + sum(child.total_sub_items for child in rec.child_ids)
            rec.total_sub_items = count
