import pdfplumber
import re

values = []

with pdfplumber.open("sample.pdf") as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            numbers = re.findall(r'\d+', text)
            values.extend(numbers)

print(values)