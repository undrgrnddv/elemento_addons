{
    'name': 'Elemento ERP Ventas',
    'version': '1.0',
    'summary': 'Instala Modulos de Ventas Elemento.',
    'category': 'Elemento Custom',
    'depends': [
        'sale_quotation_number', # Different sequence for sale quotations
        'sale_order_product_availability_inline', #Show product availability in sales order line product drop-down.
        'sale_order_line_sequence', #Propagates SO line sequence to invoices and stock picking.
        'sale_order_line_remove', # Allows removal of sale order lines from confirmed orders if not invoiced or received
        'sale_sourced_by_line', # source a line of sale order from a specific warehouse instead of using the warehouse of the sale order
        'sale_stock_picking_note', # Include external (customer) and internal picking note that will be transferred to the picking
        'sale_stock_line_sequence', # Glue module between Sale Order Line Sequence and Stock Picking Line Sequence
        'sale_partner_incoterm', # Set the customer preferred incoterm on each sales order
        # 'sale_order_lot_selection' # allows you to select a lot number on sale order line (Falta desarrollar para funcionalidad completa)

    ],
    'installable': True,
    'application': True,
}