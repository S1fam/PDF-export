from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")  # P-portray, L-Landscape


pdf.add_page()
pdf.set_font(family="Times", style="B", size=12)  # set cells font, mm dont apply for font
pdf.cell(w=40, h=12, txt="Pdf generation:", align="C", ln=0, border=0)
pdf.cell(w=100, h=12, txt="Something:", align="R", ln=0, border=0)  # basically adding text through cells
pdf.cell(w=50, h=12, txt="study materials", align="L", ln=1, border=0)
pdf.cell(w=0, h=5, txt="/\\Hi There/\\", align="C", ln=1, border=0)  # ln = is breakline -> 1 * \n
pdf.cell(w=0, h=2, txt="/*   _      * \\ ", align="C", ln=1, border=0)

pdf.set_y(270)  # self promotion :)
pdf.set_x(180)
pdf.set_font("Times", "U", 11)
pdf.cell(w=25, h=6, txt="From portfolio:", border=0, align="C",
         link="https://s1fam-portfolio-home-at8i55.streamlit.app")


df = pd.read_csv("topics.csv")  # df create
pdf.set_auto_page_break(auto=False, margin=0)  # pages should not be broken automatically

for index, row in df.iterrows():  # df rows

    if row["Pages"] > 0:
        pdf.add_page()
        pdf.set_font(family="Times", style="B", size=20)  # set cells font, mm dont apply for font
        pdf.set_text_color(69, 69, 69)
        pdf.cell(w=60, h=12, txt="Pdf generation:", align="R", ln=0, border=0)
        pdf.cell(w=70, h=12, txt=f"{row['Order']}: {row['Topic']}", align="R", ln=0, border=0)
        pdf.cell(w=65, h=12, txt="- study materials", align="L", ln=1, border=0)  # basically adding text through cells
        pdf.line(x1=10, y1=25, x2=200, y2=25)

        pdf.ln(262)  # adds 262 breaklines - limits future content generation
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(150, 150, 150)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        for i in range(row["Pages"] - 1):
            pdf.add_page()
            pdf.line(x1=10, y1=25, x2=200, y2=25)
            pdf.ln(274)
            pdf.set_font(family="Times", style="I", size=8)
            pdf.set_text_color(150, 150, 150)
            pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output.pdf")
