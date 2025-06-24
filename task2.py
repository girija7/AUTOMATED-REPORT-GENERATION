from fpdf import FPDF
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import os

# Sample data
data = {
    'Region': ['North', 'South', 'East', 'West'],
    'Sales': [78542, 65421, 52987, 45632],
    'Products': ['Product A', 'Product B', 'Product C', 'Product D'],
    'Units': [1428, 1205, 982, 875],
    'Months': ['Jan', 'Feb', 'Mar'],
    'Monthly_Sales': [45000, 62000, 75000]
}

def generate_sample_pdf():
    # Initialize PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Add title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Q1 2023 Sales Performance Report", ln=1, align='C')
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=1, align='C')
    pdf.ln(10)
    
    # 1. Summary Statistics
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="1. Summary Statistics", ln=1)
    pdf.set_font("Arial", size=10)
    pdf.cell(200, 6, txt="Numerical Summary:", ln=1)
    pdf.cell(200, 6, txt="Units Sold: Mean=24.5, Max=49", ln=1)
    pdf.cell(200, 6, txt="Unit Price: Mean=54.32, Max=99.99", ln=1)
    pdf.cell(200, 6, txt="Total Sales: Mean=1325.42, Max=4899.51", ln=1)
    pdf.ln(5)
    
    # 2. Sales by Region (with chart)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="2. Sales by Region", ln=1)
    
    # Create and save plot
    plt.figure(figsize=(6, 4))
    plt.bar(data['Region'], data['Sales'], color='skyblue')
    plt.title('Total Sales by Region')
    plt.ylabel('Sales ($)')
    plot_filename = "region_sales.png"
    plt.savefig(plot_filename, bbox_inches='tight')
    plt.close()
    
    # Add plot to PDF
    pdf.image(plot_filename, x=30, w=150)
    pdf.ln(60)
    
    # 3. Top Selling Products
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="3. Top Selling Products", ln=1)
    
    # Create table
    pdf.set_font("Arial", size=10)
    col_widths = [60, 50, 60]
    
    # Header
    pdf.cell(col_widths[0], 6, txt="Product", border=1)
    pdf.cell(col_widths[1], 6, txt="Units Sold", border=1)
    pdf.cell(col_widths[2], 6, txt="Total Sales ($)", border=1, ln=1)
    
    # Rows
    for i in range(4):
        pdf.cell(col_widths[0], 6, txt=data['Products'][i], border=1)
        pdf.cell(col_widths[1], 6, txt=str(data['Units'][i]), border=1)
        pdf.cell(col_widths[2], 6, txt=f"{data['Sales'][i]:,}", border=1, ln=1)
    
    pdf.ln(10)
    
    # 4. Monthly Sales Trend
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="4. Monthly Sales Trend", ln=1)
    
    # Create and save plot
    plt.figure(figsize=(6, 4))
    plt.plot(data['Months'], data['Monthly_Sales'], marker='o', color='green')
    plt.title('Monthly Sales Trend')
    plt.ylabel('Sales ($)')
    plot_filename = "monthly_trend.png"
    plt.savefig(plot_filename, bbox_inches='tight')
    plt.close()
    
    # Add plot to PDF
    pdf.image(plot_filename, x=30, w=150)
    
    # Save the PDF
    output_filename = "sample_sales_report.pdf"
    pdf.output(output_filename)
    
    # Clean up
    os.remove("region_sales.png")
    os.remove("monthly_trend.png")
    
    print(f"Sample PDF report generated: {output_filename}")

# Generate the report
generate_sample_pdf()
