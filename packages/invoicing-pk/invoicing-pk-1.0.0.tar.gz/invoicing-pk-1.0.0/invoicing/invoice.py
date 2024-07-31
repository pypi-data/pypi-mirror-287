import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
import os


def generate(img_path, invoices_path, dest_folder, product_id, product_name,
             amount_purchased, price_per_unit, price):
    """
    This function converts invoice Excel files into PDF invoices.
    :param img_path:
    :param invoices_path:
    :param dest_folder:
    :param product_id:
    :param product_name:
    :param amount_purchased:
    :param price_per_unit:
    :param total_price:
    :return:
    """
    filepaths = glob.glob(f"{invoices_path}/*.xlsx")
    for filepath in filepaths:
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()
        filename = Path(filepath).stem
        invoice_no, date = filename.split("-")

        # invoice no. and date is printed
        pdf.set_font(family="Times", style="B", size=16)
        pdf.cell(w=50, h=8,txt=f"Invoice no. {invoice_no}", align="L", ln=1)
        pdf.cell(w=50, h=8, txt=f"Date {date}", align="L", ln=1)

        # adding header
        data = pd.read_excel(filepath, sheet_name="Sheet 1")
        columns = list(data.columns)
        columns = [items.replace("_", " ").title() for items in columns]
        pdf.set_font(family="Times", style="B", size=10)
        pdf.ln(5)
        pdf.cell(w=35, h=10, txt=columns[0], align="L", border=1)
        pdf.cell(w=45, h=10, txt=columns[1], align="L", border=1)
        pdf.cell(w=35, h=10, txt=columns[2], align="L", border=1)
        pdf.cell(w=35, h=10, txt=columns[3], align="L", border=1)
        pdf.cell(w=35, h=10, txt=columns[4], align="L", border=1, ln=1)

        for index,row in data.iterrows():
            # adding table data
            pdf.set_font(family="Times", size=10)
            pdf.cell(w=35, h=10, txt=f"{row[product_id]}", align="L", border=1)
            pdf.cell(w=45, h=10, txt=f"{row[product_name]}", align="L", border=1)
            pdf.cell(w=35, h=10, txt=f"{row[amount_purchased]}", align="L", border=1)
            pdf.cell(w=35, h=10, txt=f"{row[price_per_unit]}", align="L", border=1)
            pdf.cell(w=35, h=10, txt=f"{row[price]}", align="L", border=1, ln=1)
        # adding total price to the table
        total_price = data[price].sum()
        pdf.set_font(family="Times", size=10)
        pdf.cell(w=35, h=10, txt="", align="L", border=1)
        pdf.cell(w=45, h=10, txt="", align="L", border=1)
        pdf.cell(w=35, h=10, txt="", align="L", border=1)
        pdf.cell(w=35, h=10, txt="", align="L", border=1)
        pdf.cell(w=35, h=10, txt=str(total_price), align="L", border=1, ln=1)

        # add the total price sentence
        pdf.set_font(family="Times", size=10, style="B")
        pdf.cell(w=35, h=10, txt=f"The total price is {total_price}", ln=1)

        # add the total price sentence
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=26, h=10, txt="PythonHow")
        pdf.image(img_path, w=10)

        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)
        pdf.output(f"{dest_folder}/{filename}.pdf")
