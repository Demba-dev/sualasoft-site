from odoo import models, fields

class SualasoftReference(models.Model):
    _name = "sualasoft.reference"
    _description = "Reference / Portfolio"

    name = fields.Char(required=True)
    sector = fields.Char()
    services = fields.Char()
    description = fields.Text()
    image_id = fields.Binary()
    reference_type = fields.Selection([('mobile','Mobile'),('web','Web'),('odoo','Odoo'),('infra','Infra')])
    service_ids = fields.Many2many('sualasoft.service', string="Services liés")
    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)

