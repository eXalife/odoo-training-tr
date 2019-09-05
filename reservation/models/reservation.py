from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta


class Reservation(models.Model):
    _name = 'reservation'
    _description = 'Reservation'

    activity_place_id = fields.Many2one('activity.place', required=True)
    employee_id = fields.Many2one('hr.employee', required=True)
    start_date = fields.Datetime(string='Start Date', required=True) # deneme
    finish_date = fields.Datetime(string='Finish Date', required=True)
    active = fields.Boolean(string = 'Active', default=True)

    @api.constrains('activity_place_id','start_date','finish_date')
    def _check_date(self):
        if self.entity_id and self.entity_id.is_certification_body == False:
            raise ValidationError('It is not a certification entity')


    # @api.model
    # def create(self, vals):
    #     if vals.get('name', _('New')) == _('New'):
    #         vals['name'] = self.env['ir.sequence'].next_by_code('stock.landed.cost')
    #     return super(Reservation, self).create(vals)
