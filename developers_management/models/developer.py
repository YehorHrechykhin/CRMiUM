from odoo import models, fields, api


class Developer(models.Model):
    _name = 'developer'
    _description = 'Developer Information'

    # Selection options for developer types
    TYPE_SELECTION = [
        ('front-end', 'Front-end'),
        ('backend', 'Backend'),
        ('fullstack', 'Fullstack'),
        ('out-stuff', 'Out-stuff')
    ]

    name = fields.Char(required=True)
    type = fields.Selection(TYPE_SELECTION)
    phone = fields.Char()
    email = fields.Char()
    job_position = fields.Char()
    address = fields.Text()
    birthdate = fields.Date()
    company_id = fields.Many2one(comodel_name='company')
    global_identification = fields.Char(compute='_compute_global_identification')

    # SQL constraint to ensure unique names for developers
    _sql_constraints = [('developer_uniq',
                         'UNIQUE (name)',
                         'Name of developer must be unique!')]

    # Compute method to generate the global identification
    @api.depends('name', 'type')
    def _compute_global_identification(self):
        for developer in self:
            developer.global_identification = f"{developer.name}-{developer.type}"

    # Constraint to clear phone for 'out-stuff' type developers
    @api.constrains('type')
    def _check_phone_for_out_staff(self):
        for developer in self:
            if developer.type == 'out-stuff':
                developer.phone = False
