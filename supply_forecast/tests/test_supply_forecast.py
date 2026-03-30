from odoo.tests.common import TransactionCase

class TestSupplyForecast(TransactionCase):
    def setUp(self):
        super(TestSupplyForecast, self).setUp()
        self.SupplyForecast = self.env['supply.forecast']

    def test_forecast_creation(self):
        """Test if a forecast can be created."""
        product = self.env['product.product'].create({
            'name': 'Test Product',
            'type': 'product'
        })
        forecast = self.SupplyForecast.create({
            'product_id': product.id,
            'date_start': '2026-01-01',
            'date_end': '2026-01-31',
            'forecast_qty': 100.0,
        })
        self.assertEqual(forecast.state, 'draft')
        self.assertEqual(forecast.product_id.id, product.id)
