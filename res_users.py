from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    # Añadir campos personalizados si es necesario
    minimal_field = fields.Char(string="Minimal Field")
