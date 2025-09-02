import pandas as pd

def count_trusted_contacts(customers: pd.DataFrame, contacts: pd.DataFrame, invoices: pd.DataFrame) -> pd.DataFrame:

    contact_customer = contacts.merge(customers, how = 'left', left_on = 'contact_email', right_on = 'email')
    contact_customer = contact_customer.groupby('user_id').agg(contacts_cnt = ('contact_email', 'count'), 
        trusted_contacts_cnt = ('email', 'count'))
    invoices = invoices.merge(customers, how = 'left', left_on = 'user_id', right_on = 'customer_id')
    df = invoices.merge(contact_customer, how = 'left', on = 'user_id')
    df = df.fillna(0)
    return df[['invoice_id', 'customer_name', 'price', 'contacts_cnt', 'trusted_contacts_cnt']].sort_values(by = 'invoice_id')