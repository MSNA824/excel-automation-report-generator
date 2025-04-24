from scripts.load_data import load_data
from scripts.sales_trends import plot_monthly_sales
from scripts.top_products import get_top_products
from scripts.purchase_behavior import average_products_per_transaction
from scripts.customer_segments import get_profitable_customers
from scripts.recommendations import generate_recommendations
from scripts.generate_report import generate_pdf_report

def main():
    df = load_data()

    # Q1: Sales trend
    plot_monthly_sales(df)

    # Q2: Top products
    print("Top Products:\n", get_top_products(df))

    # Q3: Purchase behavior
    print("Average products per transaction:", average_products_per_transaction(df))

    # Q4: Most profitable customers
    print("Top customers:\n", get_profitable_customers(df))

    # Q5: Recommendations
    print("Business Recommendations:")
    for r in generate_recommendations(df):
        print("-", r)
    # generate report
    generate_pdf_report(df, generate_recommendations(df))

if __name__ == "__main__":
    main()
