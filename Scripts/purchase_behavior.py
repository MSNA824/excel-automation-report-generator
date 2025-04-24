def average_products_per_transaction(df):
    valid_tx = df[df['Quantity'] > 0]
    items_per_tx = valid_tx.groupby('InvoiceNo')['Quantity'].sum()
    return items_per_tx.mean()
