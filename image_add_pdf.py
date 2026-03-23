

import os
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import io

def insert_image_as_page(input_pdf_path, image_path, output_path, insert_at_page):
    # 1. Convert the Image to a PDF Page in memory
    img_temp_pdf = io.BytesIO()
    c = canvas.Canvas(img_temp_pdf, pagesize=A4)
    
    # Draw the image to fill the page (adjust width/height if needed)
    # Using 0,0 and A4 dimensions to make it a full-page "certificate"
    c.drawImage(image_path, 0, 0, width=A4[0], height=A4[1], preserveAspectRatio=True)
    c.showPage()
    c.save()
    
    img_temp_pdf.seek(0)
    image_reader = PdfReader(img_temp_pdf)
    image_page = image_reader.pages[0]

    # 2. Read the original PDF
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()
    
    # 3. Insert the image page at the choice position
    # pages.insert() handles the heavy lifting for us
    for page in reader.pages:
        writer.add_page(page)
        
    # insert_at_page is 1-based (e.g., 2 means it becomes the 2nd page)
    # We use index (insert_at_page - 1)
    writer.insert_page(image_page, index=insert_at_page - 1)

    # 4. Save the result
    with open(output_path, "wb") as f:
        writer.write(f)
    
    print(f"Success! Image inserted as page {insert_at_page} in {output_path}")

# --- Configuration ---
config = {
    "input_pdf_path": "input.pdf",
    "image_path": "img.png",
    "output_path": "output.pdf",
    "insert_at_page": 1  # This will make the image the 2nd page
}

if __name__ == "__main__":
    insert_image_as_page(**config)