from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta


class Reservation(models.Model):
    _name = 'reservation'
    _description = 'Reservation'

    activity_place_id = fields.One2many(related = 'activity.place')
    employee_id = fields.One2many(related = 'hr.employee')
    start_date = fields.Date(string='Start Date')
    start_date2 = fields.DateTime(string='Start Date2') # deneme
    finish_date = fields.Date(string='Finish Date')
    active = fields.Boolean(string = 'Active')