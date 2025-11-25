
from odoo import models, fields

class SualasoftService(models.Model):
    _name = "sualasoft.service"
    _description = "Services proposés"

    name = fields.Char(required=True)
   