{
    'name': 'Base Mini',
    'version': '1.0',
    'summary': 'Minimal user management without dependencies on default apps like Invoicing or Inventory',
    'author': 'Juan Jose Benites Coronel',
    'category': 'Administration',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'security/base_mini_security.xml',
    ],
    'installable': True,
    'application': False,
}