import pandas as pd

def load_data(path=r'C:\Users\topsa\Desktop\PYTHON\excel-automation-report-generator\raw_data\Sales Transaction.csv'):

    df = pd.read_csv(path, encoding='ISO-8859-1')
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df = df.dropna(subset=['CustomerID'])  # Remove rows without customer
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
    return df
