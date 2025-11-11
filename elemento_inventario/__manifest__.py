{
    'name': 'Elemento ERP Inventario',
    'version': '1.0',
    'summary': 'Instala Modulos de Inventario Elemento.',
    'category': 'Elemento Custom',
    'depends': [
        'product_lot_sequence', # Adds ability to define a lot sequence from the product which will be proposed upon creating new lots. 
        'stock_no_negative', # You'll be blocked when trying to validate a stock operation that will set the stock level as negative.     

    ],
    'installable': True,
    'application': True,
}