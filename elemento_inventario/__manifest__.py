{
    'name': 'Elemento ERP Inventario',
    'version': '1.0',
    'summary': 'Instala Modulos de Inventario Elemento.',
    'category': 'Elemento Custom',
    'depends': [
        # product-attribute Repo https://github.com/OCA/product-attribute
        'product_lot_sequence', # Adds ability to define a lot sequence from the product which will be proposed upon creating new lots. 

        # stock-logistics-workflow Repo https://github.com/OCA/stock-logistics-workflow
        'stock_no_negative', # You'll be blocked when trying to validate a stock operation that will set the stock level as negative.     
        'stock_move_actual_date', # Adds Stock Move Actual Date field
        'sale_stock_picking_invoice_link', # adds a link between pickings and invoices
#        'sale_order_global_stock_route', # This module adds the possibility to apply a general route on a quotation.

    ],
    'installable': True,
    'application': True,
}