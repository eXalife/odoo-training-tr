from odoo import models, fields, api


class ActivityPlace(models.Model):
    _name = 'activity.place'
    _description = 'Activity Place'

    place = fields.Char(string='Place')
    activity = fields.One2many(related='activity')