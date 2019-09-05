from odoo import models, fields, api


class Activity(models.Model):
    _name = 'activity'
    _description = 'Activity'

    activity = fields.Char(string='Activity')