import pdfplumber
import os

with open(os.path.join("Destination", f"import pdfplumber_CGMC-Report-2023-04.txt"),
                "a",
                encoding="utf-8") as text_file:
    with pdfplumber.open('Source\\CGMC-Report-2023-04.pdf') as pdf:
        # iterate over each page
        
        for page in pdf.pages:
            # extract text
            text = page.extract_text()
            text_file.write(page.extract_text())
            # print(text)

            