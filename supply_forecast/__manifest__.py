{
    'name': 'AI Supply Chain Optimizer (Vertex AI)',
    'version': '19.0.1.0.0',
    'category': 'Inventory/Inventory',
    'images': ['static/description/banner.png'],
    'summary': 'Enterprise-grade demand forecasting and inventory optimization powered by Vertex AI (TimesFM)',
    'description': """
AI Supply Chain Optimizer
=========================
Advanced demand forecasting and inventory optimization for Odoo 19.

Key Features:
-------------
* **AI Demand Forecasting**: Powered by Google Vertex AI (TimesFM Zero-Shot model).
* **Statistical Safety Stock**: Dynamic calculation based on service levels (90%, 95%, 99%).
* **Lead Time Integration**: Automatic synchronization with supplier delivery times.
* **360° Data Vision**: Analyzes sales, production consumption, and stock moves.
* **Explainable AI (XAI)**: Human-readable rationale for every stock recommendation.
* **Proactive Monitoring**: Real-time alerts for Overstock and Obsolescence.
* **Multi-company & Multi-warehouse support**.
    """,
    'author': 'TMFCoders SL',
    'website': 'https://tmfcoders.com',
    'price': 199.00,
    'currency': 'EUR',
    'license': 'OPL-1',
    'depends': ['stock', 'sale_stock', 'purchase_stock'],
    'data': [
        'security/ir.model.access.csv',
        'security/supply_forecast_security.xml',
        'data/ir_cron_data.xml',
        'views/supply_forecast_views.xml',
        'views/menus.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'supply_forecast/static/src/components/dashboard/supply_forecast_dashboard.scss',
            'supply_forecast/static/src/components/dashboard/supply_forecast_dashboard.xml',
            'supply_forecast/static/src/components/dashboard/supply_forecast_dashboard.js',
        ],
    },
    'demo': [],
    'installable': True,
    'application': True,
}
