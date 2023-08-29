from odoo import models, fields


class Company(models.Model):
    _name = 'company'
    _description = 'Company Information'

    name = fields.Char(required=True)
    address = fields.Text()
    developer_ids = fields.One2many(
        comodel_name='developer',
        inverse_name='company_id',
        string='Developers',
    )

    # SQL constraint to ensure unique names for companies
    _sql_constraints = [('company_uniq',
                         'UNIQUE (name)',
                         'Name of company must be unique!')]
