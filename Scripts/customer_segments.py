def get_profitable_customers(df, top_n=10):
    customer_revenue = df[df['Quantity'] > 0].groupby('CustomerID')['TotalPrice'].sum()
    return customer_revenue.sort_values(ascending=False).head(top_n)
