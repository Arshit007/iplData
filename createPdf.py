
# from fpdf import FPDF

# pdf = FPDF(orientation='P', unit='mm', format='A4')
# pdf.add_page()
# pdf.set_font("Arial", size=12)
# pdf.cell(200, 10, txt="2011 Season, Match 15", ln=1, align="C")
# pdf.cell(200, 10, txt="Saturday April 16th 2011", ln=1, align="C")
# pdf.cell(200, 10, txt="Rajiv Gandhi Intl. Cricket Stadium, Hyderabad", ln=1, align="C")
# pdf.cell(200, 10, txt="Deccan Charges vs Kings Eleven Punjab", ln=1, align="C")
# pdf.cell(200, 10, txt="Kings XI Punjab won by 8 wickets", ln=1, align="C")

# pdf.output("simple_demo.pdf")

import pdfkit
pdfkit.from_url('http://google.com', 'simple_demo.pdf')