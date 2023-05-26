from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")  # P-portray, L-Landscape

df = pd.read_csv("topics.csv")


pdf.add_page()

pdf.set_font(family="Times", style="B", size=12)  # set cells font, mm dont apply for font
pdf.cell(w=40, h=12, txt="Pdf generation:", align="C", ln=0, border=0)
pdf.cell(w=100, h=12, txt="Something:", align="R", ln=0, border=0)  # basically adding text through cells
pdf.cell(w=50, h=12, txt="study materials", align="L", ln=1, border=0)
pdf.cell(w=0, h=5, txt="/\\Hi There/\\", align="C", ln=1, border=0)  # ln = is breakline -> 1 * \n
pdf.cell(w=0, h=2, txt="/*   _      * \\ ", align="C", ln=1, border=0)


pdf.add_page()

pdf.set_font(family="Times", style="B", size=12)
pdf.cell(w=40, h=12, txt="Pdf generation:", align="C", ln=0, border=0)
pdf.cell(w=100, h=12, txt="Something:", align="R", ln=0, border=0)
pdf.cell(w=50, h=12, txt="study materials", align="L", ln=1, border=0)

pdf.output("output.pdf")
