import fitz

pdffile = "main.pdf"
doc = fitz.open(pdffile)

for page_i, page in enumerate(doc):
    svg_output = page.get_svg_image(matrix=fitz.Identity)
    output = f"preview/{page_i}.svg"
    with open(output,'w') as file:
        file.write(svg_output)
    