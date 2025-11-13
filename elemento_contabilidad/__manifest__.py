{
    'name': 'Elemento ERP Contabilidad',
    'version': '1.0',
    'summary': 'Instala Modulos de Contabilidad Elemento.',
    'category': 'Elemento Custom',
    'depends': [
        # account-financial-tools Repo https://github.com/OCA/account-financial-tools
        'account_usability', # Adds missing menu entries for Account module and adds the option to enable Saxon Accounting
        'product_category_tax', # Edit taxes directly in the product category.
        'account_move_print', # Adds the option to print Journal Entries
        'account_move_post_date_user', # Trace journal entry posting date and user.
        'account_move_line_sale_info', # Introduces the sales order line to the journal items
        'account_move_line_purchase_info', # Introduces the purchase order line to the journal items
#        'account_dashboard_banner_mis_builder', # Display MIS builder KPIs in the accounting dashboard banner
#        'account_dashboard_banner', # Add a configurable banner on the accounting dashboard
        
         # account-financial-reporting Repo https://github.com/OCA/account-financial-reporting
        'account_financial_report', # OCA Financial Reports
        'account_tax_balance', # Compute tax balances based on date range
        'account_financial_report_sale', # OCA Financial Reports Sale
        'mis_builder_cash_flow', # MIS Builder Cash Flow
        'mis_template_financial_report', # Profit & Loss / Balance sheet MIS templates
        'partner_statement', # OCA Financial Reports
        
        # account-reconcile Repo https://github.com/OCA/account-reconcile
        'account_reconcile_analytic_tag', # Analytic tags in account reconciliation
        'account_reconcile_model_oca', # This includes the logic moved from Odoo Community to Odoo Enterprise
        'account_reconcile_oca', # Reconcile addons for Odoo CE accounting
        'account_move_base_import', # Journal Entry base import
        'account_statement_base', # Base module for Bank Statements
        'base_transaction_id', # Base transaction ID for financial institutes
        
        # bank-statement-import Repo https://github.com/OCA/bank-statement-import
        'account_statement_import_file_reconcile_oca', # Import Statement Files and Go Direct to Reconciliation
        'account_statement_import_file', # Import Statement Files
#        'account_statement_import_camt54',
#        'account_statement_import_camt',
#        'account_statement_import_base',
#        'account_statement_import_ofx',
        
        # account-invoicing Repo https://github.com/OCA/account-invoicing
        'account_invoice_supplier_ref_unique', # This module checks that a supplier invoice/refund is not entered twice.
        'stock_account_move_reset_to_draft', # Stock account move reset to draft
#        'product_form_account_move_line_link', # Adds a button on product forms to access Journal Items
        
        # account-payment Repo https://github.com/OCA/account-payment
        'account_due_list', # List of open credits and debits, with due date. 
        'account_payment_method_base', # Add form and list view for account.payment.method
        'account_payment_show_invoice', # Extends the tree view of payments to show the paid invoices related to the payments using the vendor reference by default
        'account_payment_widget_amount', # Extends the payment widget to be able to choose the payment amount
        
        # bank-payment Repo https://github.com/OCA/bank-payment
        'account_payment_partner', # Adds payment mode on partners and invoices
        'account_payment_purchase', # Adds Bank Account and Payment Mode on Purchase Orders
        'account_payment_sale', # Adds payment mode on sale orders
        
#        'account_loan', # This module extends the functionality of accounting to support loans.

    ],
    'installable': True,
    'application': True,
}

