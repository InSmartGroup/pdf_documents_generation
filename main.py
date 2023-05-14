import pandas as pd
from fpdf import FPDF

# read the csv file
df = pd.read_csv("topics.csv", sep=",")

# create a pdf object
pdf = FPDF(orientation="portrait", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False)  # prevent page auto-break

# create content
for index, row in df.iterrows():

    # create a title page
    pdf.add_page()
    pdf.set_font(family="Times", size=24, style="B")
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 20, 200, 20)

    # create new lines on the title page
    for line in range(20, 290, 10):
        pdf.set_text_color(180, 180, 180)
        pdf.line(10, line, 200, line)

    # create a footer on the title page
    pdf.ln(260)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(120, 120, 120)
    pdf.cell(txt=row["Topic"], w=0, h=8, align='R', ln=1)

    # create more blank pages in the same topic
    for page in range(row["Pages"] - 1):
        pdf.add_page()

        # create a footer on each blank page
        pdf.ln(272)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(120, 120, 120)
        pdf.cell(txt=row["Topic"], w=0, h=8, align='R', ln=1)

        # create new lines on blank pages
        for line in range(20, 290, 10):
            pdf.set_text_color(180, 180, 180)
            pdf.line(10, line, 200, line)

# write as a pdf file
pdf.output("workbook.pdf")
