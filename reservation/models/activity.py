from odoo import models, fields, api


class Activity(models.Model):
    _name = 'activity'
    _description = 'Activity'
    _rec_name = 'activity'

    activity = fields.Char(string='Activity')