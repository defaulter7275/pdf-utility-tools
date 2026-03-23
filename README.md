🛠️ PDF Utility Tools
A collection of lightweight and efficient Python scripts designed to automate common PDF tasks such as merging, image insertion, and high-ratio compression.

🚀 Key Features
PDF Merger: Automatically scans a directory, sorts PDF files, and combines them into a single document.

Image-to-PDF Inserter: Converts an image (like a certificate or cover page) into a full-page PDF and inserts it at a specific page index.

Hard Compression: Utilizes advanced garbage collection and stream deflation to significantly reduce file sizes while maintaining document integrity.

📋 Prerequisites
To run these tools, you will need:

Python 3.10 or higher.

pip (Python package installer).

🛠️ Installation
Clone the repository:

Bash
git clone https://github.com/defaulter7275/pdf-utility-tools.git
cd pdf-utility-tools
Install dependencies:

Bash
pip install -r requirements.txt
📖 How to Use
1. Merging Documents
Place the PDF files you want to combine into the folderpath/ directory and run:

Bash
python merge_all_documents.py
2. Inserting an Image
Update the config dictionary in the script with your file paths and desired page index, then run:

Bash
python image_add_Pdf.py
3. Compressing a PDF
To optimize and shrink a large PDF file, run:

Bash
python pdf_compress.py
🧪 Technical Stack
This project leverages the following industry-standard libraries:

pypdf: For robust PDF reading, writing, and page manipulation.

ReportLab: For programmatically generating PDF pages from images.

PyMuPDF (fitz): For advanced document cleaning and stream-level compression.

👨‍💻 About the Author
Satyam Gupta Third-year College Student | Competitive Programmer | AI/ML Enthusiast