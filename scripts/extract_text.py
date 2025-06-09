import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path, output_path="book_text.txt"):
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        text = page.get_text()
        full_text += text
        full_text += "\n--- PAGE BREAK ---\n"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_text)
    print(f"Text extracted and saved to {output_path}")

extract_text_from_pdf("/workspaces/azure-search-openai-demo/data/dioterapevtska_onkologija(6).pdf")
