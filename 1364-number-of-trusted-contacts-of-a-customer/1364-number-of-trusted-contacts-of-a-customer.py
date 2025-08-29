import pandas as pd

def count_trusted_contacts(customers: pd.DataFrame, contacts: pd.DataFrame, invoices: pd.DataFrame) -> pd.DataFrame:
    # 1. merge customer and contacts
    contact_customer = contacts.merge(customers, how = 'left', left_on = 'contact_email', right_on = 'email') 
    # if email is null means this contact is NOT customer
    # 2. count contacts and trusted contacts
    contact_customer = contact_customer.groupby('user_id').agg(contacts_cnt = ('contact_email', 'count'), trusted_contacts_cnt = ('email', 'count'))
    # 3. merge invoices with customer to get names
    invoices = invoices.merge(customers, how = 'left', left_on = 'user_id', right_on = 'customer_id')
    # 4. merge invoices with contact_customer to get counts, fillna if null
    df = invoices.merge(contact_customer, how = 'left', on = 'user_id').fillna(0)
    # 5. get wanted columns and reorder
    return df[['invoice_id', 'customer_name', 'price', 'contacts_cnt', 'trusted_contacts_cnt']].sort_values(by = 'invoice_id', ascending = True)