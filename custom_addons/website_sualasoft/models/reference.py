from odoo import models, fields

class SualasoftContact(models.Model):
    _name = 'sualasoft.contact'
    _description = 'Sualasoft Contact Form Submission'
    _order = 'created_date desc'

    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    email = fields.Char(string='Email', required=True)
    phone = fields.Char(string='Phone', required=True)
    message = fields.Text(string='Message', required=True)
    
    project_type = fields.Selection([
        ('mobile', 'Mobile Development'),
        ('web', 'Web Development'),
        ('odoo', 'Odoo Integration'),
        ('infrastructure', 'Infrastructure SI'),
        ('other', 'Other'),
    ], string='Project Type', required=True)
    
    created_date = fields.Datetime(string='Created Date', default=fields.Datetime.now)
    processed = fields.Boolean(string='Processed', default=False)
    industry = fields.Char(string="Secteur d'activité")


class SualasoftReference(models.Model):
    _name = 'sualasoft.reference'
    _description = 'Sualasoft Reference / Portfolio'
    _order = 'sequence, name'

    name = fields.Char(string='Client Name', required=True)
    description = fields.Text(string='Description')
    industry = fields.Char(string='Industry', help='Client industry sector')
    
    service_ids = fields.Many2many(
        'sualasoft.service',
        'reference_service_rel',
        'reference_id',
        'service_id',
        string='Services'
    )
    
    technologies = fields.Char(string='Technologies', help='Stack technique utilisée')
    website = fields.Char(string='Client Website URL')
    
    featured = fields.Boolean(string='Featured', default=False)
    sequence = fields.Integer(string='Sequence', default=10)
    
    active = fields.Boolean(default=True)
    created_date = fields.Datetime(string='Date Created', default=fields.Datetime.now)

    def action_toggle_featured(self):
        self.featured = not self.featured
        return True


class SualasoftService(models.Model):
    _name = 'sualasoft.service'
    _description = 'Sualasoft Service Type'
    _order = 'name'

    name = fields.Char(string='Service Name', required=True)
    code = fields.Char(string='Code', required=True)
    description = fields.Text(string='Description')
    color = fields.Integer(string='Color Index')
    
    _sql_constraints = [
        ('code_unique', 'unique(code)', 'Le code du service doit être unique'),
    ]
