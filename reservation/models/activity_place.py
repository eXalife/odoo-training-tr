import base64

from odoo import models, fields, api, tools


class ActivityPlace(models.Model):
    _name = 'activity.place'
    _description = 'Activity Place'
    _rec_name = 'place'

    place = fields.Char(string='Place')
    activity_id = fields.Many2one('activity')
    image = fields.Binary(string='Picture', attachment=True)

   # @api.model
    #def _default_image(self):
     #   image_path = get_module_resource('reservation', 'static/description/deneme.png', 'default_image.png')
      #  return tools.image_resize_image_big(base64.b64encode(open(image_path, 'rb').read()))