{
    'name': 'Elemento ERP Partner',
    'version': '1.0',
    'summary': 'Instala Modulos de Partner Elemento.',
    'category': 'Elemento Custom',
    'depends': [
        # partner-contact Repo https://github.com/OCA/partner-contact
        'base_location', # Enhanced zip/npa management system
        'base_location_geonames_import', # Import zip entries from Geonames
        'partner_property', # This module adds the use of properties in partners (different for companies and individuals).
        'partner_supplier_ref', # Adds a supplier reference to contacts
        'partner_ref_unique', # Add an unique constraint to partner ref field
        'base_partner_sequence', # Sets customer's code from a sequence
        'partner_vat_unique', # Module to make the VAT number unique for customers and suppliers.
        'partner_firstname', # Split first name and last name for non company partners
        'base_country_state_translatable', # Translate Country States
        'partner_category_type', # Add a selection field 'Type' to classify Contact Tags.
        'partner_company_default', # This module assigns default company to res.partner.
        'partner_company_type', # Adds a company type to partner that are companies
        'partner_contact_access_link', # Allow to visit the full contact form from a company
    ],
    'installable': True,
    'application': True,
}