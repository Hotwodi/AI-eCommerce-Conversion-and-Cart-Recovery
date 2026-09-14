{
    'name': 'AI eCommerce Conversion & Cart Recovery',
    'version': '18.0.1.0.0',
    'images': ['static/description/cover.png'],
    'category': 'Productivity/AI',
    'summary': 'AI-powered cart recovery and conversion optimization for eCommerce',
    'description': """
AI eCommerce Conversion & Cart Recovery
========================================

Recover abandoned carts and boost conversion rates with AI-driven insights:
- Abandoned cart tracking with AI recovery probability scoring
- Conversion funnel analytics with AI drop-off detection
- AI product recommendations (cross-sell, up-sell, personalized)
- Cart recovery email templates with automated scheduling
- Conversion insights with AI-powered recommendations

    """,
    'author': 'SoftaiDev',
    'website': 'https://softaidev.pages.dev',
    'license': 'LGPL-3',
    'price': 79.99,
    'currency': 'USD',
    'depends': ['base', 'web', 'mail'],
    'application': True,
    'installable': True,
    'data': [
        'security/ir.model.access.csv',
        'views/abandoned_cart_views.xml',
        'views/conversion_funnel_views.xml',
        'views/product_recommendation_views.xml',
        'views/cart_recovery_template_views.xml',
        'views/conversion_insight_views.xml',
        'views/menu.xml',
    ],
}
