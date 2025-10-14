from odoo import fields, models

class Session(models.Model):
    _name = 'openacademy.session'
    _order = 'course_id, instructor_id, id'
    
    name = fields.Char()
    course_id = fields.Many2one('openacademy.course')
    instructor_id = fields.Many2one('res.partner')

