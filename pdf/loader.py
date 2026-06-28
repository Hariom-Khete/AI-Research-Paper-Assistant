import pymupdf

def read_pdf(file):

    pdf = pymupdf.open(stream=file.read(), filetype="pdf")

    pages = []

    for page_num, page in enumerate(pdf, start=1):

        pages.append({
            "page": page_num,
            "text": page.get_text()
        })

    pdf.close()

    return pages