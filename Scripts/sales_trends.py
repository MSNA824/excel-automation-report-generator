import matplotlib.pyplot as plt
import pandas as pd

def plot_monthly_sales(df):
    df['Month'] = df['InvoiceDate'].dt.to_period('M')
    monthly_sales = df[df['Quantity'] > 0].groupby('Month')['TotalPrice'].sum()

    plt.figure(figsize=(12, 6))
    monthly_sales.plot(kind='bar', color='skyblue')
    plt.title("Monthly Sales Trend")
    plt.ylabel("Revenue (£)")
    plt.xlabel("Month")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
