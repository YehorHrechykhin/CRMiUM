from odoo.tests import tagged

from .common import TestDeveloperCompanyModule


@tagged('post_install', '-at_install', 'dev_manag', 'access')
class TestDevelopersManagement(TestDeveloperCompanyModule):

    def test_unique_developer_name_constraint(self):
        # Try to create two developers with the same name
        with self.assertRaises(Exception):
            self.dev_alice
            self.Developer.create({'name': 'Alice Smith'})

    def test_unique_company_name_constraint(self):
        # Try to create two companies with the same name
        with self.assertRaises(Exception):
            self.company_developing
            self.Company.create({'name': 'Developing Inc'})

    def test_global_identification_computation(self):
        developer = self.dev_alice
        self.assertEqual(developer.global_identification, 'Alice Smith-front-end')

    def test_out_stuff_developer_phone_constraint(self):
        developer = self.dev_bob
        self.assertFalse(developer.phone)

    def test_company_developer_relationship(self):
        company = self.company_developing
        developer1 = self.dev_cindy
        developer2 = self.dev_david

        self.assertIn(developer1, company.developer_ids)
        self.assertIn(developer2, company.developer_ids)
        self.assertEqual(len(company.developer_ids), 2)
