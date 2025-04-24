# Excel Automation Report Generator 📊

A Python automation script that processes raw Excel data, formats it, summarizes key metrics, and emails the final report.

## 🚀 Features
- Reads raw Excel files (.xlsx)
- Cleans and formats data (removes blanks, standardizes columns)
- Creates pivot tables and charts
- Saves the output as a formatted report
- Automatically sends the report via email

## 🧰 Tech Stack
- Python 3.x
- pandas
- openpyxl
- matplotlib / seaborn (for charting)
- smtplib (for emailing)

## 📂 Sample Workflow
1. Drop raw Excel files in the `input_data/` folder
2. Run `generate_report.py`
3. Output saved to `output/`
4. Email sent to configured recipient(s)

## 📝 Example Use Cases
- Weekly sales reporting
- Inventory tracking
- Employee productivity summaries

## 🔧 Setup
1. Clone the repo:
   ```bash
   git clone https://github.com/msna824/excel-automation-report-generator.git
   cd excel-automation-report-generator
