def get_top_products(df, top_n=10):
    product_counts = df[df['Quantity'] > 0].groupby('Description')['Quantity'].sum()
    top_products = product_counts.sort_values(ascending=False).head(top_n)
    return top_products
