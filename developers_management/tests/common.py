from odoo.tests.common import TransactionCase


class TestDeveloperCompanyModule(TransactionCase):

    def setUp(self):
        super(TestDeveloperCompanyModule, self).setUp()
        self.Developer = self.env['developer']
        self.Company = self.env['company']

        # Create sample developers
        self.dev_alice = self.Developer.create({
            'name': 'Alice Smith',
            'type': 'front-end',
        })

        self.dev_bob = self.Developer.create({
            'name': 'Bob Johnson',
            'type': 'out-stuff',
            'phone': '123456',
        })

        # Create sample company
        self.company_developing = self.Company.create({
            'name': 'Developing Inc',
        })

        # Associate developers with the company
        self.dev_cindy = self.Developer.create({
            'name': 'Cindy Brown',
            'type': 'backend',
            'company_id': self.company_developing.id,
        })

        self.dev_david = self.Developer.create({
            'name': 'David Green',
            'type': 'fullstack',
            'company_id': self.company_developing.id,
        })
