from odoo.tests import common

class TestSupplyForecast(common.TransactionCase):

    def setUp(self):
        super(TestSupplyForecast, self).setUp()
        self.product_template = self.env['product.template'].create({
            'name': 'Test Product',
            'type': 'consu',
        })
        self.product = self.product_template.product_variant_id

    def test_forecast_creation(self):
        """ Test basic forecast creation """
        forecast = self.env['supply.forecast'].create({
            'product_id': self.product.id,
            'date_start': '2026-04-01',
            'date_end': '2026-04-30',
            'forecast_qty': 100.0,
        })
        self.assertEqual(forecast.state, 'draft')
        self.assertEqual(forecast.forecast_qty, 100.0)
