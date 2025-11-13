{
    'name': 'Elemento ERP Interfaz de Usuario',
    'version': '1.0',
    'summary': 'Instala Modulos de Interfaz de Usuario.',
    'category': 'Elemento Custom',
    'depends': [
        # web Repo https://github.com/OCA/web
        'web_quick_start_screen',
        'web_responsive',
        'web_remember_tree_column_width',
        'web_no_bubble', # Remove the bubbles from the web interface
        'web_excel_export_dynamic_expand', # Export collapsed groups or the full tree, based on its view.
        'web_favicon', # Allows to set a custom shortcut icon (aka favicon)
        'web_pwa_customize', # Web Pwa Customize
        
        # server-brand Repo https://github.com/OCA/server-brand
        'disable_odoo_online', # Remove odoo.com Bindings
        'portal_odoo_debranding', # Remove Odoo Branding from Website
        'remove_odoo_enterprise', # Remove enterprise modules and setting items
        
        # mail Repo https://github.com/OCA/mail
        'mail_debrand',
        
        # (Not Installed on ER) mass-mailing Repo https://github.com/OCA/mass-mailing


    ],
    'installable': True,
    'application': True,
}