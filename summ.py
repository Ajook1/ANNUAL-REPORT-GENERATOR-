from pdfminer.high_level import extract_text

def pdf_to_text(pdf_path):
    """
    This function uses PDFMiner.six to extract text from a given PDF file.
    """
    try:
        text = extract_text(pdf_path)
        return text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return None

# Specify the path to the PDF file using a raw string
pdf_path = r'rule.pdf'

# Call the function to extract text
extracted_text = pdf_to_text(pdf_path)

# Print the extracted text or an error message
if extracted_text:
    print(extracted_text)
else:
    print("No text extracted from the PDF.")


