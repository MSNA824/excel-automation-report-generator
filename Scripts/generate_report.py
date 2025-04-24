from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
import os
import matplotlib.pyplot as plt

report_dir = "output"
os.makedirs(report_dir, exist_ok=True)

def save_plot_as_image(plot_func, df, filename, **kwargs):
    path = os.path.join(report_dir, filename)
    plt.figure()
    plot_func(df, **kwargs)
    plt.savefig(path, bbox_inches="tight")
    plt.close()
    return path

def generate_pdf_report(df, recommendations):
    from scripts.sales_trends import plot_monthly_sales
    from scripts.top_products import get_top_products
    from scripts.customer_segments import get_profitable_customers

    pdf_path = os.path.join(report_dir, "final_report.pdf")
    doc = SimpleDocTemplate(pdf_path, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    # Title
    elements.append(Paragraph("UK E-Commerce Sales Analysis Report", styles['Title']))
    elements.append(Spacer(1, 12))

    # Monthly sales plot
    sales_img = save_plot_as_image(plot_monthly_sales, df, "monthly_sales.png")
    elements.append(Paragraph("1. Monthly Sales Trend", styles['Heading2']))
    elements.append(Image(sales_img, width=400, height=200))
    elements.append(Spacer(1, 12))

    # Top products
    top_products = get_top_products(df)
    elements.append(Paragraph("2. Top Purchased Products", styles['Heading2']))
    for product, qty in top_products.items():
        elements.append(Paragraph(f"{product}: {int(qty)} units", styles['Normal']))
    elements.append(Spacer(1, 12))

    # Profitable customers
    top_customers = get_profitable_customers(df)
    elements.append(Paragraph("3. Most Profitable Customers", styles['Heading2']))
    for cust_id, revenue in top_customers.items():
        elements.append(Paragraph(f"Customer {int(cust_id)}: £{revenue:.2f}", styles['Normal']))
    elements.append(Spacer(1, 12))

    # Recommendations
    elements.append(Paragraph("4. Recommendations to Increase Profit", styles['Heading2']))
    for rec in recommendations:
        elements.append(Paragraph(f"• {rec}", styles['Normal']))
    elements.append(Spacer(1, 12))

    doc.build(elements)
    print(f"Report generated: {pdf_path}")
