from odoo import models, fields, api
from odoo.exceptions import ValidationError


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
        reservations = self.env['reservation'].search([('activity_place_id', '=', self.activity_place_id.id), ('active', '=', True)])
        for reservation in reservations:
            if (reservation.start_date < self.start_date and reservation.finish_date > self.start_date) or (reservation.start_date < self.finish_date and reservation.finish_date > self.finish_date):
                raise ValidationError('reserva no disponible')



    # @api.model
    # def create(self, vals):
    #     if vals.get('name', _('New')) == _('New'):
    #         vals['name'] = self.env['ir.sequence'].next_by_code('stock.landed.cost')
    #     return super(Reservation, self).create(vals)

# @api.multi
# 	def action_refuse(self):
# 		current_employee = self.env['hr.employee'].search([('user_id', '=', self.env.uid)], limit=1)
# 		for i in self:
#
# 				i.write({'state': 'refuse', 'second_approver_id': current_employee.id})
# #	Eğer şu anki state validate1 ise state'i refuse olarak değiştirilir.
# 		return True

# values['attendee_ids'] = self.env['event.registration'].search([('sale_order_line_id', '=', line.id), ('state', '!=', 'cancel')]).ids