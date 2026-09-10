{
    'name': 'Sale Performance Killer',
    'version': '1.0',
    'category': 'Customisation',
    'summary': 'Faulty Module',
    'author': 'Odoo PS',
    'website': "https://swww.odoo.com/",
    'depends': ['crm', 'sale_management', 'sale_stock'],
    'data': [
        'data/account_payment_term_data.xml',
        'views/sale_order_views.xml',
    ],
    'assets': {
    },
    'installable': True,
    'license': 'LGPL-3'
}