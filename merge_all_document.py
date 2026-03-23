import os
from pypdf import PdfWriter

def merge_certificates(input_folder, output_filename):
    merger = PdfWriter()
    
    # Get all pdf files and sort them
    files = [f for f in os.listdir(input_folder) if f.endswith('.pdf')]
    files.sort()
    
    if not files:
        print("No PDF files found in the directory.")
        return

    for filename in files:
        filepath = os.path.join(input_folder, filename)
        print(f"Adding: {filename}")
        merger.append(filepath)

    # Write the merged file to disk
    with open(output_filename, "wb") as output_file:
        merger.write(output_file)
    
    merger.close()
    print(f"\nSuccess! All certificates merged into: {output_filename}")

# Configuration
input_dir = "./folderpath"  # Change this to your folder path
output_path = "all_certificates_merged.pdf"

if __name__ == "__main__":
    # Create directory if it doesn't exist for testing
    if not os.path.exists(input_dir):
        print(f"Please put your PDFs in the '{input_dir}' folder.")
    else:
        merge_certificates(input_dir, output_path)

